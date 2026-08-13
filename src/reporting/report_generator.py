from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_validation_report(
    output_path,
    model_name,
    model_version,
    validation_metrics,
    stress_results,
    findings
):

    document = SimpleDocTemplate(
        output_path,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    story = []

    # Title

    story.append(
        Paragraph(
            "RiskGuard Model Validation Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # Model information

    story.append(
        Paragraph(
            f"Model: {model_name}",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Version: {model_version}",
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # Executive summary

    story.append(
        Paragraph(
            "1. Executive Summary",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "RiskGuard provides an independent "
            "validation and monitoring assessment "
            "of the selected credit-risk model.",
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 15)
    )

    # Discrimination

    story.append(
        Paragraph(
            "2. Discriminatory Power",
            styles["Heading2"]
        )
    )

    metric_data = [
        ["Metric", "Value"]
    ]

    for metric, value in (
        validation_metrics.items()
    ):

        metric_data.append([
            metric,
            f"{value:.4f}"
        ])

    metric_table = Table(
        metric_data
    )

    metric_table.setStyle(
        TableStyle([
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.black
            ),
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.grey
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            )
        ])
    )

    story.append(
        metric_table
    )

    story.append(
        Spacer(1, 20)
    )

    # Stress testing

    story.append(
        Paragraph(
            "3. Stress Testing",
            styles["Heading2"]
        )
    )

    stress_data = [
        [
            "Scenario",
            "Baseline PD",
            "Stressed PD",
            "Change"
        ]
    ]

    for _, row in stress_results.iterrows():

        stress_data.append([
            row["scenario"],
            f"{row['baseline_pd']:.4%}",
            f"{row['stressed_pd']:.4%}",
            f"{row['pd_change']:.4%}"
        ])

    stress_table = Table(
        stress_data
    )

    stress_table.setStyle(
        TableStyle([
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.black
            )
        ])
    )

    story.append(
        stress_table
    )

    story.append(
        Spacer(1, 20)
    )

    # Findings

    story.append(
        Paragraph(
            "4. Model Risk Findings",
            styles["Heading2"]
        )
    )

    for finding in findings:

        story.append(
            Paragraph(
                (
                    f"{finding['finding_id']} — "
                    f"{finding['severity']}"
                ),
                styles["Heading3"]
            )
        )

        story.append(
            Paragraph(
                finding["description"],
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                (
                    "Recommendation: "
                    + finding["recommendation"]
                ),
                styles["Normal"]
            )
        )

        story.append(
            Spacer(1, 10)
        )

    # Conclusion

    story.append(
        Paragraph(
            "5. Validation Conclusion",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "The model should remain subject to "
            "ongoing performance, calibration and "
            "stability monitoring. Any material "
            "threshold breaches should be investigated "
            "through the model risk governance process.",
            styles["Normal"]
        )
    )

    document.build(story)