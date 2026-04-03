import os

from dotenv import load_dotenv
from openai import OpenAI

from prompts import build_prompt


load_dotenv()

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4")


def get_explanation(topic: str) -> str:
    """Generate a three-part explanation for an engineering topic."""
    cleaned_topic = topic.strip()
    if not cleaned_topic:
        raise ValueError("Please provide a topic to explain.")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Add it to your .env file before running the app."
        )

    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.create(
            model=DEFAULT_MODEL,
            input=build_prompt(cleaned_topic),
        )
    except Exception as exc:
        raise RuntimeError(f"OpenAI request failed: {exc}") from exc

    explanation = (response.output_text or "").strip()
    if not explanation:
        raise RuntimeError(
            "The model returned an empty explanation. Please try again."
        )

    return explanation
