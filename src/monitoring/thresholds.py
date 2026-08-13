def classify_psi(psi):

    if psi < 0.10:
        return "GREEN"

    elif psi < 0.25:
        return "AMBER"

    return "RED"


def recommended_action(status):

    actions = {
        "GREEN":
            "Continue routine monitoring.",

        "AMBER":
            "Investigate deviation and increase monitoring.",

        "RED":
            (
                "Escalate finding, investigate root cause, "
                "and assess recalibration or redevelopment."
            )
    }

    return actions[status]