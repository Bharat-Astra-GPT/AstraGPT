import streamlit as st
from groq import Groq
import google.generativeai as genai
from fpdf import FPDF
import time

# --- 1. PREMIUM UI CONFIG & DESIGN ---
st.set_page_config(page_title="Bharat-Astra-GPT", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for Global Best UI
st.markdown("""
    <style>
    /* Gradient Background & Fonts */
    .stApp { background: radial-gradient(circle at bottom, #101014, #050505); color: #FFFFFF; font-family: 'Inter', sans-serif; }
    
    /* Bottom Chat Bar Container */
    .stChatInputContainer {
        border-radius: 30px !important;
        background-color: #1e1f20 !important;
        border: 1px solid #3c4043 !important;
        padding: 5px 15px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }
    
    /* Research Mode Indicator (Top Right) */
    .research-indicator {
        position: fixed; top: 20px; right: 20px;
        padding: 5px 15px; background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 20px; color: black; font-weight: bold; font-size: 12px;
    }
    
    /* Small Circle Loader */
    .stStatus { border: none !important; background: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CORE IDENTITY ---
IDENTITY = "You are Bharat-Astra-GPT, the world's best AI Assistant, created by Mohammad Sartaj. You provide accurate, reasoning-based answers in Simple, Detailed, or Step-by-Step modes. No robotic emojis."

# --- 3. SMART MODES & SIDEBAR ---
with st.sidebar:
    st.title("⚡ Bharat-Astra")
    st.caption("Developed by Mohammad Sartaj")
    st.divider()
    app_mode = st.selectbox("🎯 Smart Mode", ["Student Mode", "Exam Mode", "Creator Mode", "Developer Mode", "Researcher Mode"])
    st.divider()
    research_on = st.toggle("🔍 Research Mode (Web-Deep)")
    st.divider()
    st.button("🧠 AI Memory")
    st.button("📄 PDF Tools (Convert/Summary)")

if research_on:
    st.markdown('<div class="research-indicator">Research Mode ON</div>', unsafe_allow_html=True)

# --- 4. FLOATING ACTION BUTTONS (Above Chatbox) ---
col_img, col_vid, col_blank = st.columns([1, 1, 6])
with col_img:
    gen_img = st.button("🎨 Image AI")
with col_vid:
    gen_vid = st.button("🎥 Video AI")

# --- 5. CHAT ENGINE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "media" in msg: st.image(msg["media"])

# --- 6. INPUT AREA (Plus icon Left, Send Right) ---
# Note: Streamlit handles Send button on right by default. 
# We use the Plus expander for Left-side inputs.

with st.expander("➕ Upload Anything", expanded=False):
    c1, c2, c3, c4 = st.columns(4)
    c1.file_uploader("🖼 Image", type=['png','jpg'], key="img_up")
    c2.file_uploader("📄 PDF/Doc", type=['pdf','docx'], key="pdf_up")
    c3.file_uploader("🎥 Video", type=['mp4'], key="vid_up")
    c4.camera_input("📷 Camera")

if prompt := st.chat_input("Ask anything... type, speak, or upload"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Dynamic Loader Label
        loader_text = "🎨 Creating..." if "create" in prompt.lower() or gen_img else "🔍 Analyzing..."
        
        with st.status(loader_text, expanded=True) as s:
            time.sleep(1.2)
            
            # --- FEATURE: IMAGE GEN ---
            if "create" in prompt.lower() or "image" in prompt.lower() or gen_img:
                # 4K & Anatomy Fix Internal Prompting
                final_prompt = f"{prompt}, 4k resolution, cinematic, hyper-realistic, highly detailed skin and fingers, masterpiece"
                img_url = f"https://pollinations.ai/p/{final_prompt.replace(' ', '%20')}?width=1024&height=1024&model=flux"
                st.image(img_url)
                response_text = "Maine aapka visual design kar diya hai."
                st.session_state.messages.append({"role": "assistant", "content": response_text, "media": img_url})
            
            # --- FEATURE: RESEARCH / CHAT ---
            else:
                client = Groq(api_key=st.secrets["GROQ_KEY"])
                # Custom Reasoning Logic based on Mode
                mode_instruction = f"Mode: {app_mode}. Explain in Step-by-Step detail."
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": IDENTITY + mode_instruction}] + st.session_state.messages
                )
                response_text = response.choices[0].message.content
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            
            s.update(label="✅ Task Complete", state="complete")
    
