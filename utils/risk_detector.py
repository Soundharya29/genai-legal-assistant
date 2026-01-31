import re

def detect_risks(clause_text):
    clause_text = clause_text.lower()
    risks = []

    if "penalty" in clause_text or "fine" in clause_text:
        risks.append("Penalty clause")

    if "indemnify" in clause_text or "indemnity" in clause_text:
        risks.append("Indemnity clause")

    if "terminate" in clause_text and "employee" in clause_text:
        risks.append("Unilateral termination")

    if "lock-in" in clause_text or "lock in" in clause_text:
        risks.append("Lock-in period")

    if "arbitration" in clause_text:
        risks.append("Arbitration clause")

    if "non-compete" in clause_text or "non compete" in clause_text:
        risks.append("Non-compete restriction")

    return risks


def risk_level(risks):
    if not risks:
        return "🟢 Low Risk"
    if len(risks) == 1:
        return "🟡 Medium Risk"
    return "🔴 High Risk"


def explain_risk(risks):
    explanations = []

    for risk in risks:
        if risk == "Penalty clause":
            explanations.append(
                "This clause may impose financial penalties which can increase business risk."
            )

        elif risk == "Indemnity clause":
            explanations.append(
                "This clause may require one party to cover losses of the other, increasing liability exposure."
            )

        elif risk == "Unilateral termination":
            explanations.append(
                "This allows one party to terminate the contract without equal rights for the other."
            )

        elif risk == "Lock-in period":
            explanations.append(
                "This restricts exit options and binds one party for a fixed duration."
            )

        elif risk == "Arbitration clause":
            explanations.append(
                "This may force dispute resolution through arbitration, limiting court access."
            )

        elif risk == "Non-compete restriction":
            explanations.append(
                "This may restrict future business or employment opportunities."
            )

    return explanations


def suggest_alternatives(risks):
    suggestions = []

    for risk in risks:
        if risk == "Unilateral termination":
            suggestions.append(
                "Allow termination with equal notice period for both parties."
            )

        elif risk == "Lock-in period":
            suggestions.append(
                "Reduce the lock-in duration or allow early exit with reasonable notice."
            )

        elif risk == "Penalty clause":
            suggestions.append(
                "Replace penalties with proportional damages or dispute resolution mechanisms."
            )

        elif risk == "Indemnity clause":
            suggestions.append(
                "Limit indemnity to direct losses and exclude indirect damages."
            )

        elif risk == "Non-compete restriction":
            suggestions.append(
                "Restrict non-compete scope to reasonable duration and geography."
            )

    return suggestions


def contract_risk_score(all_clause_risks):
    if "🔴 High Risk" in all_clause_risks:
        return "🔴 High Risk"
    elif "🟡 Medium Risk" in all_clause_risks:
        return "🟡 Medium Risk"
    else:
        return "🟢 Low Risk"