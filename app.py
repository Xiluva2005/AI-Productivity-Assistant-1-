import streamlit as st

st.set_page_config(page_title="AI Productivity Assistant", page_icon="🤖")
st.title("🤖 AI Productivity Assistant")
st.write("By XC Mhlanga")

task = st.sidebar.selectbox("Choose a task", ["Email Generation", "Meeting Summary", "Task Planning", "Research Help", "Chatbot"])

if task == "Email Generation":
    st.header("Email Generator")
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Apologetic"])
    text = st.text_area("What is the email about?")
    if st.button("Generate"):
        st.success(f"Subject: Re {text[:20]}\n\nDear Team,\n\n{tone} email about {text}.\n\nBest regards")

elif task == "Meeting Summary":
    st.header("Meeting Summarizer")
    t = st.text_area("Paste transcript")
    if st.button("Summarize"):
        st.info(f"Summary: Meeting about {t[:100]}... \nDecisions: Agreed \nActions: Follow up")

elif task == "Task Planning":
    st.header("Task Planner")
    g = st.text_input("Goal")
    if st.button("Plan"):
        st.success(f"Plan for {g}: 1. Research 2. Draft 3. Submit")

elif task == "Research Help":
    st.header("Research Assistant")
    top = st.text_input("Topic")
    if st.button("Research"):
        st.success(f"Research on {top}: Key points about productivity and AI tools. Source: OpenAI docs")

else:
    st.header("Chatbot")
    q = st.text_input("Ask me")
    if st.button("Ask"):
        st.write(f"Answer for '{q}': Break it into small tasks and use AI tools.")
