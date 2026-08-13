import numpy as np


def calculate_expected_loss(
    pd_value,
    lgd_value,
    ead_value
):
    """
    Expected Loss = PD × LGD × EAD
    """

    expected_loss = (
        pd_value
        * lgd_value
        * ead_value
    )

    return np.maximum(
        expected_loss,
        0
    )