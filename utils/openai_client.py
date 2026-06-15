import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def generate_ai_response(system_prompt: str, user_input: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to your .env file before using AI features."
        )

    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

    try:
        response = client.responses.create(
            model=model,
            instructions=system_prompt,
            input=user_input,
        )
    except Exception as exc:
        raise RuntimeError(
            "The OpenAI request failed. Please check your API key, model name, and network access."
        ) from exc

    output_text = response.output_text.strip()
    if not output_text:
        raise RuntimeError("The model returned an empty response. Please try again.")

    return output_text
