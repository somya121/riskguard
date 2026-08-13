import numpy as np
import pandas as pd


def generate_credit_portfolio(
    n_customers=10000,
    start_date="2022-01-01",
    n_months=24,
    random_state=42
):
    rng = np.random.default_rng(random_state)

    dates = pd.date_range(
        start=start_date,
        periods=n_months,
        freq="MS"
    )

    customer_ids = np.arange(
        1,
        n_customers + 1
    )

    df = pd.DataFrame({
        "customer_id": np.repeat(
            customer_ids,
            len(dates)
        ),
        "observation_date": np.tile(
            dates,
            n_customers
        )
    })

    n = len(df)

    # Customer characteristics

    df["age"] = rng.normal(
        42, 10, n
    ).clip(21, 75).round()

    df["annual_income"] = rng.lognormal(
        mean=np.log(60000),
        sigma=0.5,
        size=n
    ).clip(15000, 500000)

    df["employment_years"] = (
        (df["age"] - 21)
        * rng.uniform(0.2, 0.8, n)
    ).clip(0, 40)

    # Credit characteristics

    df["credit_score"] = rng.normal(
        680,
        60,
        n
    ).clip(300, 850).round()

    df["debt_to_income"] = rng.beta(
        2,
        5,
        n
    ).clip(0.01, 0.95)

    df["credit_utilization"] = rng.beta(
        2,
        3,
        n
    ).clip(0.01, 0.99)

    df["previous_defaults"] = rng.poisson(
        0.15,
        n
    ).clip(0, 5)

    df["delinquencies_12m"] = rng.poisson(
        0.5,
        n
    ).clip(0, 8)

    # Loan characteristics

    df["loan_amount"] = rng.lognormal(
        mean=np.log(15000),
        sigma=0.6,
        size=n
    ).clip(1000, 100000)

    df["loan_term_months"] = rng.choice(
        [12, 24, 36, 48, 60],
        size=n,
        p=[0.10, 0.20, 0.35, 0.20, 0.15]
    )

    df["interest_rate"] = rng.normal(
        8.5,
        2,
        n
    ).clip(3, 20)

    # Macroeconomic variables

    month_number = (
        df["observation_date"]
        .dt.to_period("M")
        .astype(int)
    )

    df["unemployment_rate"] = (
        5.5
        + 0.4 * np.sin(month_number / 4)
        + rng.normal(0, 0.15, n)
    ).clip(3, 12)

    df["gdp_growth"] = (
        2.5
        - 0.5 * (
            df["unemployment_rate"] - 5.5
        )
        + rng.normal(0, 0.3, n)
    )

    # Latent default risk

    risk_score = (
        -4.5
        - 0.008 * (
            df["credit_score"] - 650
        )
        + 2.5 * df["debt_to_income"]
        + 1.5 * df["credit_utilization"]
        + 0.45 * df["previous_defaults"]
        + 0.25 * df["delinquencies_12m"]
        + 0.06 * df["interest_rate"]
        + 0.12 * df["unemployment_rate"]
        - 0.08 * df["gdp_growth"]
    )

    true_pd = (
        1 / (1 + np.exp(-risk_score))
    )

    df["default_flag"] = rng.binomial(
        1,
        true_pd
    )

    # Research-only true PD
    df["true_pd"] = true_pd

    # LGD

    recovery_rate = (
        0.55
        - 0.15 * df["credit_utilization"]
        - 0.10 * df["debt_to_income"]
        + rng.normal(0, 0.08, n)
    ).clip(0.05, 0.95)

    df["lgd"] = 1 - recovery_rate

    # EAD

    ccf = (
        0.65
        + rng.normal(0, 0.10, n)
    ).clip(0.20, 1.00)

    df["ead"] = (
        df["loan_amount"] * ccf
    )

    return df.reset_index(drop=True)