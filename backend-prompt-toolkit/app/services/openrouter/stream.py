# app/services/openrouter/stream.py
import os
import json
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "meta-llama/llama-3.1-8b-instruct:free"


def stream_chat_completion(messages, model=DEFAULT_MODEL):
    """
    Streams a chat completion from OpenRouter.
    Yields plain text content chunks as they arrive via SSE.
    """
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": os.getenv("APP_URL", "http://localhost:5173"),
        "X-Title": "ChatRouter",
    }

    payload = {
        "model": model,
        "messages": messages,
        "stream": True,
    }

    with requests.post(
        f"{OPENROUTER_BASE_URL}/chat/completions",
        headers=headers,
        json=payload,
        stream=True,
        timeout=60,
    ) as response:
        response.raise_for_status()

        for line in response.iter_lines():
            if not line:
                continue
            decoded = line.decode("utf-8")
            if not decoded.startswith("data: "):
                continue
            data_str = decoded[6:]
            if data_str.strip() == "[DONE]":
                break
            try:
                data = json.loads(data_str)
                delta = data["choices"][0]["delta"]
                content = delta.get("content", "")
                if content:
                    yield content
            except (json.JSONDecodeError, KeyError, IndexError):
                continue
