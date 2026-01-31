import json
import os
from datetime import datetime

AUDIT_DIR = "audit_logs"
os.makedirs(AUDIT_DIR, exist_ok=True)

AUDIT_FILE = os.path.join(AUDIT_DIR, "audit_log.json")


def log_audit_event(
    filename,
    contract_type,
    overall_risk,
    clause_count
):
    event = {
        "timestamp": datetime.now().isoformat(),
        "file_name": filename,
        "contract_type": contract_type,
        "overall_risk": overall_risk,
        "total_clauses": clause_count
    }

    if os.path.exists(AUDIT_FILE):
        with open(AUDIT_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(event)

    with open(AUDIT_FILE, "w") as f:
        json.dump(data, f, indent=4)
