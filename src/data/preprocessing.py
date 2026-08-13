df["credit_score"] = (
    df[
        [
            "CSCORE_B",
            "CSCORE_C"
        ]
    ]
    .min(axis=1)
)