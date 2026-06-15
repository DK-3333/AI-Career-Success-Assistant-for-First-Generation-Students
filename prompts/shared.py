"""Shared prompt utilities and coach persona for all workflows."""

from typing import Iterable

from utils.prompt_loader import load_prompt


BASE_SYSTEM_PROMPT = load_prompt("system/base_system.txt")
SHARED_CONTEXT_BLOCK = load_prompt("system/shared_context.txt")


def build_system_prompt(feature_prompt_path: str) -> str:
    feature_instructions = load_prompt(feature_prompt_path)
    return (
        f"{BASE_SYSTEM_PROMPT}\n\n"
        f"Shared app context:\n{SHARED_CONTEXT_BLOCK}\n\n"
        f"{feature_instructions}"
    )


def format_list(items: Iterable[str]) -> str:
    values = [item for item in items if item]
    return ", ".join(values) if values else "None provided"


def format_optional_text(value: str) -> str:
    cleaned = value.strip()
    return cleaned if cleaned else "Not provided"
