import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class LLMClient:
    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        client: Any = None,
    ) -> None:
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-5-mini")

        if client is not None:
            self.client = client
            return

        resolved_api_key = api_key or os.getenv("OPENAI_API_KEY")

        if not resolved_api_key:
            raise ValueError("OPENAI_API_KEY não configurada.")

        self.client = OpenAI(api_key=resolved_api_key)

    def generate_response(self, prompt: str) -> str:
        if not prompt or not prompt.strip():
            raise ValueError("O prompt não pode ser vazio.")

        response = self.client.responses.create(
            model=self.model,
            input=prompt.strip(),
        )

        return response.output_text.strip()