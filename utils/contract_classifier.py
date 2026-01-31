def classify_contract(text):
    text = text.lower()

    if "employment" in text or "employee" in text:
        return "Employment Contract"
    elif "vendor" in text or "supplier" in text:
        return "Vendor Agreement"
    elif "lease" in text or "rent" in text:
        return "Lease Agreement"
    elif "partnership" in text or "partner" in text:
        return "Partnership Deed"
    elif "service" in text:
        return "Service Agreement"
    else:
        return "General Contract"
