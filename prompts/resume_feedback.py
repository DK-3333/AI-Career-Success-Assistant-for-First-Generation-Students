"""Prompt template for the Resume Feedback workflow."""

from prompts.shared import build_system_prompt, format_optional_text


SYSTEM_PROMPT = build_system_prompt("system/resume_feedback.txt")


def build_user_prompt(
    resume_text: str,
    target_role: str,
    feedback_focus: str,
    job_description: str,
) -> str:
    return f"""
Review the following resume content for a first-generation or early-career college student.

Selected feedback focus:
{format_optional_text(feedback_focus)}

Target internship or job title:
{format_optional_text(target_role)}

Resume bullets or experience summary:
{format_optional_text(resume_text)}

Target job description:
{format_optional_text(job_description)}

Instructions:
- Follow the required output format exactly.
- Tailor the depth and emphasis to the selected feedback focus.
- Be encouraging, practical, specific, and non-judgmental.
- Be honest about gaps while still showing the student how to improve.
- Do not fabricate experience, credentials, achievements, or results.
""".strip()
