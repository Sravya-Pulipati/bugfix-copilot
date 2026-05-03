from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def analyze_error_with_ai(error_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Analyze this error:
                    {error_text}

                    Give:
                    1. Root cause
                    2. Module
                    3. Fix
                    """
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI temporarily unavailable. Error: {str(e)}"