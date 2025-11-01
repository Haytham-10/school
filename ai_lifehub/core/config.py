"""Configuration helpers for AI LifeHub.

This module centralizes runtime configuration for the application, notably how
we load sensitive values such as API keys.  The design keeps secrets out of the
source code while still making it easy to run the demo locally.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


DEFAULT_MODEL_NAME = "gemini-2.0-flash-exp"


@dataclass
class GeminiSettings:
    """Holds configuration required to talk to the Gemini API."""

    api_key: str
    model: str = DEFAULT_MODEL_NAME
    temperature: float = 0.6
    top_p: float = 0.8
    top_k: int | None = None


def load_gemini_settings() -> GeminiSettings:
    """Load Gemini settings from environment variables.

    The function prioritises explicit environment variables and raises a clear
    error when mandatory values are missing.  This keeps the rest of the code
    clean and focused on product logic.
    """

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Environment variable GOOGLE_API_KEY is required to use the Gemini API."
        )

    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL_NAME)
    temperature = float(os.getenv("GEMINI_TEMPERATURE", 0.6))
    top_p = float(os.getenv("GEMINI_TOP_P", 0.8))
    top_k_str = os.getenv("GEMINI_TOP_K")
    top_k = int(top_k_str) if top_k_str else None

    return GeminiSettings(
        api_key=api_key,
        model=model,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
    )


__all__ = ["GeminiSettings", "load_gemini_settings", "DEFAULT_MODEL_NAME"]
