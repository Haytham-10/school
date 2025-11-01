"""Social communication helper."""

from __future__ import annotations

from textwrap import dedent

from ..core.client import generate_response
from .base import ModuleResponse

SYSTEM_INSTRUCTION = dedent(
    """
    أنت مرشد تواصل اجتماعي ضمن AI LifeHub. حافظ على اللباقة، وراعي اختلاف اللهجات،
    وقدّم اقتراحات باللغة العربية الفصيحة مع إمكانية إضافة لمسة ودودة عند الحاجة.
    """
).strip()


def suggest_reply(context: str) -> ModuleResponse:
    """Create a polite reply suggestion."""

    prompt = dedent(
        f"""
        سياق الرسالة أو المحادثة:
        {context}

        اقترح ثلاث صيغ ردود بدرجات رسمية مختلفة، واذكر سبب كل اقتراح بإيجاز.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="اقتراحات للردود", body=body)


def craft_post(idea: str) -> ModuleResponse:
    """Generate a social media post."""

    prompt = dedent(
        f"""
        الفكرة أو المناسبة:
        {idea}

        اكتب منشورًا جذابًا، ثم اقترح وسوماً ووسيطًا بصريًا (صورة أو فيديو قصير) يمكن
        تصميمه بسرعة.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="منشور اجتماعي مقترح", body=body)


__all__ = ["suggest_reply", "craft_post"]
