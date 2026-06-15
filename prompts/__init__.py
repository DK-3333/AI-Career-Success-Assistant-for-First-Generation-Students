"""Prompt templates for each app workflow."""

from .career_roadmap_builder import SYSTEM_PROMPT as CAREER_ROADMAP_SYSTEM_PROMPT
from .interview_practice import SYSTEM_PROMPT as INTERVIEW_PRACTICE_SYSTEM_PROMPT
from .job_search_guidance import SYSTEM_PROMPT as JOB_SEARCH_SYSTEM_PROMPT
from .networking_message_generator import SYSTEM_PROMPT as NETWORKING_SYSTEM_PROMPT
from .resume_feedback import SYSTEM_PROMPT as RESUME_FEEDBACK_SYSTEM_PROMPT

__all__ = [
    "CAREER_ROADMAP_SYSTEM_PROMPT",
    "INTERVIEW_PRACTICE_SYSTEM_PROMPT",
    "JOB_SEARCH_SYSTEM_PROMPT",
    "NETWORKING_SYSTEM_PROMPT",
    "RESUME_FEEDBACK_SYSTEM_PROMPT",
]
