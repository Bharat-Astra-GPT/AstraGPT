import streamlit as st
from groq import Groq

# Streamlit Secrets se Key lena
if "GROQ_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_KEY"])

st.set_page_config(page_title="Bharat Astra GPT", page_icon="🚀")
st.title("🚀 Bharat Astra GPT")

prompt = st.chat_input("Puchiye kuch bhi...")
if prompt:
    with st.spinner("Bharat Astra soch raha hai..."):
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        st.write(completion.choices[0].message.content)
        
