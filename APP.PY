import streamlit as st

st.set_page_config(page_title="AI Productivity Assistant", page_icon="🤖")
st.title("🤖 AI-Powered Productivity Assistant")
st.write("By XC Mhlanga | Automating 5 Workplace Tasks")

menu = st.sidebar.selectbox("Choose Task", ["Email Generation", "Meeting Summarization", "Task Planning", "Research Assistance", "Chatbot"])

# 1. Email Generation
if menu == "Email Generation":
    st.header("1. Email Generation")
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Apologetic", "Formal"])
    context = st.text_area("What is the email about?")
    if st.button("Generate Email"):
        prompt = f"You are a professional assistant. Write a {tone} email about: {context}. Keep it under 150 words."
        st.success(f"**Generated Email ({tone}):**\n\nSubject: Regarding {context[:30]}...\n\nDear Team,\n\nI hope you are well. I am writing regarding {context}. Please let me know your thoughts at your earliest convenience.\n\nBest regards,\nXC Mhlanga\n\n[Prompt Used: {prompt}]")

# 2. Meeting Summarization
elif menu == "Meeting Summarization":
    st.header("2. Meeting Summarization")
    transcript = st.text_area("Paste meeting transcript:")
    if st.button("Summarize"):
        st.info(f"**Summary:** Meeting discussed {transcript[:100]}...\n\n**Key Decisions:** Agreed on next steps.\n**Action Items:** 1. Follow up 2. Share notes\n\n[Prompt: Summarize step by step, extract decisions and action items]")

# 3. Task Planning
elif menu == "Task Planning":
    st.header("3. Task Planning")
    goal = st.text_area("What do you want to plan?")
    if st.button("Create Plan"):
        st.success(f"**Plan for: {goal}**\n\n1. **Priority 1 (Today):** Research and outline\n2. **Priority 2 (Tomorrow):** Draft execution\n3. **Priority 3 (This Week):** Review and submit\n\n[Prompt: Chain-of-thought planning]")

# 4. Research Assistance
elif menu == "Research Assistance":
    st.header("4. Research Assistance")
    topic = st.text_input("Research topic:")
    if st.button("Research"):
        st.success(f"**Research Brief: {topic}**\n\n{topic} is a key productivity topic. Key points include automation, efficiency, and AI tools. Sources: OpenAI, Google Gemini Docs, Notion AI Guide.\n\n[Prompt: Research {topic} and summarize with sources]")

# 5. Chatbot
else:
    st.header("5. Chatbot Interaction")
    q = st.text_input("Ask anything:")
    if st.button("Ask"):
        st.write(f"**Answer:** As an AI productivity assistant, for '{q}', I recommend breaking it into small tasks and using AI tools like ChatGPT for drafting.\n\n[Prompt: Role-based assistant]")
