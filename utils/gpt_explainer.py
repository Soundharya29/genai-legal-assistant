import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_clause(clause_text):
    prompt = f"""
Explain the following contract clause in simple business English.
Avoid legal jargon.

Clause:
{clause_text}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        # Graceful fallback (quota / network / billing issues)
        return (
            "This clause describes a condition or responsibility within the contract. "
            "It explains what one party is required to do or is restricted from doing. "
            "Such clauses should be reviewed carefully to ensure they are fair and do not "
            "create unnecessary legal or financial risks."
        )
