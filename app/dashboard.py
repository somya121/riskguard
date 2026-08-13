import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="RiskGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

OUTPUT_DIR = (
    BASE_DIR
    / "data"
    / "outputs"
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def load_csv(filename):
    """
    Load a CSV file from data/outputs.

    Returns:
        DataFrame if file exists
        None otherwise
    """

    file_path = OUTPUT_DIR / filename

    if file_path.exists():
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            st.error(
                f"Could not read {filename}: {e}"
            )
            return None

    return None


def format_number(value):
    """
    Format large numerical values.
    """

    try:
        return f"{float(value):,.2f}"
    except Exception:
        return "N/A"


def format_percentage(value):
    """
    Convert decimal to percentage.
    """

    try:
        return f"{float(value):.2%}"
    except Exception:
        return "N/A"


# ============================================================
# LOAD OUTPUT DATA
# ============================================================

validation_metrics = load_csv(
    "validation_metrics.csv"
)

calibration_results = load_csv(
    "calibration_results.csv"
)

psi_results = load_csv(
    "psi_results.csv"
)

stress_results = load_csv(
    "stress_results.csv"
)

sensitivity_results = load_csv(
    "sensitivity_results.csv"
)

expected_loss = load_csv(
    "expected_loss_predictions.csv"
)

portfolio_summary = load_csv(
    "portfolio_risk_summary.csv"
)

findings = load_csv(
    "findings.csv"
)

model_registry = load_csv(
    "model_registry.csv"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title(
    "🛡️ RiskGuard"
)

st.sidebar.markdown(
    """
### Model Risk Management

**Credit Risk Model Validation & Monitoring**

---

**Model**

Retail Probability of Default

**Framework**

Basel / IFRS 9

**Model Type**

Credit Risk

**Version**

1.0
"""
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
RiskGuard performs independent monitoring
of credit-risk models using:

• Discrimination analysis  
• Calibration analysis  
• Stability / PSI  
• Stress testing  
• Sensitivity analysis  
• Expected Loss  
• Model risk findings  
• Governance tracking
"""
)


# ============================================================
# HEADER
# ============================================================

st.title(
    "🛡️ RiskGuard"
)

st.subheader(
    "Credit Risk Model Validation & Monitoring Platform"
)

st.markdown(
    """
RiskGuard provides an independent model risk management
framework for monitoring the performance, stability,
robustness and governance of credit-risk models.
"""
)

st.markdown("---")


# ============================================================
# SECTION 1 — MODEL OVERVIEW
# ============================================================

st.header(
    "1. Model Overview"
)

overview_col1, overview_col2, overview_col3, overview_col4 = (
    st.columns(4)
)

with overview_col1:

    st.metric(
        "Model",
        "Retail PD"
    )

with overview_col2:

    st.metric(
        "Model Type",
        "Logistic Regression"
    )

with overview_col3:

    st.metric(
        "Risk Type",
        "Credit Risk"
    )

with overview_col4:

    st.metric(
        "Version",
        "1.0"
    )


# ============================================================
# SECTION 2 — MODEL PERFORMANCE
# ============================================================

st.header(
    "2. Model Performance"
)

if validation_metrics is not None:

    # Convert metric/value table into dictionary

    if (
        "metric" in validation_metrics.columns
        and "value" in validation_metrics.columns
    ):

        metric_dict = dict(
            zip(
                validation_metrics["metric"],
                validation_metrics["value"]
            )
        )

        col1, col2, col3, col4 = (
            st.columns(4)
        )

        # ----------------------------------------------------
        # AUC
        # ----------------------------------------------------

        with col1:

            auc_value = metric_dict.get(
                "AUC",
                None
            )

            if auc_value is not None:

                st.metric(
                    "AUC",
                    f"{float(auc_value):.3f}"
                )

            else:

                st.metric(
                    "AUC",
                    "N/A"
                )

        # ----------------------------------------------------
        # KS
        # ----------------------------------------------------

        with col2:

            ks_value = metric_dict.get(
                "KS",
                None
            )

            if ks_value is not None:

                st.metric(
                    "KS",
                    f"{float(ks_value):.3f}"
                )

            else:

                st.metric(
                    "KS",
                    "N/A"
                )

        # ----------------------------------------------------
        # GINI
        # ----------------------------------------------------

        with col3:

            gini_value = metric_dict.get(
                "Gini",
                None
            )

            if gini_value is not None:

                st.metric(
                    "Gini",
                    f"{float(gini_value):.3f}"
                )

            else:

                st.metric(
                    "Gini",
                    "N/A"
                )

        # ----------------------------------------------------
        # ACCURACY RATIO
        # ----------------------------------------------------

        with col4:

            ar_value = metric_dict.get(
                "Accuracy Ratio",
                None
            )

            if ar_value is not None:

                st.metric(
                    "Accuracy Ratio",
                    f"{float(ar_value):.3f}"
                )

            else:

                st.metric(
                    "Accuracy Ratio",
                    "N/A"
                )

        st.subheader(
            "Validation Metrics"
        )

        st.dataframe(
            validation_metrics,
            use_container_width=True
        )

    else:

        st.warning(
            "validation_metrics.csv does not "
            "contain the expected metric/value columns."
        )

else:

    st.warning(
        "Validation metrics are not available yet. "
        "Run the model validation notebook first."
    )


# ============================================================
# SECTION 3 — CALIBRATION
# ============================================================

st.header(
    "3. Calibration Analysis"
)

st.markdown(
    """
Calibration evaluates whether predicted probabilities
are consistent with realized default rates.
"""
)

if calibration_results is not None:

    st.dataframe(
        calibration_results,
        use_container_width=True
    )

    # --------------------------------------------------------
    # Calibration error
    # --------------------------------------------------------

    if (
        "predicted_pd" in calibration_results.columns
        and
        "realized_default_rate"
        in calibration_results.columns
    ):

        st.subheader(
            "Predicted PD vs Realized Default Rate"
        )

        chart_data = calibration_results[
            [
                "predicted_pd",
                "realized_default_rate"
            ]
        ].copy()

        chart_data.columns = [
            "Predicted PD",
            "Realized Default Rate"
        ]

        st.line_chart(
            chart_data
        )

    # --------------------------------------------------------
    # Maximum calibration error
    # --------------------------------------------------------

    if (
        "calibration_error"
        in calibration_results.columns
    ):

        max_error = (
            calibration_results[
                "calibration_error"
            ]
            .abs()
            .max()
        )

        st.metric(
            "Maximum Absolute Calibration Error",
            f"{max_error:.2%}"
        )

        if max_error <= 0.03:

            st.success(
                "Calibration is within the "
                "defined monitoring threshold."
            )

        else:

            st.error(
                "Calibration threshold breached. "
                "Model investigation is required."
            )

else:

    st.warning(
        "Calibration results are not available yet."
    )


# ============================================================
# SECTION 4 — STABILITY / PSI
# ============================================================

st.header(
    "4. Population Stability Monitoring"
)

st.markdown(
    """
Population Stability Index (PSI) is used to identify
material changes in the distribution of model inputs
between the baseline population and the OOT population.
"""
)

if psi_results is not None:

    st.dataframe(
        psi_results,
        use_container_width=True
    )

    # --------------------------------------------------------
    # PSI chart
    # --------------------------------------------------------

    if (
        "variable" in psi_results.columns
        and "psi" in psi_results.columns
    ):

        st.subheader(
            "PSI by Variable"
        )

        psi_chart = (
            psi_results
            .set_index("variable")[
                ["psi"]
            ]
        )

        st.bar_chart(
            psi_chart
        )

    # --------------------------------------------------------
    # Count status
    # --------------------------------------------------------

    if "status" in psi_results.columns:

        green_count = (
            psi_results["status"]
            .astype(str)
            .str.upper()
            .eq("GREEN")
            .sum()
        )

        amber_count = (
            psi_results["status"]
            .astype(str)
            .str.upper()
            .eq("AMBER")
            .sum()
        )

        red_count = (
            psi_results["status"]
            .astype(str)
            .str.upper()
            .eq("RED")
            .sum()
        )

        col1, col2, col3 = (
            st.columns(3)
        )

        with col1:

            st.metric(
                "GREEN",
                green_count
            )

        with col2:

            st.metric(
                "AMBER",
                amber_count
            )

        with col3:

            st.metric(
                "RED",
                red_count
            )

else:

    st.warning(
        "PSI results are not available yet."
    )


# ============================================================
# SECTION 5 — STRESS TESTING
# ============================================================

st.header(
    "5. Stress Testing"
)

st.markdown(
    """
Stress testing evaluates the sensitivity of the credit
portfolio to adverse macroeconomic conditions.
"""
)

if stress_results is not None:

    st.dataframe(
        stress_results,
        use_container_width=True
    )

    # --------------------------------------------------------
    # Stress chart
    # --------------------------------------------------------

    if (
        "scenario" in stress_results.columns
        and "stressed_pd" in stress_results.columns
    ):

        st.subheader(
            "PD Under Stress Scenarios"
        )

        stress_chart = (
            stress_results
            .set_index("scenario")[
                ["stressed_pd"]
            ]
        )

        st.bar_chart(
            stress_chart
        )

else:

    st.warning(
        "Stress-testing results are not available yet."
    )


# ============================================================
# SECTION 6 — SENSITIVITY ANALYSIS
# ============================================================

st.header(
    "6. Sensitivity Analysis"
)

st.markdown(
    """
Sensitivity analysis evaluates how model outputs respond
to changes in key economic or portfolio variables.
"""
)

if sensitivity_results is not None:

    st.dataframe(
        sensitivity_results,
        use_container_width=True
    )

    # --------------------------------------------------------
    # Try to identify useful numerical columns
    # --------------------------------------------------------

    numeric_columns = (
        sensitivity_results
        .select_dtypes(
            include="number"
        )
        .columns
        .tolist()
    )

    if len(numeric_columns) >= 2:

        st.subheader(
            "Sensitivity Results"
        )

        st.line_chart(
            sensitivity_results[
                numeric_columns
            ]
        )

else:

    st.warning(
        "Sensitivity-analysis results are not available yet."
    )


# ============================================================
# SECTION 7 — CREDIT RISK PORTFOLIO
# ============================================================

st.header(
    "7. Credit Risk Portfolio"
)

if portfolio_summary is not None:

    if (
        "Metric" in portfolio_summary.columns
        and "Value" in portfolio_summary.columns
    ):

        summary_dict = dict(
            zip(
                portfolio_summary["Metric"],
                portfolio_summary["Value"]
            )
        )

        # ----------------------------------------------------
        # Portfolio metrics
        # ----------------------------------------------------

        col1, col2, col3 = (
            st.columns(3)
        )

        # Number of exposures

        with col1:

            value = summary_dict.get(
                "Number of Exposures"
            )

            if value is not None:

                st.metric(
                    "Exposures",
                    f"{int(float(value)):,}"
                )

            else:

                st.metric(
                    "Exposures",
                    "N/A"
                )

        # Average PD

        with col2:

            value = summary_dict.get(
                "Average PD"
            )

            if value is not None:

                st.metric(
                    "Average PD",
                    f"{float(value):.2%}"
                )

            else:

                st.metric(
                    "Average PD",
                    "N/A"
                )

        # Average LGD

        with col3:

            value = summary_dict.get(
                "Average LGD"
            )

            if value is not None:

                st.metric(
                    "Average LGD",
                    f"{float(value):.2%}"
                )

            else:

                st.metric(
                    "Average LGD",
                    "N/A"
                )

        # ----------------------------------------------------
        # EAD / Expected Loss
        # ----------------------------------------------------

        col1, col2 = (
            st.columns(2)
        )

        with col1:

            value = summary_dict.get(
                "Total EAD"
            )

            if value is not None:

                st.metric(
                    "Total EAD",
                    f"{float(value):,.2f}"
                )

            else:

                st.metric(
                    "Total EAD",
                    "N/A"
                )

        with col2:

            value = summary_dict.get(
                "Total Expected Loss"
            )

            if value is not None:

                st.metric(
                    "Total Expected Loss",
                    f"{float(value):,.2f}"
                )

            else:

                st.metric(
                    "Total Expected Loss",
                    "N/A"
                )

        # ----------------------------------------------------
        # Expected Loss / EAD
        # ----------------------------------------------------

        value = summary_dict.get(
            "Expected Loss / EAD"
        )

        if value is not None:

            st.metric(
                "Expected Loss / EAD",
                f"{float(value):.2%}"
            )

else:

    st.warning(
        "Portfolio risk summary is not available yet."
    )


# ============================================================
# SECTION 8 — EXPOSURE LEVEL RISK
# ============================================================

st.subheader(
    "Exposure-Level Risk"
)

if expected_loss is not None:

    st.dataframe(
        expected_loss.head(100),
        use_container_width=True
    )

    # --------------------------------------------------------
    # Expected loss distribution
    # --------------------------------------------------------

    if "expected_loss" in expected_loss.columns:

        st.subheader(
            "Expected Loss Distribution"
        )

        st.bar_chart(
            expected_loss[
                ["expected_loss"]
            ].head(50)
        )

else:

    st.warning(
        "Expected-loss predictions are not available yet."
    )


# ============================================================
# SECTION 9 — MODEL RISK FINDINGS
# ============================================================

st.header(
    "8. Model Risk Findings"
)

st.markdown(
    """
Findings represent breaches, weaknesses or concerns
identified during independent model validation and monitoring.
"""
)

if findings is not None:

    st.dataframe(
        findings,
        use_container_width=True
    )

    # --------------------------------------------------------
    # Finding statistics
    # --------------------------------------------------------

    if "severity" in findings.columns:

        severity_counts = (
            findings[
                "severity"
            ]
            .value_counts()
        )

        st.subheader(
            "Findings by Severity"
        )

        st.bar_chart(
            severity_counts
        )

    if "status" in findings.columns:

        open_findings = (
            findings[
                "status"
            ]
            .astype(str)
            .str.upper()
            .isin([
                "OPEN",
                "UNDER INVESTIGATION",
                "ACTION DEFINED"
            ])
            .sum()
        )

        closed_findings = (
            findings[
                "status"
            ]
            .astype(str)
            .str.upper()
            .eq("CLOSED")
            .sum()
        )

        col1, col2 = (
            st.columns(2)
        )

        with col1:

            st.metric(
                "Open / Active Findings",
                open_findings
            )

        with col2:

            st.metric(
                "Closed Findings",
                closed_findings
            )

else:

    st.info(
        "No model-risk findings have been generated yet."
    )


# ============================================================
# SECTION 10 — MODEL REGISTRY
# ============================================================

st.header(
    "9. Model Registry"
)

st.markdown(
    """
The model registry provides governance information for
models within the credit-risk framework.
"""
)

if model_registry is not None:

    st.dataframe(
        model_registry,
        use_container_width=True
    )

else:

    st.warning(
        "Model registry is not available yet."
    )


# ============================================================
# SECTION 11 — GOVERNANCE FRAMEWORK
# ============================================================

st.header(
    "10. Model Risk Governance"
)

governance_col1, governance_col2 = (
    st.columns(2)
)

with governance_col1:

    st.subheader(
        "Validation Lifecycle"
    )

    st.markdown(
        """
    **1. Model Development**

    ↓

    **2. Independent Validation**

    ↓

    **3. Performance Assessment**

    ↓

    **4. Stability Monitoring**

    ↓

    **5. Stress Testing**

    ↓

    **6. Findings & Remediation**

    ↓

    **7. Revalidation**
    """
    )


with governance_col2:

    st.subheader(
        "Monitoring Framework"
    )

    st.markdown(
        """
    **Discrimination**

    AUC / KS / Gini

    **Calibration**

    Predicted vs realized defaults

    **Stability**

    PSI / population drift

    **Robustness**

    Sensitivity / stress testing

    **Governance**

    Findings / corrective actions
    """
    )


# ============================================================
# SECTION 12 — VALIDATION REPORT
# ============================================================

st.header(
    "11. Validation Report"
)

report_path = (
    OUTPUT_DIR
    / "RiskGuard_Validation_Report.pdf"
)

if report_path.exists():

    st.success(
        "Validation report is available."
    )

    with open(
        report_path,
        "rb"
    ) as file:

        st.download_button(
            label=(
                "📄 Download Validation Report"
            ),
            data=file,
            file_name=(
                "RiskGuard_Validation_Report.pdf"
            ),
            mime="application/pdf"
        )

else:

    st.warning(
        "Validation report has not been generated yet."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    """
RiskGuard | Credit Risk Model Validation &
Model Risk Management Framework

PD • LGD • EAD • Expected Loss •
Calibration • Stability • Stress Testing •
Sensitivity • Governance
"""
)