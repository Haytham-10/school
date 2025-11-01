"""Educational tutor module."""

from __future__ import annotations

from textwrap import dedent

from ..core.client import generate_response
from .base import ModuleResponse

SYSTEM_INSTRUCTION = dedent(
    """
    أنت معلم تفاعلي في AI LifeHub. اشرح المفاهيم بوضوح بالعربية أو الإنجليزية بناءً على
    طلب المستخدم، وقدّم أمثلة وتمارين قصيرة. التزم بتدرّج تعليمي لطيف وشجع المتعلم.
    """
).strip()


def explain_topic(topic_request: str) -> ModuleResponse:
    """Explain a topic for a student."""

    prompt = dedent(
        f"""
        طلب الطالب:
        {topic_request}

        قدم شرحًا موجزًا، مثالاً عمليًا، ثم تمرينًا ذاتيًا مع الحل المقترح.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="شرح تعليمي", body=body)


def quiz_student(topic_request: str) -> ModuleResponse:
    """Create a short interactive quiz."""

    prompt = dedent(
        f"""
        موضوع الطالب ومستواه:
        {topic_request}

        أنشئ اختبارًا من ثلاث أسئلة متعددة الخيارات مع الإجابة الصحيحة وشرح موجز لكل
        إجابة.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="اختبار تفاعلي", body=body)


__all__ = ["explain_topic", "quiz_student"]
