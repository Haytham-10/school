"""Shared helpers for the LifeHub domain modules."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ModuleResponse:
    """Standardised response returned by each module."""

    title: str
    body: str
    follow_up: str | None = None

    def as_markdown(self) -> str:
        """Render the response as Markdown for CLI display."""

        follow_up_block = f"\n\n**نصيحة إضافية:** {self.follow_up}" if self.follow_up else ""
        return f"## {self.title}\n\n{self.body}{follow_up_block}"


__all__ = ["ModuleResponse"]
