from datetime import datetime


class ModelRegistry:

    def __init__(self):
        self.models = []

    def register_model(
        self,
        model_id,
        model_name,
        model_type,
        version,
        owner,
        risk_type,
        status="ACTIVE"
    ):

        model = {
            "model_id": model_id,
            "model_name": model_name,
            "model_type": model_type,
            "version": version,
            "owner": owner,
            "risk_type": risk_type,
            "status": status,
            "registered_at":
                datetime.now().isoformat()
        }

        self.models.append(model)

    def get_models(self):
        return self.models