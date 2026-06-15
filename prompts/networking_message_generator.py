"""Prompt template for the Networking Message Generator workflow."""

from prompts.shared import build_system_prompt, format_optional_text


SYSTEM_PROMPT = build_system_prompt("system/networking_message_generator.txt")


def build_user_prompt(
    contact_type: str,
    shared_context: str,
    goal: str,
    preferred_tone: str,
    student_background: str,
) -> str:
    return f"""
Draft networking outreach materials for a first-generation college student.

Who the student is reaching out to:
{format_optional_text(contact_type)}

Shared connection or context:
{format_optional_text(shared_context)}

Networking goal:
{format_optional_text(goal)}

Preferred tone:
{format_optional_text(preferred_tone)}

Student background:
{format_optional_text(student_background)}

Instructions:
- Follow the required output format exactly.
- Tailor the messaging to the selected contact type, goal, and tone.
- Keep the outreach warm, clear, respectful, and realistic.
- Do not sound desperate.
- Do not overstate the student's background or experience.
- Be honest and helpful without bias.
""".strip()
