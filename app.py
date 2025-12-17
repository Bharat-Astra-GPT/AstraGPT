import streamlit as st
from groq import Groq
import google.generativeai as genai
from fpdf import FPDF
from gtts import gTTS
import time
import base64

# --- 1. GLOBAL UI & THEME (NEON FUTURISTIC) ---
st.set_page_config(page_title="Bharat-Astra-GPT Ultimate", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* UI Deep Theme */
    .stApp { background: radial-gradient(circle at bottom, #10121a, #050505); color: #e0e0e0; font-family: 'Inter', sans-serif; }
    
    /* Typing Box Styling (Floating Center-Bottom) */
    div[data-testid="stChatInputContainer"] {
        background-color: #1e1f20 !important;
        border-radius: 25px !important;
        border: 1px solid #3c4043 !important;
        padding: 8px 15px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8) !important;
    }
    
    /* Toolbar Style */
    .toolbar-btn {
        display: inline-block; padding: 10px 20px; margin: 5px;
        background: rgba(255, 255, 255, 0.05); border: 1px solid #444;
        border-radius: 12px; cursor: pointer; transition: 0.3s;
    }
    .toolbar-btn:hover { background: #007bff; color: white; border-color: #007bff; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CORE IDENTITY & LOGIC ---
DEVELOPER = "Mohammad Sartaj"
IDENTITY = f"You are Bharat-Astra-GPT, the world's most advanced AI Assistant, developed by {DEVELOPER}."

# --- 3. TOP TOOLBAR (Above Chat) ---
st.markdown("### 🛠️ Bharat-Astra ToolHub")
t_col1, t_col2, t_col3, t_col4, t_col5, t_col6 = st.columns(6)

with t_col1:
    mode_research = st.checkbox("🔍 Research", help="Deep Factual Answers")
with t_col2:
    mode_study = st.checkbox("🎓 Study", help="Step-by-Step Teacher Mode")
with t_col3:
    mode_code = st.checkbox("💻 Coding", help="Clean & Commented Code")
with t_col4:
    gen_img = st.button("🎨 Image AI")
with t_col5:
    gen_pdf = st.button("📄 PDF Gen")
with t_col6:
    web_app = st.button("🌐 Web/App")

# --- 4. SIDEBAR (History & History) ---
with st.sidebar:
    st.title("⚡ Bharat-Astra")
    st.write(f"Dev: {DEVELOPER}")
    st.divider()
    st.button("🆕 New Chat")
    st.button("📜 History")
    st.button("🎓 Learning Paths")
    st.divider()
    theme = st.select_slider("Theme", options=["Dark", "Neon", "Light"])

# --- 5. CHAT SYSTEM ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying Chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "img" in msg: st.image(msg["img"])

# --- 6. PLUS (+) MENU (Expanded Controls) ---
with st.expander("➕ Attach & AI Tools", expanded=False):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.file_uploader("🖼 Upload Image", type=['png','jpg'], key="img_up")
        st.camera_input("📷 Live Scan")
    with c2:
        st.file_uploader("📄 Upload PDF/DOC", type=['pdf','docx'], key="pdf_up")
        st.button("📄 Text to PPT")
    with c3:
        st.file_uploader("🎧 Upload Audio", type=['mp3','wav'], key="aud_up")
        st.button("🗺 Mind Map")
    with c4:
        st.file_uploader("🎥 Upload Video", type=['mp4'], key="vid_up")
        st.button("🎤 Voice Transcription")

# --- 7. MAIN INPUT & BRAIN ---
if prompt := st.chat_input("Ask anything… Learn, Build, Create 🚀"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Logic for Thinking Animation
        status_label = "🎨 Creating..." if "create" in prompt.lower() or gen_img else "🧠 Analyzing..."
        
        with st.status(status_label, expanded=True) as status:
            time.sleep(1.5)
            
            # --- FEATURE 1: IMAGE GENERATION (Anatomy Fix Internal) ---
            if "create" in prompt.lower() or "image" in prompt.lower() or gen_img:
                final_prompt = f"{prompt}, high definition, 4k, hyper-realistic skin, perfect fingers, cinematic lighting"
                img_url = f"https://pollinations.ai/p/{final_prompt.replace(' ', '%20')}?width=1024&height=1024&model=flux"
                st.image(img_url)
                ans = "Maine aapka ultra-realistic visual create kar diya hai."
                st.session_state.messages.append({"role": "assistant", "content": ans, "img": img_url})
            
            # --- FEATURE 2: WEB/APP BUILDER LOGIC ---
            elif "website" in prompt.lower() or "app" in prompt.lower() or web_app:
                status.update(label="🌐 Designing Architecture...", state="running")
                client = Groq(api_key=st.secrets["GROQ_KEY"])
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": "You are a Senior Full-Stack Architect. Provide Roadmap, Code, and Hosting Guide."}] + st.session_state.messages
                )
                ans = response.choices[0].message.content
                st.markdown(ans)
                st.session_state.messages.append({"role": "assistant", "content": ans})

            # --- FEATURE 3: GENERAL INTELLIGENCE (NCERT/Code/Study) ---
            else:
                client = Groq(api_key=st.secrets["GROQ_KEY"])
                sys_prompt = IDENTITY
                if mode_study: sys_prompt += " Explain like a teacher (NCERT style)."
                if mode_code: sys_prompt += " Provide professional code with comments."
                
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": sys_prompt}] + st.session_state.messages
                )
                ans = response.choices[0].message.content
                st.markdown(ans)
                st.session_state.messages.append({"role": "assistant", "content": ans})
            
            status.update(label="✅ Ready!", state="complete")
                         
