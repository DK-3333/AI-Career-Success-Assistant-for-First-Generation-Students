"""Prompt template for the Job Search Guidance workflow."""

from prompts.shared import build_system_prompt, format_optional_text


SYSTEM_PROMPT = build_system_prompt("system/job_search_guidance.txt")


def build_user_prompt(
    career_interest_area: str,
    main_challenge: str,
    current_stage: str,
    hours_available: int,
    additional_context: str,
) -> str:
    return f"""
Create job search guidance for a first-generation or early-career college student.

Career interest area:
{format_optional_text(career_interest_area)}

Main challenge right now:
{format_optional_text(main_challenge)}

Current stage:
{format_optional_text(current_stage)}

Hours available per week for job search:
{hours_available}

Additional context:
{format_optional_text(additional_context)}

Instructions:
- Follow the required output format exactly.
- Tailor the advice to the student's current stage, challenge, and available time.
- Keep the guidance realistic, structured, and practical.
- Encourage applications, networking, and skill-building without making guarantees.
- Be honest and helpful without bias.
""".strip()
