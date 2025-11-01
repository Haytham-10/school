"""Daily life personal coach assistant."""

from __future__ import annotations

from textwrap import dedent

from ..core.client import generate_response
from .base import ModuleResponse


SYSTEM_INSTRUCTION = dedent(
    """
    أنت مساعد شخصي ذكي يدعى "LifeHub Coach". تحدث بلغة عربية ودية، وركز على تنظيم
    يوم المستخدم وفقًا لطاقة الجسم والحالة المزاجية الموصوفة.  قدّم نصائح عملية،
    واقترح فترات راحة، وذكّر بالمهام المهمة.
    """
).strip()


def plan_day(user_prompt: str) -> ModuleResponse:
    """Generate a personalised day plan."""

    prompt = dedent(
        f"""
        المعلومات التالية عن يوم المستخدم:
        {user_prompt}

        أنشئ جدولاً موجزًا للساعات القادمة مع اقتراحات واضحة للمهام، فترات الراحة،
        والتنبيهات التي تعكس الطاقة المتوقعة. استخدم عناوين فرعية ونقاط مرقمة.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="تنظيم اليوم الذكي", body=body)


__all__ = ["plan_day"]
