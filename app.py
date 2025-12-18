import os
import openai
import google.generativeai as genai

openai.api_key = st.secrets["OPENAI_API_KEY"]
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def ai_response(text):
    if st.session_state.mode == "Fast":
        return text

    if st.session_state.mode == "Research":
        model = genai.GenerativeModel("gemini-pro")
        res = model.generate_content(text)
        return res.text

    if st.session_state.mode == "Thinking":
        time.sleep(1)
        return "🧠 Deep thinking...\n" + text
