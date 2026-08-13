from pathlib import Path

import pandas as pd


FANNIE_COLUMNS = [
    "POOL_ID",
    "LOAN_ID",
    "ACT_PERIOD",
    "CHANNEL",
    "SELLER",
    "SERVICER",
    "MASTER_SERVICER",
    "ORIG_RATE",
    "CURR_RATE",
    "ORIG_UPB",
    "ISSUANCE_UPB",
    "CURRENT_UPB",
    "ORIG_TERM",
    "ORIG_DATE",
    "FIRST_PAY",
    "LOAN_AGE",
    "REM_MONTHS",
    "ADJ_REM_MONTHS",
    "MATR_DT",
    "OLTV",
    "OCLTV",
    "NUM_BO",
    "DTI",
    "CSCORE_B",
    "CSCORE_C",
    "FIRST_FLAG",
    "PURPOSE",
    "PROP",
    "NO_UNITS",
    "OCC_STAT",
    "STATE",
    "MSA",
    "ZIP",
    "MI_PCT",
    "PRODUCT",
    "PPMT_FLG",
    "IO",
    "FIRST_PAY_IO",
    "MNTHS_TO_AMTZ_IO",
    "DLQ_STATUS",
    "PMT_HISTORY",
    "MOD_FLAG",
    "MI_CANCEL_FLAG",
    "ZERO_BALANCE_CODE",
    "ZB_DTE",
    "LAST_UPB",
    "RPRCH_DTE",
    "CURR_SCHD_PRNCPL",
    "TOT_SCHD_PRNCPL",
    "UNSCHD_PRNCPL_CURR",
    "LAST_PAID_INSTALLMENT_DATE",
    "FORECLOSURE_DATE",
    "DISPOSITION_DATE",
    "FORECLOSURE_COSTS",
    "PROPERTY_PRESERVATION_AND_REPAIR_COSTS",
    "ASSET_RECOVERY_COSTS",
    "MISC_HOLDING_EXPENSES_AND_CREDITS",
    "ASSOCIATED_TAXES",
    "NET_SALES_PROCEEDS",
    "CREDIT_ENHANCEMENT_PROCEEDS",
    "REPURCHASE_MAKE_WHOLE_PROCEEDS",
    "OTHER_FORECLOSURE_PROCEEDS",
    "NON_INTEREST_BEARING_UPB",
    "PRINCIPAL_FORGIVENESS_UPB",
    "ORIGINAL_LIST_START_DATE",
    "ORIGINAL_LIST_PRICE",
    "CURRENT_LIST_START_DATE",
    "CURRENT_LIST_PRICE",
    "BORROWER_FICO_AT_ISSUANCE",
    "COBORROWER_FICO_AT_ISSUANCE",
    "CURRENT_BORROWER_FICO",
    "CURRENT_CO_BORROWER_FICO",
    "MORTGAGE_INSURANCE_TYPE",
    "SERVICING_ACTIVITY_INDICATOR",
    "CURRENT_PERIOD_MODIFICATION_LOSS_AMOUNT",
    "CUMULATIVE_MODIFICATION_LOSS_AMOUNT",
    "CURRENT_PERIOD_CREDIT_EVENT_NET_GAIN_OR_LOSS",
    "CUMULATIVE_CREDIT_EVENT_NET_GAIN_OR_LOSS",
    "HOMEREADY_INDICATOR",
]

def load_fannie_file(path):
    """
    Load one Fannie Mae Single-Family Loan Performance CSV.
    """

    path = Path(path)

    df = pd.read_csv(
        path,
        sep="|",
        header=None,
        names=FANNIE_COLUMNS,
        low_memory=False,
    )

    return df

def load_fannie_2018():
    """
    Load 2018Q1 and 2018Q2 Fannie Mae data.
    """

    base_path = Path("data/raw/fannie_mae/2018")

    q1_path = base_path / "2018Q1" / "2018Q1.csv"
    q2_path = base_path / "2018Q2" / "2018Q2.csv"

    q1 = load_fannie_file(q1_path)
    q2 = load_fannie_file(q2_path)

    df = pd.concat(
        [q1, q2],
        ignore_index=True
    )

    return df