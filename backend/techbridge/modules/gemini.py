import google.generativeai as genai
from django.conf import settings
import json

genai.configure(api_key=settings.GEMINI_API_KEY)


def generate_module_content(topic, difficulty):
    prompt = f"""
    Create a {difficulty} level learning module on "{topic}"

    Rules:
    - Step-by-step explanation
    - Examples
    - Clear headings
    - Plain text
    """

    model = genai.GenerativeModel("gemini-pro")
    return model.generate_content(prompt).text


def generate_test(topic, difficulty):
    prompt = f"""
    Create 5 MCQ questions on "{topic}" at {difficulty} level.

    Output STRICT JSON:
    [
      {{
        "id": 1,
        "question": "",
        "options": {{
          "A": "",
          "B": "",
          "C": "",
          "D": ""
        }},
        "correct_answer": "A"
      }}
    ]
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return json.loads(response.text)
