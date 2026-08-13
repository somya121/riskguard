import numpy as np
from sklearn.metrics import (
    roc_auc_score,
    roc_curve
)


def calculate_auc(
    y_true,
    y_score
):
    return roc_auc_score(
        y_true,
        y_score
    )


def calculate_ks(
    y_true,
    y_score
):
    fpr, tpr, thresholds = roc_curve(
        y_true,
        y_score
    )

    return np.max(tpr - fpr)


def calculate_gini(
    y_true,
    y_score
):
    auc = calculate_auc(
        y_true,
        y_score
    )

    return 2 * auc - 1


def calculate_accuracy_ratio(
    y_true,
    y_score
):
    return calculate_gini(
        y_true,
        y_score
    )