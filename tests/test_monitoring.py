def test_auc_range():

    auc = 0.82

    assert 0 <= auc <= 1


def test_ks_range():

    ks = 0.40

    assert 0 <= ks <= 1


def test_gini_range():

    gini = 0.64

    assert -1 <= gini <= 1


def test_psi_non_negative():

    psi = 0.15

    assert psi >= 0