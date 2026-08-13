from pathlib import Path

import pandas as pd


FANNIE_COLUMNS = [
    # 1-10
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

    # 11-20
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

    # 21-30
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

    # 31-40
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

    # 41-50
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

    # 51-60
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

    # 61-70
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

    # 71-80
    "CURRENT_BORROWER_FICO",
    "CURRENT_CO_BORROWER_FICO",
    "MORTGAGE_INSURANCE_TYPE",
    "SERVICING_ACTIVITY_INDICATOR",
    "CURRENT_PERIOD_MODIFICATION_LOSS_AMOUNT",
    "CUMULATIVE_MODIFICATION_LOSS_AMOUNT",
    "CURRENT_PERIOD_CREDIT_EVENT_NET_GAIN_OR_LOSS",
    "CUMULATIVE_CREDIT_EVENT_NET_GAIN_OR_LOSS",
    "SPECIAL_ELIGIBILITY_PROGRAM",
    "FORECLOSURE_PRINCIPAL_WRITE_OFF_AMOUNT",

    # 81-90
    "RELOCATION_MORTGAGE_INDICATOR",
    "ZERO_BALANCE_CODE_CHANGE_DATE",
    "LOAN_HOLDBACK_INDICATOR",
    "LOAN_HOLDBACK_EFFECTIVE_DATE",
    "DELINQUENT_INTEREST",
    "PROPERTY_VALUATION_METHOD",
    "HIGH_BALANCE_LOAN_INDICATOR",
    "ARM_INITIAL_FIXED_RATE_PERIOD_5YR_INDICATOR",
    "ARM_PRODUCT_TYPE",
    "INITIAL_FIXED_RATE_PERIOD",

    # 91-100
    "INTEREST_RATE_ADJUSTMENT_FREQUENCY",
    "NEXT_INTEREST_RATE_CHANGE_DATE",
    "NEXT_PAYMENT_CHANGE_DATE",
    "ARM_INDEX",
    "ARM_CAP_STRUCTURE",
    "INITIAL_INTEREST_RATE_CAP_UP_PERCENT",
    "PERIODIC_INTEREST_RATE_CAP_UP_PERCENT",
    "LIFETIME_INTEREST_RATE_CAP_UP_PERCENT",
    "MORTGAGE_MARGIN",
    "ARM_BALLOON_INDICATOR",

    # 101-110
    "ARM_PLAN_NUMBER",
    "BORROWER_ASSISTANCE_PLAN",
    "HLTV_REFINANCE_OPTION_INDICATOR",
    "DEAL_NAME",
    "REPURCHASE_MAKE_WHOLE_PROCEEDS_FLAG",
    "ALTERNATIVE_DELINQUENCY_RESOLUTION",
    "ALTERNATIVE_DELINQUENCY_RESOLUTION_COUNT",
    "TOTAL_DEFERRAL_AMOUNT",
    "PAYMENT_DEFERRAL_MODIFICATION_EVENT_INDICATOR",
    "INTEREST_BEARING_UPB",

    # 111-113
    "ORIGINATION_CLASSIC_FICO",
    "ISSUANCE_CLASSIC_FICO",
    "CURRENT_CLASSIC_FICO",
]


PROJECT_ROOT = Path(__file__).resolve().parents[2]

FANNIE_ROOT = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "fannie_mae"
)


def load_fannie_file(path, chunksize=None):
    """
    Load one Fannie Mae Single-Family
    Loan Performance CSV.

    The 2018 files are pipe-delimited
    and do not contain a usable header,
    so the official field layout is supplied
    explicitly.
    """

    path = Path(path)

    if not path.is_absolute():
        path = PROJECT_ROOT / path

    if not path.exists():
        raise FileNotFoundError(
            f"Fannie Mae file not found: {path}"
        )

    df = pd.read_csv(
        path,
        sep="|",
        header=None,
        names=FANNIE_COLUMNS,
        chunksize=chunksize,
        dtype="string",
        low_memory=False,
    )

    return df


def load_fannie_quarter(
    year,
    quarter,
    chunksize=None
):
    """
    Load one Fannie Mae acquisition-quarter file.

    Example
    -------
    load_fannie_quarter(2018, "Q1")
    """

    path = (
        FANNIE_ROOT
        / str(year)
        / f"{year}{quarter}"
        / f"{year}{quarter}.csv"
    )

    return load_fannie_file(path, chunksize=chunksize)


def load_fannie_2018_chunks(chunksize=100_000):
    """
    Load the currently selected migration scope:

        2018Q1
        2018Q2

    Monthly performance observations are retained.

    No duplicate removal is performed because
    multiple rows for the same LOAN_ID are expected.
    """
    for quarter in ["Q1", "Q2"]:
        reader = load_fannie_quarter(
            2018,
            quarter,
            chunksize=chunksize
        )
        for chunk in reader:
            chunk["source_quarter"] = f"{quarter} 2018"
            yield chunk



def get_fannie_file_summary(df):
    """
    Return basic information about
    the loaded Fannie Mae dataset.
    """

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "unique_loans": df["LOAN_ID"].nunique(),
        "duplicate_loan_rows": (
            df["LOAN_ID"].duplicated().sum()
        ),
        "min_activity_period": (
            df["ACT_PERIOD"].min()
        ),
        "max_activity_period": (
            df["ACT_PERIOD"].max()
        ),
    }