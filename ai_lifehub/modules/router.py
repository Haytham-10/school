"""Routing utilities for AI LifeHub CLI."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict

from . import career_advisor, health_companion, personal_coach, social_buddy, tech_helper, tutor
from .base import ModuleResponse


@dataclass(slots=True)
class Route:
    """Defines a CLI route."""

    handler: Callable[[str], ModuleResponse]
    description: str


ROUTES: Dict[str, Route] = {
    "coach": Route(personal_coach.plan_day, "تنظيم اليوم الذكي"),
    "cv": Route(career_advisor.craft_cv, "تحسين السيرة الذاتية"),
    "learning": Route(career_advisor.recommend_learning_path, "خارطة تطوير المهارات"),
    "health": Route(health_companion.analyse_wellbeing, "مراجعة الصحة والعافية"),
    "calm": Route(health_companion.calming_mode, "وضع التهدئة الذكي"),
    "reply": Route(social_buddy.suggest_reply, "اقتراحات للردود"),
    "post": Route(social_buddy.craft_post, "منشور اجتماعي"),
    "tech": Route(tech_helper.diagnose_issue, "تشخيص الأعطال التقنية"),
    "explain": Route(tutor.explain_topic, "شرح تعليمي"),
    "quiz": Route(tutor.quiz_student, "اختبار تفاعلي"),
}


def available_routes() -> Dict[str, Route]:
    """Return copy of CLI routes."""

    return dict(ROUTES)


__all__ = ["available_routes", "Route"]
