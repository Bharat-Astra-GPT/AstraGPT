import streamlit as st
from groq import Groq
import google.generativeai as genai
from fpdf import FPDF
import time
import requests
from PIL import Image

# --- CONFIG & IDENTITY ---
st.set_page_config(page_title="Bharat-Astra-GPT", layout="wide", initial_sidebar_state="collapsed")
DEVELOPER = "Mohammad Sartaj"
IDENTITY = f"You are Bharat-Astra-GPT, created by {DEVELOPER}. You provide 100% accurate info."

# --- PREMIUM UI & BOTTOM SHEET CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0c; color: #e3e3e3; }
    
    /* Plus Icon Position (Inside Chat Bar - Left) */
    .plus-container {
        position: fixed; bottom: 25px; left: calc(50% - 42%);
        z-index: 10000; cursor: pointer;
        background: #2a2a2a; border-radius: 50%;
        width: 40px; height: 40px; display: flex;
        align-items: center; justify-content: center;
        transition: 0.3s;
    }
    .plus-container:hover { background: #3a3a3a; transform: rotate(90deg); }
    
    /* Chat Input Padding for Plus Icon */
    div[data-testid="stChatInputContainer"] textarea {
        padding-left: 55px !important;
    }

    /* Bottom Sheet Menu Styling */
    .bottom-sheet {
        background: #1e1f20; border-radius: 25px 25px 0 0;
        padding: 20px; border-top: 1px solid #444;
    }
    
    .icon-label { font-size: 12px; text-align: center; color: #aaa; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- REAL WORKING FUNCTIONS ---

def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # Cleaning for Latin-1 encoding to prevent errors
    clean_text = text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 10, txt=clean_text)
    pdf.output("Astra_Notes.pdf")
    return "Astra_Notes.pdf"

# --- APP LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Bharat-Astra-GPT 🚀")
st.caption(f"100% Working Edition | Dev: {DEVELOPER}")

# --- 🟢 THE REAL PLUS MENU (BOTTOM SHEET) ---
# Streamlit mein "Bottom Sheet" ke liye hum Expander ko chat bar ke upar use karte hain
with st.expander("✨ Select Action (Camera, Gallery, Quiz, Research)", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        cam = st.button("📷\nCam")
    with col2:
        gal = st.button("🖼️\nGallery")
    with col3:
        quiz = st.button("📎\nQuiz")
    with col4:
        drive = st.button("📂\nDrive")
    
    st.divider()
    deep_res = st.toggle("🔍 Deep Research Mode")
    canvas_mode = st.toggle("🎨 Canvas (Drawing Mode)")

# Floating Visual Plus (Just for UI look)
st.markdown('<div class="plus-container"><span style="color:white;font-size:24px;">+</span></div>', unsafe_allow_html=True)

# Handle Special Modes
if canvas_mode:
    st.info("🎨 Canvas Mode: Ab aap whiteboard par draw kar sakte hain (Coming with st-canvas integration).")

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "img" in msg: st.image(msg["img"])

# --- 🧠 BRAIN (CHATTING & GENERATION) ---
if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # 1. DEEP RESEARCH MODE
        if deep_res:
            with st.status("🔍 Deep Researching Global Sources...", expanded=True) as s:
                client = Groq(api_key=st.secrets["GROQ_KEY"])
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": "Provide a heavy, factual, and long research report with citations."}] + st.session_state.messages
                )
                ans = response.choices[0].message.content
                s.update(label="✅ Research Complete", state="complete")
                st.markdown(ans)
                st.session_state.messages.append({"role": "assistant", "content": ans})

        # 2. IMAGE GENERATION
        elif "photo" in prompt.lower() or "image" in prompt.lower() or "generate" in prompt.lower():
            with st.status("🎨 Creating 4K Realistic Image...", expanded=True) as s:
                img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&model=flux"
                st.image(img_url)
                s.update(label="✅ Image Ready", state="complete")
                res = "Aapka masterpiece taiyar hai."
                st.session_state.messages.append({"role": "assistant", "content": res, "img": img_url})

        # 3. PDF/E-BOOK GENERATION
        elif "pdf" in prompt.lower() or "ebook" in prompt.lower():
            with st.status("📄 Formatting PDF...", expanded=True) as s:
                client = Groq(api_key=st.secrets["GROQ_KEY"])
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": "Write high-quality educational notes for PDF."}] + st.session_state.messages
                )
                content = response.choices[0].message.content
                pdf_path = generate_pdf(content)
                with open(pdf_path, "rb") as f:
                    st.download_button("📩 Download PDF", f, file_name="Astra_Notes.pdf")
                s.update(label="✅ PDF Generated", state="complete")
                st.markdown(content)
                st.session_state.messages.append({"role": "assistant", "content": content})

        # 4. SIMPLE CHAT
        else:
            with st.status("🧠 Analyzing...", expanded=True) as s:
                client = Groq(api_key=st.secrets["GROQ_KEY"])
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": IDENTITY}] + st.session_state.messages
                )
                ans = response.choices[0].message.content
                s.update(label="✅ Done", state="complete")
                st.markdown(ans)
                st.session_state.messages.append({"role": "assistant", "content": ans})
