import pandas as pd
import numpy as np


def run_stress_test(
    model,
    portfolio,
    features,
    scenarios
):
    """
    Apply macroeconomic stress scenarios
    to a portfolio and measure the impact
    on model-predicted PD.
    """

    # ---------------------------------
    # 1. Baseline portfolio
    # ---------------------------------

    baseline_data = portfolio.copy()

    baseline_X = baseline_data[
        features
    ]

    baseline_pd = model.predict_proba(
        baseline_X
    )[:, 1]

    baseline_avg_pd = (
        baseline_pd.mean()
    )

    # ---------------------------------
    # 2. Initialize results
    # ---------------------------------

    results = [
        {
            "scenario": "Baseline",
            "baseline_pd": baseline_avg_pd,
            "stressed_pd": baseline_avg_pd,
            "pd_change": 0.0,
            "pd_change_pct": 0.0
        }
    ]

    # ---------------------------------
    # 3. Apply stress scenarios
    # ---------------------------------

    for scenario_name, changes in scenarios.items():

        stressed_data = portfolio.copy()

        # Apply macroeconomic changes
        for variable, change in changes.items():

            stressed_data[variable] = (
                stressed_data[variable]
                + change
            )

        # Select model features
        stressed_X = stressed_data[
            features
        ]

        # Generate stressed PD
        stressed_pd = model.predict_proba(
            stressed_X
        )[:, 1]

        stressed_avg_pd = (
            stressed_pd.mean()
        )

        # Absolute PD change
        pd_change = (
            stressed_avg_pd
            - baseline_avg_pd
        )

        # Relative PD change
        if baseline_avg_pd != 0:

            pd_change_pct = (
                pd_change
                / baseline_avg_pd
            ) * 100

        else:

            pd_change_pct = np.nan

        results.append({
            "scenario": scenario_name,
            "baseline_pd": baseline_avg_pd,
            "stressed_pd": stressed_avg_pd,
            "pd_change": pd_change,
            "pd_change_pct": pd_change_pct
        })

    return pd.DataFrame(results)