"""Gemini client wrapper used by AI LifeHub modules."""

from __future__ import annotations

import logging
from functools import lru_cache
from typing import Any

import google.generativeai as genai

from .config import GeminiSettings, load_gemini_settings

LOGGER = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def _configure_client(settings: GeminiSettings | None = None) -> genai.GenerativeModel:
    """Configure and memoise the Gemini SDK model instance."""

    settings = settings or load_gemini_settings()
    genai.configure(api_key=settings.api_key)
    generation_config: dict[str, Any] = {
        "temperature": settings.temperature,
        "top_p": settings.top_p,
    }
    if settings.top_k is not None:
        generation_config["top_k"] = settings.top_k

    LOGGER.debug("Configured Gemini model %s", settings.model)
    return genai.GenerativeModel(settings.model, generation_config=generation_config)


def generate_response(prompt: str, *, system_instruction: str | None = None) -> str:
    """Generate a text response for the provided prompt."""

    model = _configure_client()
    full_prompt = prompt
    if system_instruction:
        full_prompt = f"{system_instruction}\n\n{prompt}"

    LOGGER.debug("Sending prompt to Gemini: %s", prompt)
    result = model.generate_content(full_prompt)
    if not result.candidates:
        return ""

    return result.text.strip()


__all__ = ["generate_response"]
