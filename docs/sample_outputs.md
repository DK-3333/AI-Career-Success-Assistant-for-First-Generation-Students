# Sample Testing Profiles and Expected Outputs

This document supports Phase 8 testing for the Streamlit app:
`AI Career Success Assistant for First-Generation Students`.

The test cases below are based on the exact input fields currently used in
app.py. The goal is to validate that each service produces relevant, structured, and
supportive outputs for realistic first-generation and early-career student use
cases.

## Student Personas

### Persona 1
First-generation business student targeting a Business Analyst internship.

### Persona 2
Computer Science student targeting a Software Engineering internship.

### Persona 3
Information Management graduate student targeting Analytics Engineer new grad
full-time roles.

## Test Cases

### Test Case 1
**Persona name:** Persona 1, First-generation business student targeting a Business Analyst internship

**Service being tested:** Resume Feedback

**Exact app input fields and sample values:**
- `Target internship or job title`: `Business Analyst Intern`
- `Resume bullets or experience summary`:
  `Analyzed survey responses from 120 student club members using Excel to identify top event preferences.`
  `Worked 20 hours per week in campus dining while training 3 new student employees on register and customer service processes.`
  `Built a class project presentation comparing pricing strategies for three retail brands and presented recommendations to 25 students.`
- `Target job description`:
  `Looking for a Business Analyst Intern with strong Excel skills, attention to detail, problem-solving ability, and experience communicating insights to stakeholders. Familiarity with dashboards, data analysis, and cross-functional teamwork is preferred.`
- `Feedback focus`: `Overall improvement`

**Expected AI response type:**
- A balanced resume review with a clear overall impression.
- Strengths tied to analysis, communication, and work ethic.
- Improvement ideas around specificity, business language, and stronger outcomes.
- Missing keywords such as stakeholder communication, dashboarding, and data analysis.
- Revised bullet suggestions and ATS alignment guidance.
- Three practical next steps.

**What to check during manual testing:**
- The response follows the required resume structure.
- The feedback matches the selected focus of `Overall improvement`.
- Suggested rewrites do not invent metrics or experience.
- The advice feels relevant for a first-generation business student, not generic corporate jargon.

**Why this test supports the project mission:**
It validates that the app can help a student translate everyday academic and work
experience into stronger internship-ready resume language.

### Test Case 2
**Persona name:** Persona 1, First-generation business student targeting a Business Analyst internship

**Service being tested:** Networking Message Generator

**Exact app input fields and sample values:**
- `Who are you reaching out to?`: `Alumnus or alumna`
- `What is your goal?`: `Informational interview`
- `Shared connection or context`: `We both attend the University of Illinois and I saw you studied business analytics.`
- `Preferred tone`: `Warm and professional`
- `Student background`:
  `I am a first-generation junior majoring in business administration and I am exploring Business Analyst internships. I am especially interested in how professionals use data to support strategy decisions.`

**Expected AI response type:**
- A short LinkedIn note under 300 characters.
- A polished short email version.
- A respectful follow-up message for 5 to 7 days later.
- Two tips for personalization without overstating experience.

**What to check during manual testing:**
- The LinkedIn version is concise enough for a connection request.
- The email version sounds professional and not desperate.
- The follow-up message is polite and low-pressure.
- The output reflects the selected audience, goal, and tone.

**Why this test supports the project mission:**
It checks whether the app helps first-generation students build professional
network confidence with realistic, respectful outreach language.

### Test Case 3
**Persona name:** Persona 2, Computer Science student targeting a Software Engineering internship

**Service being tested:** Interview Practice

**Exact app input fields and sample values:**
- `Target role`: `Software Engineering Intern`
- `Strengths or experiences to highlight`:
  `Built a full-stack course project using React, Flask, and SQLite.`
  `Solved 180 LeetCode problems and improved in data structures coursework.`
  `Worked as a peer tutor for introductory Python and helped students debug assignments.`
- `What feels hardest about interviews right now?`:
  `I struggle to explain my projects clearly and I worry that I do not have enough internship experience.`
- `Preferred intro length`: `60 seconds`

**Expected AI response type:**
- Five likely software engineering interview questions.
- Clear reasoning for why each question matters.
- Suggested answer structures that use projects, tutoring, and coursework.
- STAR guidance where appropriate.
- One practice tip per question.
- A tailored example 60-second elevator pitch based on the student's real background.

**What to check during manual testing:**
- The interview questions are relevant to software engineering internships.
- The answer guidance works for a student without prior formal internship experience.
- The 60-second pitch is actually included.
- The pitch uses only the provided background and does not invent technologies, internships, or achievements.

**Why this test supports the project mission:**
It validates that the app can build interview confidence for students whose most
relevant experience comes from coursework, projects, and peer support roles.

### Test Case 4
**Persona name:** Persona 2, Computer Science student targeting a Software Engineering internship

**Service being tested:** Job Search Guidance

**Exact app input fields and sample values:**
- `Career interest area`: `Software engineering internships in backend or full-stack development`
- `Current stage`: `Junior`
- `Main challenge right now`: `Need a stronger application strategy`
- `Hours per week available for job search`: `10`
- `Anything else the app should know?`:
  `I am the first in my family to pursue a tech internship and I am not always sure how many applications, referrals, and networking steps I should balance each week.`

**Expected AI response type:**
- Best-fit internship titles such as software engineering intern, backend intern, and full-stack intern.
- Search keywords aligned to internship search platforms.
- Suggested organization types such as startups, mid-size tech companies, and university-affiliated programs.
- A weekly strategy that fits a 10-hour schedule.
- Networking advice, skill gaps, and three immediate actions.
  
**What to check during manual testing:**
- The weekly plan scales to the selected `10` hours.
- The advice is specific and structured rather than generic motivation.
- The response avoids guaranteeing interviews or offers.
- The recommended search keywords match the student's stated interest area.

**Why this test supports the project mission:**
It checks whether the app can turn uncertainty into a practical plan for a
first-generation student navigating internship recruiting with limited time.

### Test Case 5
**Persona name:** Persona 3, Information Management graduate student targeting Analytics Engineer new grad full-time roles

**Service being tested:** Career Roadmap Builder

**Exact app input fields and sample values:**
- `Long-term career goal`: `Become an Analytics Engineer working on modern data platforms`
- `What do you hope to achieve in the next 6-12 months?`:
  `Land a full-time Analytics Engineer or data-focused platform role, strengthen my SQL and dbt portfolio, and build confidence explaining technical business impact in interviews.`
- `Current skills`:
  `SQL, Python, Tableau, basic dbt exposure, data cleaning, dashboard creation, stakeholder presentations, and graduate coursework in data management.`
- `What support would help most?`: `Resume help`, `Interview prep`, `Career exploration`
- `How confident do you feel about your career path right now?`: `6`

**Expected AI response type:**
- A realistic 30/60/90-day roadmap summary.
- A weekly learning plan with manageable focus areas.
- Project suggestions related to analytics engineering or data transformation.
- Networking actions and resume or LinkedIn improvements.
- Milestones and a final expected portfolio outcome.

**What to check during manual testing:**
- The roadmap reflects analytics engineering goals rather than generic data advice.
- The plan is actionable and not overwhelming.
- The selected support areas appear in the guidance.
- The milestones feel appropriate for a graduate student with moderate confidence.

**Why this test supports the project mission:**
It validates that the app can support students moving from education into
full-time roles by turning broad goals into structured, confidence-building next
steps.

## Manual Testing Checklist

- App opens locally
- All tabs render correctly
- Required inputs are clear
- Buttons trigger AI response
- Empty input handling works
- Outputs are relevant and structured
- Responsible AI disclaimer is visible
- No API key is exposed
