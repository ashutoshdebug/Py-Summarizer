from google import genai
from dotenv import load_dotenv
import os

load_dotenv() # Loading .env variables

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

class AIResponse:
    @staticmethod
    def response(text: str) -> str:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=(
                    "Summarize the following text extracted from a website "
                    "in a concise and clear manner:\n\n"
                    f"{text}"
                )
            )
            return f"\n{response.text}"

        except Exception as e:
            return f"Error generating summary: {e}"