import google.generativeai as genai
import json
import os

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash-lite"
)


def extract_data(image_bytes):

    prompt = """
Analyze this answer sheet.

Return ONLY valid JSON.

{
  "registration_no":"",
  "roll_no":"",
  "student_name":"",
  "branch":"",
  "section":"",
  "course_code":"",

  "q1a":0,
  "q1b":0,
  "q1c":0,

  "q2a":0,
  "q2b":0,
  "q2c":0,

  "q3a":0,
  "q3b":0,
  "q3c":0,

  "q1_total":0,
  "q2_total":0,
  "q3_total":0,

  "grand_total":0
}
"""

    response = model.generate_content([
        prompt,
        {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }
    ])

    text = response.text

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)