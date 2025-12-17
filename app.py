import streamlit as st
import google.generativeai as genai

# Streamlit ke Secrets se API key lega
if "GEMINI_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
else:
    st.error("Dhyan dein: Streamlit Secrets mein GEMINI_KEY missing hai!")

st.set_page_config(page_title="AstraGPT", page_icon="🚀")

st.markdown("<h1 style='text-align: center; color: #FF9933;'>🚀 AstraGPT: The Indian AI</h1>", unsafe_allow_html=True)

# Chat Box
prompt = st.chat_input("Puchiye AstraGPT se kuch bhi...")

if prompt:
    with st.spinner("AstraGPT soch raha hai..."):
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(prompt)
        st.write(response.text)
