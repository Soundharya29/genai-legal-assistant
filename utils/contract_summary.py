def generate_contract_summary(
    contract_type,
    overall_risk,
    clauses,
    clause_risks
):
    high_risk_count = clause_risks.count("🔴 High Risk")
    medium_risk_count = clause_risks.count("🟡 Medium Risk")

    summary = f"This is a {contract_type}. "

    if overall_risk == "🔴 High Risk":
        summary += (
            "The contract carries HIGH legal risk and requires careful review. "
        )
    elif overall_risk == "🟡 Medium Risk":
        summary += (
            "The contract has MODERATE legal risk and some clauses may need renegotiation. "
        )
    else:
        summary += (
            "The contract has LOW legal risk and appears generally safe. "
        )

    summary += (
        f"It contains {len(clauses)} clauses, including "
        f"{high_risk_count} high-risk and "
        f"{medium_risk_count} medium-risk clauses. "
    )

    summary += (
        "Business owners should pay special attention to clauses related to "
        "termination, lock-in periods, penalties, and unilateral obligations."
    )

    return summary
