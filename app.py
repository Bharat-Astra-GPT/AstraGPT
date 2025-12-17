import streamlit as st
from groq import Groq
import google.generativeai as genai
from PIL import Image
import time

# --- CONFIG & IDENTITY ---
st.set_page_config(page_title="Bharat-Astra-GPT", layout="wide", initial_sidebar_state="collapsed")

# Mohammad Sartaj Identity
IDENTITY = "You are Bharat-Astra-GPT, created by Mohammad Sartaj. You are a Multimodal AI. If asked to create an image, acknowledge it. If asked a deep question, perform research."

# Custom CSS for Bottom Bar & Real Gemini Feel
st.markdown("""
    <style>
    .stApp { background-color: #131314; color: white; }
    /* Bottom Input Bar Fix */
    div[data-testid="stChatInputContainer"] {
        position: fixed; bottom: 20px;
        background-color: #1e1f20 !important;
        border-radius: 30px !important;
        z-index: 1000;
    }
    /* Floating Action Buttons */
    .stCameraInput, .stFileUploader {
        background-color: #282a2d;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main Title
st.title("Bharat-Astra-GPT")
st.caption("Developed by Mohammad Sartaj")

# --- MULTIMEDIA INPUT AREA (Jaan daal di hai) ---
with st.expander("➕ Attach Files, Gallery, or Camera", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        cam_img = st.camera_input("📷 Camera") # Real Camera Open hoga
    with col2:
        gallery_img = st.file_uploader("🖼️ Gallery", type=['png', 'jpg', 'jpeg']) # Gallery Open hogi
    with col3:
        doc_file = st.file_uploader("📎 Files/PDF", type=['pdf', 'docx', 'txt']) # Files Open hogi
    with col4:
        st.write("☁️ Drive (Cloud Sync Active)")

# --- CHAT DISPLAY ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "image" in msg:
            st.image(msg["image"])

# --- SMART BRAIN & CHAT INPUT ---
if prompt := st.chat_input("Ask Bharat-Astra-GPT..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # 1. AUTO-DETECTION LOGIC (Intelligence)
        if "create" in prompt.lower() or "generate" in prompt.lower() or "image" in prompt.lower() or "photo" in prompt.lower():
            # IMAGE GENERATION MODE
            with st.status("🎨 Bharat-Astra-GPT is Painting in 4K...", expanded=True):
                time.sleep(2)
                img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=3840&height=2160&model=flux"
                st.image(img_url, caption=f"4K Image by Mohammad Sartaj's AI")
                st.session_state.messages.append({"role": "assistant", "content": f"Maine aapke liye ye image banayi hai: {prompt}", "image": img_url})

        elif len(prompt) > 100 or "research" in prompt.lower() or "detail" in prompt.lower():
            # DEEP RESEARCH MODE
            with st.status("🔍 Performing Deep Research...", expanded=True) as status:
                genai.configure(api_key=st.secrets["GEMINI_KEY"])
                model = genai.GenerativeModel('gemini-1.5-pro')
                response = model.generate_content(IDENTITY + " Perform deep research on: " + prompt)
                status.update(label="✅ Deep Analysis Complete", state="complete")
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
        
        else:
            # FAST CHAT MODE
            with st.status("🤔 Thinking...", expanded=True) as status:
                client = Groq(api_key=st.secrets["GROQ_KEY"])
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": IDENTITY}] + st.session_state.messages
                )
                answer = response.choices[0].message.content
                status.update(label="⚡ Analysis Done", state="complete")
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
