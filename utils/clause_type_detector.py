def detect_clause_type(text):
    text_lower = text.lower()

    if any(word in text_lower for word in ["shall not", "must not", "may not", "prohibited"]):
        return "⚠️ Prohibition"

    if any(word in text_lower for word in ["shall", "must", "is required to", "are required to"]):
        return "🔴 Obligation"

    if any(word in text_lower for word in ["may", "is entitled to", "has the right to"]):
        return "🟢 Right"

    return "ℹ️ Neutral"
