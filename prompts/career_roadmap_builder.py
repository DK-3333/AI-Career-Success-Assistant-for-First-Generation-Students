"""Prompt template for the Career Roadmap Builder workflow."""

from prompts.shared import build_system_prompt, format_list, format_optional_text


SYSTEM_PROMPT = build_system_prompt("system/career_roadmap_builder.txt")


def build_user_prompt(
    long_term_goal: str,
    support_needs: list[str],
    next_6_to_12_month_goal: str,
    current_skills: str,
    confidence_level: int,
) -> str:
    return f"""
Build a 30/60/90-day career roadmap for a first-generation or early-career college student.

Long-term career goal:
{format_optional_text(long_term_goal)}

Support areas selected:
{format_list(support_needs)}

What the student hopes to achieve in the next 6-12 months:
{format_optional_text(next_6_to_12_month_goal)}

Current skills:
{format_optional_text(current_skills)}

Confidence level about career path right now:
{confidence_level}/10

Instructions:
- Follow the required output format exactly.
- Tailor the roadmap to the selected support needs and the student's confidence level.
- Keep the plan realistic, structured, and encouraging.
- Prioritize high-impact actions over busywork.
- Be honest and helpful without bias.
""".strip()
