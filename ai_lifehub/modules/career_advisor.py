"""Career and skill development advisor."""

from __future__ import annotations

from textwrap import dedent

from ..core.client import generate_response
from .base import ModuleResponse

SYSTEM_INSTRUCTION = dedent(
    """
    أنت خبير تطوير مهني في AI LifeHub. قدّم نصائح عملية باللغة العربية الواضحة،
    واستشهد بمصادر التعلّم الرقمية عندما يكون ذلك ممكنًا. ركّز على تطوير المهارات،
    تحسين ملفات السيرة الذاتية، وتوجيه المستخدم نحو فرص مهنية.
    """
).strip()


def craft_cv(prompt_details: str) -> ModuleResponse:
    """Produce CV enhancement suggestions."""

    prompt = dedent(
        f"""
        التفاصيل الخاصة بالسيرة الذاتية الحالية أو المسودة:
        {prompt_details}

        عدّل النص واقترح بنية احترافية، ثم قدّم نقاط قوة قابلة للقياس يمكن إضافتها.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="تحسين السيرة الذاتية", body=body)


def recommend_learning_path(profile: str) -> ModuleResponse:
    """Suggest personalised learning paths."""

    prompt = dedent(
        f"""
        ملف المستخدم المهني ومستوى خبرته:
        {profile}

        اقترح دورات عربية وعالمية، مشاريع عملية، وخطة زمنية للتعلّم بحد أقصى 3 أشهر
        لكل مرحلة. ركّز على المهارات الناعمة والتقنية.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="خارطة تطوير المهارات", body=body)


__all__ = ["craft_cv", "recommend_learning_path"]
