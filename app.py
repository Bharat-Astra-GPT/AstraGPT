import streamlit as st
from streamlit_chat import message  # Streamlit chat style
import openai
from PIL import Image
import io
import time
import pdfplumber
import docx

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="NEXT LEVEL ASTRA 🚀",
    page_icon="🚀",
    layout="wide"
)

# ================= SESSION STATE =================
if "chat" not in st.session_state:
    st.session_state.chat = []

if "mode" not in st.session_state:
    st.session_state.mode = "Fast"

if "show_plus" not in st.session_state:
    st.session_state.show_plus = False

if "show_dashboard" not in st.session_state:
    st.session_state.show_dashboard = False

# ================= OPENAI SETUP =================
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key

# ================= CSS =================
st.markdown("""
<style>
.stApp {background:#0d0d0f; color:white;}
.header {text-align:center; margin-bottom:10px;}
.header h1{margin:0; font-weight:600;}
.header p{opacity:0.6; margin:0;}
.user {background:#1a1a1c; padding:12px 16px; border-radius:18px; margin:8px 0; text-align:right;}
.ai {background:#111; padding:12px 16px; border-radius:18px; margin:8px 0;}
.bottom {position:fixed; bottom:15px; left:50%; transform:translateX(-50%); width:95%; max-width:850px; background:#1a1a1c; border-radius:28px; padding:12px; border:1px solid #2d2d2f;}
.row{display:flex;align-items:center;gap:10px;}
.input{flex:1; background:transparent; border:none; color:white; font-size:16px; outline:none;}
.icon{cursor:pointer; font-size:20px; padding:6px 10px;}
.send{background:linear-gradient(135deg,#4facfe,#00f2fe); border:none; color:black; padding:8px 14px; border-radius:50%; font-size:18px; cursor:pointer;}
.popup{background:#f0f2f5; color:black; border-radius:16px; padding:15px; margin:10px auto; max-width:500px;}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div class="header">
    <h1>NEXT LEVEL ASTRA 🚀</h1>
    <p>By Mohammad Sartaj</p>
</div>
""", unsafe_allow_html=True)

# ================= CHAT DISPLAY =================
for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.markdown(f"<div class='user'>{msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai'>{msg['text']}</div>", unsafe_allow_html=True)

# ================= POPUPS =================
if st.session_state.show_plus:
    st.markdown("""
    <div class="popup">
    📷 Camera<br><br>
    🖼 Gallery<br><br>
    📎 Files<br><br>
    ☁️ Drive
    </div>
    """, unsafe_allow_html=True)

if st.session_state.show_dashboard:
    st.markdown("""
    <div class="popup">
    ⚡ Fast Mode<br><br>
    🔍 Research Mode<br><br>
    🧠 Thinking Mode<br><br>
    🎨 Create Image<br><br>
    🧹 Clear Chat
    </div>
    """, unsafe_allow_html=True)

# ================= INPUT =================
query = st.text_input("", placeholder="Ask Astra AI...")

# ================= FILE UPLOAD =================
uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "png", "jpg", "docx"])
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            st.session_state.chat.append({"role":"ai","text":f"PDF uploaded: {uploaded_file.name}\nContent:\n{text[:500]}..."})
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])
        st.session_state.chat.append({"role":"ai","text":f"DOCX uploaded: {uploaded_file.name}\nContent:\n{text[:500]}..."})
    else:
        st.session_state.chat.append({"role":"ai","text":f"File received: {uploaded_file.name}"})

# ================= VOICE INPUT (Experimental) =================
voice_query = st.text_area("Or paste your voice-to-text here (Android/MP3 supported)")

# ================= AI RESPONSE =================
def ai_response(text):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": text}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {e}"

# ================= SEND =================
if st.button("Send") or query:
    user_text = query if query else voice_query
    if user_text:
        st.session_state.chat.append({"role":"user","text":user_text})
        reply = ai_response(user_text)
        st.session_state.chat.append({"role":"ai","text":reply})
        st.experimental_rerun()

# ================= BOTTOM BAR =================
st.markdown("""
<div class="bottom">
  <div class="row">
    <span class="icon">＋</span>
    <span class="icon">☰</span>
    <input class="input" placeholder="Ask Astra AI...">
    <span class="icon">🎤</span>
    <button class="send">➤</button>
  </div>
</div>
""", unsafe_allow_html=True)

# ================= CONTROLS =================
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("➕ Attach"):
        st.session_state.show_plus = not st.session_state.show_plus
        st.session_state.show_dashboard = False
        st.experimental_rerun()
with c2:
    if st.button("☰ Dashboard"):
        st.session_state.show_dashboard = not st.session_state.show_dashboard
        st.session_state.show_plus = False
        st.experimental_rerun()
with c3:
    mode = st.selectbox("Mode", ["Fast","Research","Thinking","Image"])
    st.session_state.mode = mode

# ================= IMAGE GENERATION =================
if st.session_state.mode == "Image":
    prompt = st.text_input("Enter image prompt")
    if st.button("Generate Image"):
        try:
            img_result = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            img_url = img_result['data'][0]['url']
            st.image(img_url)
        except Exception as e:
            st.error(f"Image generation error: {e}")
