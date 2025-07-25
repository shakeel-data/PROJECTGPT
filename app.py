<<<<<<< HEAD
# # Streamlit frontend

import streamlit as st
import os
from datetime import datetime
from pathlib import Path

# ------------------- Branding --------------------
st.set_page_config(page_title="ProjectGPT", page_icon="🤖", layout="wide")

# ------------------- Sidebar ---------------------
st.sidebar.image("https://avatars.githubusercontent.com/u/139295202?s=200&v=4", width=80)
st.sidebar.title("🌟 ProjectGPT")
st.sidebar.markdown("Generate real-world projects for Data, AI, and Tech.")
selected_tab = st.sidebar.radio("Go to", ["🏠 Home", "⚙️ Generate Project", "📚 About", "📞 Contact"])

# ------------------- Content ---------------------
if selected_tab == "🏠 Home":
    st.title("Welcome to ProjectGPT 👋")
    st.markdown("""
        🚀 **ProjectGPT** is your one-stop platform to generate hands-on projects in:
        - Python, Machine Learning, SQL, Power BI, Tableau, Excel, Cloud
        - Across domains like Finance, Healthcare, Retail, Sports, and more
        
        ✨ From **mini-projects to final year**, get everything:
        - Dataset
        - Source Code
        - Project Report
        - GitHub README
        - Video & UI scripts

        👉 Go to "⚙️ Generate Project" tab to start now!
    """)

elif selected_tab == "⚙️ Generate Project":
    st.header("⚙️ Generate a Custom Project")

    col1, col2, col3 = st.columns(3)

    with col1:
        field = st.selectbox("📌 Select Field", [
            "Python", "Java", "JavaScript", "C++", "C#", "C Language",
            "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
            "AI", "SQL", "Power BI", "Excel", "Tableau", "Cloud"
        ])

    with col2:
        level = st.selectbox("🎯 Select Level", ["Beginner", "Intermediate", "Advanced", "Resume/Job"])

    with col3:
        domain = st.selectbox("🌐 Select Domain", [
            "Finance", "Health", "Sports", "Education", "Retail",
            "Social Media", "E-Commerce", "HR", "Entertainment"
        ])

    format = st.multiselect("🧰 Choose Project Type/Format", [
        "Jupyter Notebook", "Python Script", "Dashboard (Tableau)",
        "Dashboard (Power BI)", "Dashboard (Excel)", "Web App", "Chatbot"
    ])

    extras = st.multiselect("➕ Extras to Include", [
        "Dataset", "Source Code", "Project Report", "GitHub README",
        "Video Tutorial Script", "Voiceover Script", "UI Mockup"
    ])

    if st.button("🚀 Generate Project"):
        st.success("✅ Project generated!")

        title = f"{field}-based {domain} Project for {level} Level"
        summary = f"This project focuses on using {field} tools and techniques to solve real-world problems in the {domain} domain, suitable for a {level} level learner."
        tasks = f"1. Define the problem scope in {domain}\n2. Collect or generate synthetic dataset\n3. Implement core {field} logic\n4. Visualize results\n5. Document the work\n6. Prepare deliverables"

        dataset_link = "https://www.kaggle.com/datasets"
        fake_code = f"# Example {field} code\nprint('Hello from ProjectGPT')"
        readme = f"# {title}\n\n## Overview\n{summary}\n\n## Tools\n- {field}\n\n## Steps\n{tasks}"
        report = f"## Project Report\n\n### Title\n{title}\n\n### Summary\n{summary}\n\n### Domain: {domain}\n### Level: {level}\n\n### Tasks\n{tasks}"
        video_script = f"🎥 Welcome to the {field}-based project in {domain}! In this tutorial, we’ll cover how to use {field} to solve problems in {domain} using a hands-on approach."
        voiceover_script = f"🗣️ This project was generated using ProjectGPT for the {domain} domain at a {level} difficulty level. The tools used include {field}, and the output is a complete hands-on solution."
        ui_mockup = f"UI: [Home] ➝ [Select Field: {field}] ➝ [Level: {level}] ➝ [Domain: {domain}] ➝ [Format: {', '.join(format)}] ➝ [Extras: {', '.join(extras)}] ➝ [Generate]"

        # --- Display Content ---
        st.markdown(f"### 📌 Title\n{title}")
        st.markdown(f"### ✍️ Summary\n{summary}")
        st.markdown(f"### 🧪 Tasks\n{tasks}")

        if "Dataset" in extras:
            st.markdown(f"### 📂 Dataset\nSample dataset from [Kaggle]({dataset_link})")

        if "Source Code" in extras:
            st.markdown(f"### 💻 Sample Code\n```{field.lower()}\n{fake_code}\n```")

        if "GitHub README" in extras:
            st.markdown(f"### 📄 README.md\n```\n{readme}\n```")

        if "Project Report" in extras:
            st.markdown(f"### 🧾 Report\n```\n{report}\n```")

        if "Video Tutorial Script" in extras:
            st.markdown(f"### 🎬 Video Script\n```\n{video_script}\n```")

        if "Voiceover Script" in extras:
            st.markdown(f"### 🎤 Voiceover Script\n```\n{voiceover_script}\n```")

        if "UI Mockup" in extras:
            st.markdown(f"### 🖼️ UI Mockup Description\n```\n{ui_mockup}\n```")

elif selected_tab == "📚 About":
    st.title("📚 About ProjectGPT")
    st.markdown("""
    ProjectGPT is a startup initiative to bridge the gap between learning and doing.
    Our platform lets students, job seekers, and professionals auto-generate full-stack or analytical projects with just a few clicks.

    🚧 MVP built using Python + Streamlit + GPT  
    📈 Vision: Grow into a SaaS platform for personalized AI project generation  
    💡 Built with ❤️ by Shakeel Ahamed
    """)

elif selected_tab == "📞 Contact":
    st.title("📞 Contact & Feedback")
    st.markdown("""
    🔗 Connect on [LinkedIn](https://linkedin.com/in/shakeel-data)  
    📬 Email: shakeelahamed6618@gmail.com  
    💬 WhatsApp: +91 94442 33768
=======
# # Streamlit frontend

import streamlit as st
import os
from datetime import datetime
from pathlib import Path

# ------------------- Branding --------------------
st.set_page_config(page_title="ProjectGPT", page_icon="🤖", layout="wide")

# ------------------- Sidebar ---------------------
st.sidebar.image("https://avatars.githubusercontent.com/u/139295202?s=200&v=4", width=80)
st.sidebar.title("🌟 ProjectGPT")
st.sidebar.markdown("Generate real-world projects for Data, AI, and Tech.")
selected_tab = st.sidebar.radio("Go to", ["🏠 Home", "⚙️ Generate Project", "📚 About", "📞 Contact"])

# ------------------- Content ---------------------
if selected_tab == "🏠 Home":
    st.title("Welcome to ProjectGPT 👋")
    st.markdown("""
        🚀 **ProjectGPT** is your one-stop platform to generate hands-on projects in:
        - Python, Machine Learning, SQL, Power BI, Tableau, Excel, Cloud
        - Across domains like Finance, Healthcare, Retail, Sports, and more
        
        ✨ From **mini-projects to final year**, get everything:
        - Dataset
        - Source Code
        - Project Report
        - GitHub README
        - Video & UI scripts

        👉 Go to "⚙️ Generate Project" tab to start now!
    """)

elif selected_tab == "⚙️ Generate Project":
    st.header("⚙️ Generate a Custom Project")

    col1, col2, col3 = st.columns(3)

    with col1:
        field = st.selectbox("📌 Select Field", [
            "Python", "Java", "JavaScript", "C++", "C#", "C Language",
            "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
            "AI", "SQL", "Power BI", "Excel", "Tableau", "Cloud"
        ])

    with col2:
        level = st.selectbox("🎯 Select Level", ["Beginner", "Intermediate", "Advanced", "Resume/Job"])

    with col3:
        domain = st.selectbox("🌐 Select Domain", [
            "Finance", "Health", "Sports", "Education", "Retail",
            "Social Media", "E-Commerce", "HR", "Entertainment"
        ])

    format = st.multiselect("🧰 Choose Project Type/Format", [
        "Jupyter Notebook", "Python Script", "Dashboard (Tableau)",
        "Dashboard (Power BI)", "Dashboard (Excel)", "Web App", "Chatbot"
    ])

    extras = st.multiselect("➕ Extras to Include", [
        "Dataset", "Source Code", "Project Report", "GitHub README",
        "Video Tutorial Script", "Voiceover Script", "UI Mockup"
    ])

    if st.button("🚀 Generate Project"):
        st.success("✅ Project generated!")

        title = f"{field}-based {domain} Project for {level} Level"
        summary = f"This project focuses on using {field} tools and techniques to solve real-world problems in the {domain} domain, suitable for a {level} level learner."
        tasks = f"1. Define the problem scope in {domain}\n2. Collect or generate synthetic dataset\n3. Implement core {field} logic\n4. Visualize results\n5. Document the work\n6. Prepare deliverables"

        dataset_link = "https://www.kaggle.com/datasets"
        fake_code = f"# Example {field} code\nprint('Hello from ProjectGPT')"
        readme = f"# {title}\n\n## Overview\n{summary}\n\n## Tools\n- {field}\n\n## Steps\n{tasks}"
        report = f"## Project Report\n\n### Title\n{title}\n\n### Summary\n{summary}\n\n### Domain: {domain}\n### Level: {level}\n\n### Tasks\n{tasks}"
        video_script = f"🎥 Welcome to the {field}-based project in {domain}! In this tutorial, we’ll cover how to use {field} to solve problems in {domain} using a hands-on approach."
        voiceover_script = f"🗣️ This project was generated using ProjectGPT for the {domain} domain at a {level} difficulty level. The tools used include {field}, and the output is a complete hands-on solution."
        ui_mockup = f"UI: [Home] ➝ [Select Field: {field}] ➝ [Level: {level}] ➝ [Domain: {domain}] ➝ [Format: {', '.join(format)}] ➝ [Extras: {', '.join(extras)}] ➝ [Generate]"

        # --- Display Content ---
        st.markdown(f"### 📌 Title\n{title}")
        st.markdown(f"### ✍️ Summary\n{summary}")
        st.markdown(f"### 🧪 Tasks\n{tasks}")

        if "Dataset" in extras:
            st.markdown(f"### 📂 Dataset\nSample dataset from [Kaggle]({dataset_link})")

        if "Source Code" in extras:
            st.markdown(f"### 💻 Sample Code\n```{field.lower()}\n{fake_code}\n```")

        if "GitHub README" in extras:
            st.markdown(f"### 📄 README.md\n```\n{readme}\n```")

        if "Project Report" in extras:
            st.markdown(f"### 🧾 Report\n```\n{report}\n```")

        if "Video Tutorial Script" in extras:
            st.markdown(f"### 🎬 Video Script\n```\n{video_script}\n```")

        if "Voiceover Script" in extras:
            st.markdown(f"### 🎤 Voiceover Script\n```\n{voiceover_script}\n```")

        if "UI Mockup" in extras:
            st.markdown(f"### 🖼️ UI Mockup Description\n```\n{ui_mockup}\n```")

elif selected_tab == "📚 About":
    st.title("📚 About ProjectGPT")
    st.markdown("""
    ProjectGPT is a startup initiative to bridge the gap between learning and doing.
    Our platform lets students, job seekers, and professionals auto-generate full-stack or analytical projects with just a few clicks.

    🚧 MVP built using Python + Streamlit + GPT  
    📈 Vision: Grow into a SaaS platform for personalized AI project generation  
    💡 Built with ❤️ by Shakeel Ahamed
    """)

elif selected_tab == "📞 Contact":
    st.title("📞 Contact & Feedback")
    st.markdown("""
    🔗 Connect on [LinkedIn](https://linkedin.com/in/shakeel-data)  
    📬 Email: shakeelahamed6618@gmail.com  
    💬 WhatsApp: +91 94442 33768
>>>>>>> 58761a10e1991985f42ca2f82f577dc2b5c4bf42
    """)