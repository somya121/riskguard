from pathlib import Path

from src.data.fannie_mae_loader import (
    load_fannie_2018,
    get_fannie_file_summary,
)

from src.data.preprocessing import (
    preprocess_fannie_data,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

CANONICAL_OUTPUT = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "credit_portfolio.csv"
)


def build_canonical_dataset(
    output_path=CANONICAL_OUTPUT,
):
    """
    Build the canonical dataset
    from Fannie Mae 2018Q1 + 2018Q2.
    """

    print(
        "Loading Fannie Mae 2018Q1 + 2018Q2..."
    )

    raw_df = load_fannie_2018()

    print(
        f"Raw rows: {len(raw_df):,}"
    )

    print(
        f"Unique loans: "
        f"{raw_df['LOAN_ID'].nunique():,}"
    )

    df = preprocess_fannie_data(
        raw_df
    )

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Canonical dataset written to:\n"
        f"{output_path}"
    )

    print(
        f"Rows: {len(df):,}"
    )

    print(
        f"Columns: {len(df.columns)}"
    )

    print(
        f"Unique loans: "
        f"{df['loan_id'].nunique():,}"
    )

    return df