import numpy as np


def calculate_sensitivity(
    model,
    data,
    feature,
    changes
):

    baseline_data = data.copy()

    baseline_pd = (
        model
        .predict_proba(
            baseline_data
        )[:, 1]
    )

    results = []

    for change in changes:

        stressed_data = (
            data.copy()
        )

        stressed_data[feature] = (
            stressed_data[feature]
            + change
        )

        stressed_pd = (
            model
            .predict_proba(
                stressed_data
            )[:, 1]
        )

        results.append({
            "feature": feature,
            "change": change,
            "baseline_pd":
                np.mean(baseline_pd),
            "stressed_pd":
                np.mean(stressed_pd),
            "pd_change":
                np.mean(stressed_pd)
                - np.mean(baseline_pd)
        })

    return results