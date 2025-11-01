"""Health and wellness companion."""

from __future__ import annotations

from textwrap import dedent

from ..core.client import generate_response
from .base import ModuleResponse

SYSTEM_INSTRUCTION = dedent(
    """
    أنت خبير صحة وعافية رقمي ضمن AI LifeHub. تقدّم توجيهات عامة لا تغني عن زيارة
    الطبيب، وتراعي الجوانب النفسية والبدنية للمستخدم. عند الإشارة إلى حالات طبية
    خطيرة، انصح بالتواصل مع مختص.
    """
).strip()


def analyse_wellbeing(inputs: str) -> ModuleResponse:
    """Generate wellbeing guidance from user reflections."""

    prompt = dedent(
        f"""
        بيانات المستخدم عن النوم، المزاج، النشاط البدني، أو أي أعراض:
        {inputs}

        حلّل الحالة وقدّم نصائح تغذية، نشاط، وتمارين تنفّس، ثم اختم بجملة تذكير أن
        النصائح لا تغني عن الاستشارة الطبية.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="مراجعة الصحة والعافية", body=body)


def calming_mode(trigger: str) -> ModuleResponse:
    """Provide a calming ritual when stress is detected."""

    prompt = dedent(
        f"""
        حالة التوتر أو القلق الموصوفة:
        {trigger}

        أنشئ بروتوكول تهدئة من ثلاث مراحل: موسيقى أو صوت مقترح، تمرين تنفّس، وجملة
        دعم نفسي. استخدم لغة مطمئنة.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="وضع التهدئة الذكي", body=body)


__all__ = ["analyse_wellbeing", "calming_mode"]
