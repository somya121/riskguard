from datetime import datetime


class FindingManager:

    def __init__(self):
        self.findings = []

    def create_finding(
        self,
        finding_id,
        model_id,
        finding_type,
        severity,
        metric,
        observed_value,
        threshold,
        description,
        recommendation
    ):

        finding = {
            "finding_id": finding_id,
            "model_id": model_id,
            "finding_type": finding_type,
            "severity": severity,
            "metric": metric,
            "observed_value":
                observed_value,
            "threshold":
                threshold,
            "description":
                description,
            "recommendation":
                recommendation,
            "status": "OPEN",
            "created_at":
                datetime.now().isoformat()
        }

        self.findings.append(
            finding
        )

    def get_findings(self):
        return self.findings

    def update_status(
        self,
        finding_id,
        new_status
    ):

        for finding in self.findings:

            if (
                finding["finding_id"]
                == finding_id
            ):
                finding["status"] = (
                    new_status
                )