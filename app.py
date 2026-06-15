import streamlit as st

from prompts.career_roadmap_builder import (
    SYSTEM_PROMPT as CAREER_ROADMAP_SYSTEM_PROMPT,
    build_user_prompt as build_career_roadmap_prompt,
)
from prompts.interview_practice import (
    SYSTEM_PROMPT as INTERVIEW_PRACTICE_SYSTEM_PROMPT,
    build_user_prompt as build_interview_practice_prompt,
)
from prompts.job_search_guidance import (
    SYSTEM_PROMPT as JOB_SEARCH_SYSTEM_PROMPT,
    build_user_prompt as build_job_search_prompt,
)
from prompts.networking_message_generator import (
    SYSTEM_PROMPT as NETWORKING_SYSTEM_PROMPT,
    build_user_prompt as build_networking_prompt,
)
from prompts.resume_feedback import (
    SYSTEM_PROMPT as RESUME_FEEDBACK_SYSTEM_PROMPT,
    build_user_prompt as build_resume_feedback_prompt,
)
from utils.openai_client import generate_ai_response


st.set_page_config(
    page_title="AI Career Success Assistant | First-Generation Students",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


def render_output_placeholder(title: str, default_message: str) -> None:
    st.markdown(f"#### {title}")
    st.container(border=True).markdown(default_message)


def render_ai_response(
    *,
    system_prompt: str,
    user_prompt: str,
    button_label: str,
    button_key: str,
    default_message: str,
) -> None:
    if st.button(button_label, key=button_key, use_container_width=True):
        try:
            with st.spinner("Generating guidance..."):
                response = generate_ai_response(system_prompt, user_prompt)
        except ValueError as exc:
            st.error(str(exc))
            render_output_placeholder("Output", default_message)
        except RuntimeError as exc:
            st.error(str(exc))
            render_output_placeholder("Output", default_message)
        else:
            st.markdown("#### Output")
            st.container(border=True).markdown(response)
    else:
        render_output_placeholder("Output", default_message)


def render_resume_tab() -> None:
    st.subheader("Resume Feedback")
    st.write(
        "Paste your current resume bullets and a target role to receive tailored feedback "
        "for U.S. internships and entry-level jobs."
    )

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        role = st.text_input(
            "Target internship or job title",
            placeholder="Example: Data Analyst Intern",
            key="resume_role",
        )
        resume_text = st.text_area(
            "Resume bullets or experience summary",
            placeholder=(
                "Paste 2-5 resume bullets, leadership experience, projects, or work "
                "experience here."
            ),
            height=220,
            key="resume_text",
        )
    with col2:
        job_description = st.text_area(
            "Target job description",
            placeholder="Paste the internship or job description here.",
            height=220,
            key="resume_job_description",
        )
        focus_area = st.selectbox(
            "Feedback focus",
            ["Overall improvement", "Stronger bullet points", "Keyword alignment"],
            key="resume_focus",
        )

    user_prompt = build_resume_feedback_prompt(
        resume_text=resume_text,
        target_role=role,
        feedback_focus=focus_area,
        job_description=job_description,
    )
    render_ai_response(
        system_prompt=RESUME_FEEDBACK_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        button_label="Generate Resume Feedback",
        button_key="resume_button",
        default_message="Your resume feedback results will appear here after you click the button.",
    )


def render_networking_tab() -> None:
    st.subheader("Networking Message Generator")
    st.write(
        "Draft thoughtful outreach messages that feel warm, professional, and realistic "
        "for first-generation students building their network."
    )

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        contact_type = st.selectbox(
            "Who are you reaching out to?",
            ["Alumnus or alumna", "Recruiter", "Professional in your target field", "Mentor"],
            key="network_contact_type",
        )
        message_goal = st.selectbox(
            "What is your goal?",
            ["Coffee chat request", "Informational interview", "General networking introduction"],
            key="network_goal",
        )
    with col2:
        shared_context = st.text_input(
            "Shared connection or context",
            placeholder="Example: We both attend the University of Illinois",
            key="network_context",
        )
        tone = st.selectbox(
            "Preferred tone",
            ["Warm and professional", "Confident and concise", "Friendly and curious"],
            key="network_tone",
        )

    background = st.text_area(
        "Student background",
        placeholder=(
            "Example: I am a first-generation computer science student interested in "
            "product management and summer internships."
        ),
        height=160,
        key="network_background",
    )

    user_prompt = build_networking_prompt(
        contact_type=contact_type,
        shared_context=shared_context,
        goal=message_goal,
        preferred_tone=tone,
        student_background=background,
    )
    render_ai_response(
        system_prompt=NETWORKING_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        button_label="Draft Networking Message",
        button_key="network_button",
        default_message="Your networking draft will appear here after you click the button.",
    )


def render_interview_tab() -> None:
    st.subheader("Interview Practice")
    st.write(
        "Get realistic practice questions and answer guidance that help you turn school, "
        "projects, and part-time experiences into strong interview stories."
    )

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        target_role = st.text_input(
            "Target role",
            placeholder="Example: Business Analyst Intern",
            key="interview_role",
        )
        strengths = st.text_area(
            "Strengths or experiences to highlight",
            placeholder=(
                "Example: leadership in student orgs, class projects, part-time work, "
                "community service, or research."
            ),
            height=180,
            key="interview_strengths",
        )
    with col2:
        nervous_about = st.text_area(
            "What feels hardest about interviews right now?",
            placeholder=(
                "Example: I do not know how to sound confident without feeling scripted."
            ),
            height=120,
            key="interview_nerves",
        )
        intro_length = st.radio(
            "Preferred intro length",
            ["30 seconds", "60 seconds"],
            horizontal=True,
            key="interview_length",
        )

    user_prompt = build_interview_practice_prompt(
        target_role=target_role,
        interview_challenge=nervous_about,
        strengths_or_experiences=strengths,
        preferred_intro_length=intro_length,
    )
    render_ai_response(
        system_prompt=INTERVIEW_PRACTICE_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        button_label="Generate Interview Practice",
        button_key="interview_button",
        default_message="Your interview practice guidance will appear here after you click the button.",
    )


def render_job_search_tab() -> None:
    st.subheader("Job Search Guidance")
    st.write(
        "Build a more structured job search plan with realistic weekly actions, search "
        "keywords, and suggested roles."
    )

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        interests = st.text_input(
            "Career interest area",
            placeholder="Example: Marketing, software engineering, consulting, public health",
            key="job_interest",
        )
        class_year = st.selectbox(
            "Current stage",
            ["First-year student", "Sophomore", "Junior", "Senior", "Recent graduate"],
            key="job_stage",
        )
    with col2:
        search_challenge = st.selectbox(
            "Main challenge right now",
            [
                "Not sure what roles fit me",
                "Not finding internships",
                "Need a stronger application strategy",
                "Need help staying organized",
            ],
            key="job_challenge",
        )
        weekly_capacity = st.slider(
            "Hours per week available for job search",
            min_value=1,
            max_value=42,
            value=5,
            key="job_capacity",
        )

    additional_context = st.text_area(
        "Anything else the app should know?",
        placeholder="Example: I am the first in my family to pursue a corporate internship.",
        height=140,
        key="job_context",
    )

    user_prompt = build_job_search_prompt(
        career_interest_area=interests,
        main_challenge=search_challenge,
        current_stage=class_year,
        hours_available=weekly_capacity,
        additional_context=additional_context,
    )
    render_ai_response(
        system_prompt=JOB_SEARCH_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        button_label="Create Job Search Guidance",
        button_key="job_button",
        default_message="Your job search guidance will appear here after you click the button.",
    )


def render_roadmap_tab() -> None:
    st.subheader("Career Roadmap Builder")
    st.write(
        "Create a realistic 30/60/90-day roadmap with milestones, networking actions, "
        "and portfolio-building ideas."
    )

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        long_term_goal = st.text_input(
            "Long-term career goal",
            placeholder="Example: Become a product manager in tech",
            key="roadmap_goal",
        )
        next_milestone = st.text_area(
            "What do you hope to achieve in the next 6-12 months?",
            placeholder=(
                "Example: Land my first internship, improve my resume, and build confidence "
                "networking with professionals."
            ),
            height=160,
            key="roadmap_milestone",
        )
        current_skills = st.text_area(
            "Current skills",
            placeholder=(
                "Example: Excel, Python basics, research, teamwork, public speaking, or "
                "student leadership."
            ),
            height=140,
            key="roadmap_skills",
        )
    with col2:
        support_needs = st.multiselect(
            "What support would help most?",
            ["Resume help", "Networking practice", "Interview prep", "Career exploration"],
            key="roadmap_support",
        )
        confidence_level = st.slider(
            "How confident do you feel about your career path right now?",
            min_value=1,
            max_value=10,
            value=5,
            key="roadmap_confidence",
        )

    user_prompt = build_career_roadmap_prompt(
        long_term_goal=long_term_goal,
        support_needs=support_needs,
        next_6_to_12_month_goal=next_milestone,
        current_skills=current_skills,
        confidence_level=confidence_level,
    )
    render_ai_response(
        system_prompt=CAREER_ROADMAP_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        button_label="Build Career Roadmap",
        button_key="roadmap_button",
        default_message="Your career roadmap will appear here after you click the button.",
    )


def main() -> None:
    st.title("AI Career Success Assistant for First-Generation Students 🎓")
    st.markdown(
        """
        A simple, supportive career tool designed to help first-generation students build
        confidence with resumes, networking, interviews, job search strategy, and career planning.
        """
    )

    with st.sidebar:
        st.header("Project Purpose")
        st.write(
            "This project is inspired by the goal of helping promising students build "
            "skills, networks, confidence, and career momentum."
        )
        st.markdown(
            """
            **What this app is designed to support**
            - Resume improvement
            - Networking outreach
            - Interview preparation
            - Job search planning
            - Career roadmap thinking
            """
        )
        st.caption(
            "Add your OpenAI API key in `.env` to generate tailored guidance in each tab."
        )

    st.markdown("---")

    tabs = st.tabs(
        [
            "Resume Feedback",
            "Networking Message Generator",
            "Interview Practice",
            "Job Search Guidance",
            "Career Roadmap Builder",
        ]
    )

    with tabs[0]:
        render_resume_tab()
    with tabs[1]:
        render_networking_tab()
    with tabs[2]:
        render_interview_tab()
    with tabs[3]:
        render_job_search_tab()
    with tabs[4]:
        render_roadmap_tab()

    st.markdown("---")
    st.caption(
        "Responsible use: This assistant provides career preparation guidance, but it does "
        "not guarantee employment outcomes. Users should review, personalize, and verify all "
        "AI-generated content before using it in real career decisions, applications, or outreach."
    )

    st.caption(
        """
        <p style="text-align: center; margin-top: -0.5rem; color: #4b5563;">
            ✨ Built by Dhyey K. © 2026
        </p>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
