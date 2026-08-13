import numpy as np


def calculate_psi(
    expected,
    actual,
    bins=10
):

    expected = np.asarray(expected)
    actual = np.asarray(actual)

    breakpoints = np.quantile(
        expected,
        np.linspace(0, 1, bins + 1)
    )

    breakpoints = np.unique(
        breakpoints
    )

    expected_counts, _ = np.histogram(
        expected,
        bins=breakpoints
    )

    actual_counts, _ = np.histogram(
        actual,
        bins=breakpoints
    )

    expected_pct = (
        expected_counts
        / len(expected)
    )

    actual_pct = (
        actual_counts
        / len(actual)
    )

    expected_pct = np.clip(
        expected_pct,
        0.0001,
        None
    )

    actual_pct = np.clip(
        actual_pct,
        0.0001,
        None
    )

    psi = np.sum(
        (
            actual_pct
            - expected_pct
        )
        *
        np.log(
            actual_pct
            / expected_pct
        )
    )

    return psi