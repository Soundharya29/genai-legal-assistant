import re

def extract_entities(text):
    entities = {
        "Parties": [],
        "Dates": [],
        "Amounts": [],
        "Jurisdiction / Governing Law": [],
        "Termination": [],
        "Confidentiality / NDA": [],
        "IP Ownership": [],
        "Non-Compete": []
    }

    # -----------------------------
    # Parties (simple heuristic)
    # -----------------------------
    party_patterns = [
        r"employee",
        r"employer",
        r"company",
        r"vendor",
        r"client",
        r"service provider"
    ]

    for p in party_patterns:
        if re.search(p, text, re.IGNORECASE):
            entities["Parties"].append(p.title())

    # -----------------------------
    # Dates
    # -----------------------------
    date_patterns = [
        r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}",
        r"\b\d{1,2}(st|nd|rd|th)?\s+[A-Za-z]+\s+\d{4}\b",
        r"\b\d+\s+(days|months|years)\b"
    ]

    for pattern in date_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        entities["Dates"].extend(matches)

    # -----------------------------
    # Amounts
    # -----------------------------
    amount_patterns = [
        r"₹\s?\d+(?:,\d+)*(?:\.\d+)?",
        r"Rs\.?\s?\d+(?:,\d+)*(?:\.\d+)?",
        r"\b\d+\s?(rupees|INR)\b"
    ]

    for pattern in amount_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        entities["Amounts"].extend(matches)

    # -----------------------------
    # Jurisdiction / Governing Law
    # -----------------------------
    if re.search(r"governing law|jurisdiction|courts of", text, re.IGNORECASE):
        entities["Jurisdiction / Governing Law"].append("Jurisdiction clause detected")

    # -----------------------------
    # Termination
    # -----------------------------
    if re.search(r"terminate|termination|notice period", text, re.IGNORECASE):
        entities["Termination"].append("Termination clause detected")

    # -----------------------------
    # Confidentiality / NDA
    # -----------------------------
    if re.search(r"confidential|non-disclosure|nda", text, re.IGNORECASE):
        entities["Confidentiality / NDA"].append("Confidentiality clause detected")

    # -----------------------------
    # IP Ownership
    # -----------------------------
    if re.search(r"intellectual property|ip rights|ownership of work", text, re.IGNORECASE):
        entities["IP Ownership"].append("IP ownership clause detected")

    # -----------------------------
    # Non-Compete
    # -----------------------------
    if re.search(r"non-compete|restrict.*employment|competition", text, re.IGNORECASE):
        entities["Non-Compete"].append("Non-compete clause detected")

    return entities
