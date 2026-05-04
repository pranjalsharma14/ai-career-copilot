import streamlit as st
from openai import OpenAI
import time

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Career Copilot Pro",
    page_icon="🚀",
    layout="wide"
)

# =========================
# LOADING FUNCTION
# =========================
def ai_thinking():
    with st.spinner("🧠 AI is thinking..."):
        time.sleep(1)

# =========================
# SIMPLE LOGIN SYSTEM
# =========================
USERS = {
    "pranjal": "1234",
    "admin": "admin123"
}

def login():
    st.title("🔐 AI Career Copilot Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success("Login successful 🚀")
            st.rerun()
        else:
            st.error("Invalid credentials")

def logout():
    st.sidebar.button("🚪 Logout", on_click=do_logout)

def do_logout():
    st.session_state["logged_in"] = False
    st.session_state["user"] = None
    st.rerun()

# session init
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

# =========================
# UI STYLING
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    font-family: 'Segoe UI';
}

/* LABELS */
label {
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* INPUT BOX */
input, textarea {
    background: rgba(255,255,255,0.92) !important;
    border: 1px solid rgba(0,0,0,0.15) !important;
    color: #111827 !important;
    border-radius: 12px !important;
    padding: 10px;
}

input::placeholder, textarea::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

input, textarea {
    caret-color: #111827 !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: rgba(10, 15, 30, 0.85);
    backdrop-filter: blur(20px);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* BUTTONS */
.stButton>button {
    background: linear-gradient(135deg, #06b6d4, #3b82f6);
    color: white !important;
    border-radius: 12px;
    padding: 0.6em 1.5em;
    font-weight: 700;
    box-shadow: 0 10px 25px rgba(59,130,246,0.4);
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 15px 35px rgba(56,189,248,0.5);
}

/* HEADINGS */
h1, h2, h3 {
    color: white !important;
}

/* =========================
   DASHBOARD CARDS
========================= */
.dashboard-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 18px;
    border-radius: 16px;
    margin-bottom: 15px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    transition: 0.3s;
}

.dashboard-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 40px rgba(56,189,248,0.2);
}

/* =========================
   🔥 FIX OUTPUT VISIBILITY (ADDED ONLY)
========================= */
.stMarkdown, .stMarkdown p, .stMarkdown span {
    color: #ffffff !important;
}

div[data-testid="stMarkdownContainer"] {
    color: #ffffff !important;
}

.stSuccess, .stAlert {
    color: #ffffff !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("🚀 AI Career Copilot PRO")
st.markdown("### 🔥 Resume • ATS • Interview • Career Roadmap AI Assistant")

# =========================
# API KEY
# =========================
api_key = st.text_input("🔑 Enter OpenRouter API Key", type="password")

if api_key:

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    # =========================
    # SIDEBAR
    # =========================
    st.sidebar.markdown("## ⚡ FEATURES")
    logout()

    menu = st.sidebar.radio(
        "Choose Module",
        [
            "🧾 Resume Generator",
            "📊 ATS Analyzer",
            "🎤 Interview Prep",
            "🧭 Career Roadmap"
        ]
    )

    # =========================
    # INPUTS
    # =========================
    st.markdown("## 👤 Candidate Profile")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        skills = st.text_area("Skills")

    with col2:
        education = st.text_area("Education")
        job_role = st.text_input("Target Job Role")

    projects = st.text_area("Projects")

    # =========================
    # RESUME
    # =========================
    if menu == "🧾 Resume Generator":

        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("### 🧾 Resume Generator AI")

        if st.button("✨ Generate Resume"):

            ai_thinking()

            prompt = f"""
            Create ATS resume:

            Name: {name}
            Skills: {skills}
            Education: {education}
            Projects: {projects}
            Role: {job_role}
            """

            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            st.success("Resume Generated 🚀")
            st.markdown(response.choices[0].message.content)

        st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # ATS
    # =========================
    elif menu == "📊 ATS Analyzer":

        job_desc = st.text_area("Job Description")

        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("### 📊 ATS Analyzer AI")

        if st.button("Analyze ATS"):

            ai_thinking()

            prompt = f"""
            ATS Analysis:

            Candidate:
            {name}, {skills}, {education}, {projects}

            Job:
            {job_desc}
            """

            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            st.success("Done ✅")
            st.markdown(response.choices[0].message.content)

        st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # INTERVIEW
    # =========================
    elif menu == "🎤 Interview Prep":

        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("### 🎤 Interview Prep AI")

        if st.button("Generate Questions"):

            ai_thinking()

            prompt = f"""
            Interview Questions for {job_role}
            Skills: {skills}
            """

            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            st.success("Ready 🎯")
            st.markdown(response.choices[0].message.content)

        st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # ROADMAP
    # =========================
    elif menu == "🧭 Career Roadmap":

        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("### 🧭 Career Roadmap AI")

        if st.button("Generate Roadmap"):

            ai_thinking()

            prompt = f"""
            Career roadmap for {job_role}
            Skills: {skills}
            """

            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            st.success("Roadmap Ready 🚀")
            st.markdown(response.choices[0].message.content)

        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.warning("⚠️ Enter API Key to continue")
