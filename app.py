import streamlit as st
from groq import Groq
import google.generativeai as genai

# Page Setup - Pro Look
st.set_page_config(page_title="Bharat Astra Pro", page_icon="🚀", layout="wide")

# Custom CSS for Pro Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #262730; color: white; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# System Prompt - Mohammad Sartaj ki Identity
SYSTEM_PROMPT = "You are Bharat Astra, a super-intelligent AI created by Mohammad Sartaj. Always be polite, fast, and if someone asks who created you, proudly say that you were developed by Mohammad Sartaj."

# Sidebar
st.sidebar.title("🚀 Bharat Astra Pro")
st.sidebar.subheader("Created by Mohammad Sartaj")
mode = st.sidebar.radio("Features", ["💬 Ultra-Fast Chat", "👁️ Vision Assistant", "🎨 Image Studio (Links)"])

# --- 💬 Mode 1: Groq Ultra-Fast ---
if mode == "💬 Ultra-Fast Chat":
    st.title("Bharat Astra Chat")
    client = Groq(api_key=st.secrets["GROQ_KEY"])
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("Puchiye Mohammad Sartaj ke AI se..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages
            )
            msg = response.choices[0].message.content
            st.markdown(msg)
            st.session_state.messages.append({"role": "assistant", "content": msg})

# --- 👁️ Mode 2: Vision ---
elif mode == "👁️ Vision Assistant":
    st.title("Astra Vision (Pro)")
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    img_file = st.camera_input("Apne camera se kuch dikhayein")
    if img_file:
        from PIL import Image
        img = Image.open(img_file)
        if st.button("Analyze with Astra AI"):
            response = model.generate_content([SYSTEM_PROMPT + " Analyze this image.", img])
            st.write(response.text)

# --- 🎨 Mode 3: Image Hub ---
elif mode == "🎨 Image Studio (Links)":
    st.title("AI Image Generation Hub")
    st.info("Direct integration coming soon. Use these pro tools for now:")
    cols = st.columns(3)
    cols[0].link_button("Flux AI", "https://huggingface.co/spaces/black-forest-labs/FLUX.1-dev")
    cols[1].link_button("Ideogram", "https://ideogram.ai/")
    cols[2].link_button("Bing Designer", "https://www.bing.com/images/create")
