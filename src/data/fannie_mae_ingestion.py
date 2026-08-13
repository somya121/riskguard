from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from src.data.fannie_mae_loader import (
    load_fannie_quarter,
)

from src.data.preprocessing import (
    preprocess_fannie_data,
)


def _align_chunk_to_schema(
    processed,
    canonical_schema,
):
    """
    Make a processed pandas DataFrame compatible with
    the canonical Arrow schema created from the first chunk.

    This handles:
        1. Column ordering
        2. Missing columns
        3. Extra columns
        4. Timestamp precision differences
        5. Integer/float/object dtype differences
    """

    canonical_columns = canonical_schema.names

    # ---------------------------------------------------------
    # Ensure the DataFrame contains exactly the canonical
    # columns and in exactly the same order.
    #
    # Missing columns are created as NaN.
    # Extra columns are removed.
    # ---------------------------------------------------------

    processed = processed.reindex(
        columns=canonical_columns
    )

    # ---------------------------------------------------------
    # Convert pandas DataFrame -> Arrow
    # ---------------------------------------------------------

    table = pa.Table.from_pandas(
        processed,
        preserve_index=False,
    )

    # ---------------------------------------------------------
    # Force the exact schema of the first chunk.
    #
    # safe=False is intentional here because Arrow may need
    # to convert:
    #
    # timestamp[s] -> timestamp[us]
    # float64 -> int64
    # etc.
    # ---------------------------------------------------------

    table = table.cast(
        canonical_schema,
        safe=False,
    )

    return table


def process_fannie_quarter(
    year,
    quarter,
    output_path,
    chunksize=100_000,
):
    """
    Process one Fannie Mae acquisition-quarter file
    in memory-safe chunks and write the cleaned result
    to a Parquet file.

    The first processed chunk defines the canonical
    Parquet schema.

    Every subsequent chunk is aligned and cast to
    exactly the same schema before being written.

    Parameters
    ----------
    year : int
        Fannie Mae data year.

    quarter : str
        Quarter such as "Q1", "Q2", "Q3", "Q4".

    output_path : str or Path
        Destination Parquet file.

    chunksize : int
        Number of rows processed per chunk.

    Returns
    -------
    Path
        Path to the generated Parquet file.
    """

    output_path = Path(output_path)

    # ---------------------------------------------------------
    # Create output directory if it does not exist
    # ---------------------------------------------------------

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # ---------------------------------------------------------
    # Load raw Fannie Mae data in chunks
    # ---------------------------------------------------------

    reader = load_fannie_quarter(
        year,
        quarter,
        chunksize=chunksize,
    )

    writer = None
    canonical_schema = None

    total_rows = 0
    total_chunks = 0

    try:

        # =====================================================
        # PROCESS EACH CHUNK
        # =====================================================

        for chunk_number, chunk in enumerate(
            reader,
            start=1,
        ):

            total_chunks += 1

            print(
                f"Processing {year}{quarter} "
                f"chunk {chunk_number}..."
            )

            # -------------------------------------------------
            # Add source metadata
            # -------------------------------------------------

            chunk["source_year"] = year

            chunk["source_quarter"] = (
                f"{quarter} {year}"
            )

            # -------------------------------------------------
            # Preprocess current chunk
            # -------------------------------------------------

            processed = preprocess_fannie_data(
                chunk
            )

            total_rows += len(processed)

            print(
                f"Chunk rows: {len(processed):,}"
            )

            # -------------------------------------------------
            # Convert pandas -> Arrow
            # -------------------------------------------------

            table = pa.Table.from_pandas(
                processed,
                preserve_index=False,
            )

            # =================================================
            # FIRST CHUNK
            # =================================================

            if writer is None:

                canonical_schema = table.schema

                writer = pq.ParquetWriter(
                    output_path,
                    canonical_schema,
                    compression="snappy",
                )

                print(
                    "Canonical Parquet schema created."
                )

            # =================================================
            # SUBSEQUENT CHUNKS
            # =================================================

            else:

                # ------------------------------------------------
                # Check whether the column structure is different
                # ------------------------------------------------

                if table.column_names != (
                    canonical_schema.names
                ):

                    print(
                        f"Column structure differs "
                        f"in chunk {chunk_number}. "
                        f"Aligning to canonical schema..."
                    )

                # ------------------------------------------------
                # Align and cast every subsequent chunk
                # ------------------------------------------------

                table = _align_chunk_to_schema(
                    processed,
                    canonical_schema,
                )

            # -------------------------------------------------
            # Write current chunk
            # -------------------------------------------------

            writer.write_table(
                table
            )

            # -------------------------------------------------
            # Progress information
            # -------------------------------------------------

            print(
                f"Successfully wrote chunk "
                f"{chunk_number}."
            )

    finally:

        # -----------------------------------------------------
        # Always close the Parquet writer.
        #
        # This is extremely important because closing the
        # writer finalizes the Parquet file metadata.
        # -----------------------------------------------------

        if writer is not None:
            writer.close()

    # =========================================================
    # FINAL SUMMARY
    # =========================================================

    print()
    print("=" * 60)
    print(
        f"Completed {year}{quarter}"
    )
    print(
        f"Total chunks: {total_chunks:,}"
    )
    print(
        f"Total rows: {total_rows:,}"
    )
    print(
        f"Output: {output_path}"
    )
    print("=" * 60)

    return output_path