import streamlit as st
from groq import Groq

# Streamlit Secrets se Groq Key lena
if "GROQ_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_KEY"])
else:
    st.error("Please add GROQ_KEY in Streamlit Secrets!")

st.set_page_config(page_title="Bharat Astra GPT", page_icon="🚀")
st.title("🚀 Bharat Astra GPT (Powered by Groq)")

# Chat Interface
prompt = st.chat_input("Puchiye kuch bhi...")

if prompt:
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # Groq ka sabse powerful model
        messages=[{"role": "user", "content": prompt}]
    )
    st.write(completion.choices[0].message.content)
    
