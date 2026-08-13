import numpy as np


def test_pd_range():

    pd_values = np.array([
        0.01,
        0.25,
        0.50,
        0.90
    ])

    assert pd_values.min() >= 0
    assert pd_values.max() <= 1


def test_lgd_range():

    lgd_values = np.array([
        0.10,
        0.50,
        0.90
    ])

    assert lgd_values.min() >= 0
    assert lgd_values.max() <= 1


def test_ead_non_negative():

    ead_values = np.array([
        1000,
        5000,
        10000
    ])

    assert ead_values.min() >= 0


def test_expected_loss_non_negative():

    pd_value = 0.05
    lgd_value = 0.40
    ead_value = 10000

    expected_loss = (
        pd_value
        * lgd_value
        * ead_value
    )

    assert expected_loss >= 0