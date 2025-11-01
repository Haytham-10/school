"""Technical troubleshooting assistant."""

from __future__ import annotations

from textwrap import dedent

from ..core.client import generate_response
from .base import ModuleResponse

SYSTEM_INSTRUCTION = dedent(
    """
    أنت خبير دعم تقني في AI LifeHub. حلّل المشاكل التقنية للأجهزة، الشبكات، أو السيارات
    اعتمادًا على الوصف النصي. عندما تكون هناك حاجة لفحص فعلي، وجّه المستخدم إلى مركز
    صيانة معتمد أو قدّم خطوات فحص آمنة.
    """
).strip()


def diagnose_issue(description: str) -> ModuleResponse:
    """Diagnose a technical issue from a description."""

    prompt = dedent(
        f"""
        وصف العطل:
        {description}

        حلّل السبب المحتمل، اقترح خطوات بسيطة للتشخيص الذاتي، ثم اقترح حلاً عمليًا أو
        أوصِ بزيارة مركز صيانة. أختم بقائمة أدوات أو قطع قد تكون مطلوبة.
        """
    ).strip()

    body = generate_response(prompt, system_instruction=SYSTEM_INSTRUCTION)
    return ModuleResponse(title="تشخيص الأعطال التقنية", body=body)


__all__ = ["diagnose_issue"]
