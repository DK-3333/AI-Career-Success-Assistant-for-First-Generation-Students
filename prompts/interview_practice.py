"""Prompt template for the Interview Practice workflow."""

from prompts.shared import build_system_prompt, format_optional_text


SYSTEM_PROMPT = build_system_prompt("system/interview_practice.txt")


def build_user_prompt(
    target_role: str,
    interview_challenge: str,
    strengths_or_experiences: str,
    preferred_intro_length: str,
) -> str:
    return f"""
Generate interview practice guidance for an early-career college student.

Target role:
{format_optional_text(target_role)}

What feels hardest about interviews right now:
{format_optional_text(interview_challenge)}

Strengths or experiences to highlight:
{format_optional_text(strengths_or_experiences)}

Preferred intro length:
{format_optional_text(preferred_intro_length)}

Instructions:
- Follow the required output format exactly.
- Tailor the questions and coaching to the target role and the student's stated challenge.
- Keep the advice practical, honest, and realistic for an early-career student.
- Do not invent personal stories, achievements, or background details.
- Help the student turn real academic, project, volunteer, or part-time experience into strong interview answers.
- If the preferred intro length is 60 seconds, include a tailored example elevator pitch using only the real information the student provided.
- Do not add any closing offer, extra suggestion line, or conversational ending after the required sections.
""".strip()
