import re

def split_into_clauses(text):
    """
    Splits contract text into clauses using numbering and headings.
    """
    if not text:
        return []

    # Normalize spacing
    text = re.sub(r'\n+', '\n', text)

    # Split on common clause patterns
    pattern = r'\n(?=\d+\.|\d+\)|Clause\s+\d+|SECTION\s+\d+)'
    parts = re.split(pattern, text, flags=re.IGNORECASE)

    clauses = []
    for part in parts:
        cleaned = part.strip()
        if len(cleaned) > 30:  # ignore tiny fragments
            clauses.append(cleaned)

    return clauses
import re

def split_into_subclauses(clause):
    """
    Splits a clause into sub-clauses like (a), (b), 1.1, 1.2
    """
    subclauses = re.split(r'\(\w\)|\d+\.\d+', clause)
    subclauses = [s.strip() for s in subclauses if s.strip()]
    return subclauses
