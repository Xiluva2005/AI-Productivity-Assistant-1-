"""
AI Productivity Assistant - Backend
Functional Flask API demonstrating prompt engineering and AI tool integration
"""
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Import prompt library
from prompts import PROMPTS

# --- Mock AI call (Replace with real API) ---
def call_ai(prompt_key, user_input, extra={}):
    """
    Replace this function with:
    openai.chat.completions.create(
      model="gpt-4o",
      messages=[{"role":"system","content":PROMPTS[prompt_key]}, {"role":"user","content": user_input}]
    )
    or Gemini equivalent.
    """
    template = PROMPTS[prompt_key]
    # For demo, return templated response showing prompt engineering
    return f"[PROMPT USED: {prompt_key}]\n{template[:200]}...\n\n[USER INPUT]: {user_input}\n[EXTRA]: {extra}\n\n[AI OUTPUT would be here - connect your API key]"

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/api/email', methods=['POST'])
def api_email():
    data = request.json
    result = call_ai('email_generation', data.get('text',''), {'tone': data.get('tone')})
    return jsonify({'result': result})

@app.route('/api/meeting', methods=['POST'])
def api_meeting():
    data = request.json
    result = call_ai('meeting_summary', data.get('text',''))
    return jsonify({'result': result})

@app.route('/api/task', methods=['POST'])
def api_task():
    data = request.json
    result = call_ai('task_planning', data.get('text',''))
    return jsonify({'result': result})

@app.route('/api/research', methods=['POST'])
def api_research():
    data = request.json
    result = call_ai('research', data.get('text',''))
    return jsonify({'result': result})

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json
    result = call_ai('chatbot', data.get('text',''))
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
