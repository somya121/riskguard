import pandas as pd


def backtest_pd(
    y_true,
    predicted_pd,
    n_buckets=10
):

    data = pd.DataFrame({
        "actual_default": y_true.values,
        "predicted_pd": predicted_pd
    })

    data["bucket"] = pd.qcut(
        data["predicted_pd"],
        n_buckets,
        labels=False,
        duplicates="drop"
    )

    result = (
        data
        .groupby("bucket")
        .agg(
            predicted_pd=(
                "predicted_pd",
                "mean"
            ),
            realized_default_rate=(
                "actual_default",
                "mean"
            ),
            observations=(
                "actual_default",
                "count"
            )
        )
        .reset_index()
    )

    result["difference"] = (
        result["realized_default_rate"]
        - result["predicted_pd"]
    )

    return result