import pandas as pd


# ============================================================
# FANNIE MAE DATE COLUMNS
# ============================================================

STRING_COLUMNS = [
    "loan_id",
    "pool_id",
    "channel",
    "seller",
    "servicer",
    "master_servicer",
    "payment_history",
    "borrower_assistance_plan",
    "alternative_delinquency_resolution",
    "deal_name",
    "state",
    "zip3",
    "msa",
    "delinquency_status",
    "zero_balance_code",
]

MONTH_YEAR_COLUMNS = [
    "observation_date",
    "origination_date",
    "first_payment_date",
    "maturity_date",
    "zero_balance_date",
    "repurchase_date",
    "last_paid_installment_date",
    "foreclosure_date",
    "disposition_date",
    "original_list_start_date",
    "current_list_start_date",
]


# ============================================================
# FANNIE MAE NUMERIC COLUMNS
# ============================================================

NUMERIC_COLUMNS = [
    "original_interest_rate",
    "current_interest_rate",
    "original_upb",
    "issuance_upb",
    "current_upb",
    "original_loan_term",
    "loan_age",
    "remaining_months",
    "adjusted_remaining_months",
    "original_ltv",
    "original_cltv",
    "number_of_borrowers",
    "debt_to_income",
    "borrower_credit_score",
    "co_borrower_credit_score",
    "number_of_units",
    "mortgage_insurance_pct",
    "last_upb",
    "scheduled_principal_current",
    "total_principal_current",
    "unscheduled_principal_current",
    "foreclosure_costs",
    "property_preservation_and_repair_costs",
    "asset_recovery_costs",
    "misc_holding_expenses_and_credits",
    "associated_taxes",
    "net_sales_proceeds",
    "credit_enhancement_proceeds",
    "repurchase_make_whole_proceeds",
    "other_foreclosure_proceeds",
    "non_interest_bearing_upb",
    "principal_forgiveness_upb",
    "original_list_price",
    "current_list_price",
    "borrower_fico_at_issuance",
    "co_borrower_fico_at_issuance",
    "current_borrower_fico",
    "current_co_borrower_fico",
    "current_period_modification_loss_amount",
    "cumulative_modification_loss_amount",
    "current_period_credit_event_net_gain_or_loss",
    "cumulative_credit_event_net_gain_or_loss",

    # Additional 2018 schema fields
    "foreclosure_principal_write_off_amount",
    "delinquent_interest",
    "total_deferral_amount",

    # ARM fields
    "initial_fixed_rate_period",
    "interest_rate_adjustment_frequency",
    "initial_interest_rate_cap_up_percent",
    "periodic_interest_rate_cap_up_percent",
    "lifetime_interest_rate_cap_up_percent",
    "mortgage_margin",
]


# ============================================================
# FANNIE MAE COLUMN RENAME MAP
# ============================================================

RENAME_MAP = {

    # --------------------------------------------------------
    # 1-10
    # --------------------------------------------------------

    "POOL_ID": "pool_id",
    "LOAN_ID": "loan_id",
    "ACT_PERIOD": "observation_date",
    "CHANNEL": "channel",
    "SELLER": "seller",
    "SERVICER": "servicer",
    "MASTER_SERVICER": "master_servicer",
    "ORIG_RATE": "original_interest_rate",
    "CURR_RATE": "current_interest_rate",
    "ORIG_UPB": "original_upb",

    # --------------------------------------------------------
    # 11-20
    # --------------------------------------------------------

    "ISSUANCE_UPB": "issuance_upb",
    "CURRENT_UPB": "current_upb",
    "ORIG_TERM": "original_loan_term",
    "ORIG_DATE": "origination_date",
    "FIRST_PAY": "first_payment_date",
    "LOAN_AGE": "loan_age",
    "REM_MONTHS": "remaining_months",
    "ADJ_REM_MONTHS": "adjusted_remaining_months",
    "MATR_DT": "maturity_date",
    "OLTV": "original_ltv",

    # --------------------------------------------------------
    # 21-30
    # --------------------------------------------------------

    "OCLTV": "original_cltv",
    "NUM_BO": "number_of_borrowers",
    "DTI": "debt_to_income",
    "CSCORE_B": "borrower_credit_score",
    "CSCORE_C": "co_borrower_credit_score",
    "FIRST_FLAG": "first_time_homebuyer",
    "PURPOSE": "loan_purpose",
    "PROP": "property_type",
    "NO_UNITS": "number_of_units",
    "OCC_STAT": "occupancy_status",

    # --------------------------------------------------------
    # 31-40
    # --------------------------------------------------------

    "STATE": "state",
    "MSA": "msa",
    "ZIP": "zip3",
    "MI_PCT": "mortgage_insurance_pct",
    "PRODUCT": "product_type",
    "PPMT_FLG": "prepayment_flag",
    "IO": "interest_only_flag",
    "FIRST_PAY_IO": "first_payment_io_date",
    "MNTHS_TO_AMTZ_IO": "months_to_amortization_io",
    "DLQ_STATUS": "delinquency_status",

    # --------------------------------------------------------
    # 41-50
    # --------------------------------------------------------

    "PMT_HISTORY": "payment_history",
    "MOD_FLAG": "modification_flag",
    "MI_CANCEL_FLAG": "mi_cancel_flag",
    "ZERO_BALANCE_CODE": "zero_balance_code",
    "ZB_DTE": "zero_balance_date",
    "LAST_UPB": "last_upb",
    "RPRCH_DTE": "repurchase_date",
    "CURR_SCHD_PRNCPL": "scheduled_principal_current",
    "TOT_SCHD_PRNCPL": "total_principal_current",
    "UNSCHD_PRNCPL_CURR": "unscheduled_principal_current",

    # --------------------------------------------------------
    # 51-60
    # --------------------------------------------------------

    "LAST_PAID_INSTALLMENT_DATE":
        "last_paid_installment_date",

    "FORECLOSURE_DATE":
        "foreclosure_date",

    "DISPOSITION_DATE":
        "disposition_date",

    "FORECLOSURE_COSTS":
        "foreclosure_costs",

    "PROPERTY_PRESERVATION_AND_REPAIR_COSTS":
        "property_preservation_and_repair_costs",

    "ASSET_RECOVERY_COSTS":
        "asset_recovery_costs",

    "MISC_HOLDING_EXPENSES_AND_CREDITS":
        "misc_holding_expenses_and_credits",

    "ASSOCIATED_TAXES":
        "associated_taxes",

    "NET_SALES_PROCEEDS":
        "net_sales_proceeds",

    "CREDIT_ENHANCEMENT_PROCEEDS":
        "credit_enhancement_proceeds",

    # --------------------------------------------------------
    # 61-70
    # --------------------------------------------------------

    "REPURCHASE_MAKE_WHOLE_PROCEEDS":
        "repurchase_make_whole_proceeds",

    "OTHER_FORECLOSURE_PROCEEDS":
        "other_foreclosure_proceeds",

    "NON_INTEREST_BEARING_UPB":
        "non_interest_bearing_upb",

    "PRINCIPAL_FORGIVENESS_UPB":
        "principal_forgiveness_upb",

    "ORIGINAL_LIST_START_DATE":
        "original_list_start_date",

    "ORIGINAL_LIST_PRICE":
        "original_list_price",

    "CURRENT_LIST_START_DATE":
        "current_list_start_date",

    "CURRENT_LIST_PRICE":
        "current_list_price",

    "BORROWER_FICO_AT_ISSUANCE":
        "borrower_fico_at_issuance",

    "COBORROWER_FICO_AT_ISSUANCE":
        "co_borrower_fico_at_issuance",

    # --------------------------------------------------------
    # 71-80
    # --------------------------------------------------------

    "CURRENT_BORROWER_FICO":
        "current_borrower_fico",

    "CURRENT_CO_BORROWER_FICO":
        "current_co_borrower_fico",

    "MORTGAGE_INSURANCE_TYPE":
        "mortgage_insurance_type",

    "SERVICING_ACTIVITY_INDICATOR":
        "servicing_activity_indicator",

    "CURRENT_PERIOD_MODIFICATION_LOSS_AMOUNT":
        "current_period_modification_loss_amount",

    "CUMULATIVE_MODIFICATION_LOSS_AMOUNT":
        "cumulative_modification_loss_amount",

    "CURRENT_PERIOD_CREDIT_EVENT_NET_GAIN_OR_LOSS":
        "current_period_credit_event_net_gain_or_loss",

    "CUMULATIVE_CREDIT_EVENT_NET_GAIN_OR_LOSS":
        "cumulative_credit_event_net_gain_or_loss",

    "SPECIAL_ELIGIBILITY_PROGRAM":
        "eligibility_program_raw",

    "FORECLOSURE_PRINCIPAL_WRITE_OFF_AMOUNT":
        "foreclosure_principal_write_off_amount",

    # --------------------------------------------------------
    # 81-90
    # --------------------------------------------------------

    "RELOCATION_MORTGAGE_INDICATOR":
        "relocation_mortgage_indicator",

    "ZERO_BALANCE_CODE_CHANGE_DATE":
        "zero_balance_code_change_date",

    "LOAN_HOLDBACK_INDICATOR":
        "loan_holdback_indicator",

    "LOAN_HOLDBACK_EFFECTIVE_DATE":
        "loan_holdback_effective_date",

    "DELINQUENT_INTEREST":
        "delinquent_interest",

    "PROPERTY_VALUATION_METHOD":
        "property_valuation_method",

    "HIGH_BALANCE_LOAN_INDICATOR":
        "high_balance_loan_indicator",

    "ARM_INITIAL_FIXED_RATE_PERIOD_5YR_INDICATOR":
        "arm_initial_fixed_rate_period_5yr_indicator",

    "ARM_PRODUCT_TYPE":
        "arm_product_type",

    "INITIAL_FIXED_RATE_PERIOD":
        "initial_fixed_rate_period",

    # --------------------------------------------------------
    # 91-100
    # --------------------------------------------------------

    "INTEREST_RATE_ADJUSTMENT_FREQUENCY":
        "interest_rate_adjustment_frequency",

    "NEXT_INTEREST_RATE_CHANGE_DATE":
        "next_interest_rate_change_date",

    "NEXT_PAYMENT_CHANGE_DATE":
        "next_payment_change_date",

    "ARM_INDEX":
        "arm_index",

    "ARM_CAP_STRUCTURE":
        "arm_cap_structure",

    "INITIAL_INTEREST_RATE_CAP_UP_PERCENT":
        "initial_interest_rate_cap_up_percent",

    "PERIODIC_INTEREST_RATE_CAP_UP_PERCENT":
        "periodic_interest_rate_cap_up_percent",

    "LIFETIME_INTEREST_RATE_CAP_UP_PERCENT":
        "lifetime_interest_rate_cap_up_percent",

    "MORTGAGE_MARGIN":
        "mortgage_margin",

    "ARM_BALLOON_INDICATOR":
        "arm_balloon_indicator",

    # --------------------------------------------------------
    # 101-110
    # --------------------------------------------------------

    "ARM_PLAN_NUMBER":
        "arm_plan_number",

    "BORROWER_ASSISTANCE_PLAN":
        "borrower_assistance_plan",

    "HLTV_REFINANCE_OPTION_INDICATOR":
        "hltv_refinance_option_indicator",

    "DEAL_NAME":
        "deal_name",

    "REPURCHASE_MAKE_WHOLE_PROCEEDS_FLAG":
        "repurchase_make_whole_proceeds_flag",

    "ALTERNATIVE_DELINQUENCY_RESOLUTION":
        "alternative_delinquency_resolution",

    "ALTERNATIVE_DELINQUENCY_RESOLUTION_COUNT":
        "alternative_delinquency_resolution_count",

    "TOTAL_DEFERRAL_AMOUNT":
        "total_deferral_amount",

    "PAYMENT_DEFERRAL_MODIFICATION_EVENT_INDICATOR":
        "payment_deferral_modification_event_indicator",

    "INTEREST_BEARING_UPB":
        "interest_bearing_upb",

    # --------------------------------------------------------
    # 111-113
    # --------------------------------------------------------

    "ORIGINATION_CLASSIC_FICO":
        "origination_classic_fico",

    "ISSUANCE_CLASSIC_FICO":
        "issuance_classic_fico",

    "CURRENT_CLASSIC_FICO":
        "current_classic_fico",
}


# ============================================================
# COLUMN RENAMING
# ============================================================

def rename_fannie_columns(df):
    """
    Convert Fannie Mae raw field names
    into stable canonical names.
    """

    return df.rename(
        columns=RENAME_MAP
    )


# ============================================================
# FANNIE DATE PARSING
# ============================================================

def parse_fannie_month_year(series):
    """
    Parse Fannie Mae MMYYYY values.

    Examples
    --------
    22018  -> 2018-02-01
    122018 -> 2018-12-01
    12019  -> 2019-01-01

    Blank/invalid values become NaT.
    """

    # Convert to pandas nullable string.
    values = series.astype("string").str.strip()

    # Remove the textual representation of missing values.
    values = values.replace(
        {
            "": pd.NA,
            "nan": pd.NA,
            "None": pd.NA,
            "<NA>": pd.NA,
        }
    )

    # Handle values that pandas may have read as
    # floating-point numbers, e.g. 22018.0.
    values = values.str.replace(
        r"\.0$",
        "",
        regex=True,
    )

    # Fannie MMYYYY is always six characters.
    values = values.str.zfill(6)

    parsed = pd.to_datetime(
        values,
        format="%m%Y",
        errors="coerce",
    )

    return parsed


def convert_dates(df):
    """
    Convert Fannie Mae MMYYYY date fields
    to pandas datetime.
    """

    df = df.copy()

    for column in MONTH_YEAR_COLUMNS:

        if column in df.columns:

            df[column] = parse_fannie_month_year(
                df[column]
            )

    return df


# ============================================================
# NUMERIC CONVERSION
# ============================================================

def convert_numeric(df):
    """
    Convert numeric Fannie Mae fields
    to numeric dtype.

    Invalid values become NaN.

    Delinquency status is deliberately NOT
    converted here because it is an alphanumeric
    Fannie Mae code.
    """

    df = df.copy()

    for column in NUMERIC_COLUMNS:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )

    return df


# ============================================================
# DELINQUENCY FEATURES
# ============================================================

def create_delinquency_features(df):
    """
    Preserve the original Fannie Mae delinquency code
    and create a numeric delinquency-month feature.

    Examples
    --------
    00 -> 0
    01 -> 1
    02 -> 2
    03 -> 3
    XX -> NaN
    """

    df = df.copy()

    if "delinquency_status" not in df.columns:
        return df

    # Always preserve the original code.
    df["delinquency_status"] = (
        df["delinquency_status"]
        .astype("string")
        .str.strip()
    )

    # Numeric representation used for modeling.
    df["delinquency_months"] = pd.to_numeric(
        df["delinquency_status"],
        errors="coerce",
    )

    return df


# ============================================================
# CREDIT SCORE
# ============================================================

def create_credit_score(df):
    """
    Create an origination credit score feature.

    CSCORE_B = borrower score
    CSCORE_C = co-borrower score

    For two borrowers, use the lower available
    origination score. If only one is available,
    use that score.

    The original borrower/co-borrower fields
    are retained separately.
    """

    df = df.copy()

    borrower = pd.to_numeric(
        df["borrower_credit_score"],
        errors="coerce",
    )

    co_borrower = pd.to_numeric(
        df["co_borrower_credit_score"],
        errors="coerce",
    )

    df["credit_score"] = pd.concat(
        [
            borrower,
            co_borrower,
        ],
        axis=1,
    ).min(
        axis=1,
        skipna=True,
    )

    return df


# ============================================================
# BASIC DATA QUALITY
# ============================================================

def validate_fannie_chunk(df):
    """
    Validate basic structural properties
    of a preprocessed Fannie Mae chunk.
    """

    required_columns = [
        "loan_id",
        "observation_date",
        "delinquency_status",
        "current_upb",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:

        raise ValueError(
            "Missing required Fannie columns: "
            + ", ".join(missing_columns)
        )

    if df["loan_id"].isna().any():

        raise ValueError(
            "Fannie chunk contains missing LOAN_ID values."
        )

    if df["observation_date"].isna().any():

        raise ValueError(
            "Fannie chunk contains invalid ACT_PERIOD values."
        )

    return True

def normalize_string_columns(df):
    """
    Preserve identifier, code and categorical fields
    as strings.

    This prevents numeric-looking codes from being
    interpreted as integers/floats.
    """

    df = df.copy()

    for column in STRING_COLUMNS:

        if column in df.columns:

            df[column] = (
                df[column]
                .astype("string")
                .str.strip()
            )

    return df

# ============================================================
# COMPLETE PREPROCESSING PIPELINE
# ============================================================

def preprocess_fannie_data(df):
    """
    Complete Fannie Mae preprocessing pipeline.

    Pipeline:

        raw Fannie columns
            ↓
        canonical names
            ↓
        date conversion
            ↓
        numeric conversion
            ↓
        delinquency features
            ↓
        credit score
            ↓
        validation
    """

    df = rename_fannie_columns(df)

    df = normalize_string_columns(df)

    df = convert_dates(df)

    df = convert_numeric(df)

    df = create_delinquency_features(df)

    df = create_credit_score(df)

    validate_fannie_chunk(df)

    return df