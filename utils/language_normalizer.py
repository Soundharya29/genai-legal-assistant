import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def normalize_to_english(text):
    try:
        prompt = f"""
        Translate the following legal contract text from Hindi to clear,
        professional English. Preserve legal meaning and structure.
        If the text is already in English, return it unchanged.

        TEXT:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a legal language translator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        # 🔒 Graceful fallback when quota is exceeded
        return text
