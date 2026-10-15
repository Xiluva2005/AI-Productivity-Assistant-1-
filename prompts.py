# Prompt Engineering Examples

email_prompt = "You are a professional email writer. Write a {tone} email about {context}. Constraint: Max 150 words."

meeting_prompt = "Think step by step. Summarize the following transcript. Then extract: 1. Summary 2. Decisions 3. Action Items. Transcript: {transcript}"

task_prompt = "Chain-of-thought: Break down this goal into 3 prioritized steps: {goal}"

research_prompt = "You are a research assistant. Research {topic}. Provide summary + 3 bullet points + sources."

chatbot_prompt = "You are a helpful workplace chatbot. Answer concisely and helpfully: {question}"

# Few-shot example
few_shot_example = """
Example Input: Write apology email for late submission
Example Output: Subject: Apology for late submission... [example]
Now do for: {new_input}
"""
