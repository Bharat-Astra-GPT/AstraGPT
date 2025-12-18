import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Astra GPT",
    layout="wide"
)

# ---------------- SESSION STATES ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = "fast"   # fast | research | thinking

if "show_attach" not in st.session_state:
    st.session_state.show_attach = False

if "show_dashboard" not in st.session_state:
    st.session_state.show_dashboard = False

# ---------------- CSS (CHATGPT STYLE) ----------------
st.markdown("""
<style>
.stApp{background:#0d0d0f;color:white;}

.chat-box{
    max-width:800px;
    margin:auto;
}

.user{
    text-align:right;
    background:#1a1a1c;
    padding:10px 15px;
    border-radius:18px;
    margin:8px 0;
}

.ai{
    background:#111;
    padding:12px 15px;
    border-radius:18px;
    margin:8px 0;
}

.bottom-bar{
    position:fixed;
    bottom:15px;
    left:50%;
    transform:translateX(-50%);
    width:95%;
    max-width:800px;
    background:#1a1a1c;
    border-radius:30px;
    padding:12px;
    border:1px solid #2d2d2f;
}

.row{display:flex;align-items:center;gap:10px;}

.input{
    flex:1;
    background:transparent;
    border:none;
    color:white;
    font-size:16px;
    outline:none;
}

.icon{
    cursor:pointer;
    font-size:20px;
    padding:6px 10px;
}

.popup{
    background:#f0f2f5;
    color:black;
    border-radius:16px;
    padding:15px;
    margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h2 style='text-align:center;'>Astra GPT</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;opacity:0.6;'>AI by Mohammad Sartaj</p>", unsafe_allow_html=True)

# ---------------- CHAT AREA ----------------
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    role = msg["role"]
    if role == "user":
        st.markdown(f"<div class='user'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- POPUPS ----------------
if st.session_state.show_attach:
    st.markdown("""
    <div class="popup">
        📷 Camera <br><br>
        🖼 Gallery <br><br>
        📎 Files <br><br>
        ☁️ Drive
    </div>
    """, unsafe_allow_html=True)

if st.session_state.show_dashboard:
    st.markdown("""
    <div class="popup">
        ⚡ Fast Reply <br><br>
        🔍 Research <br><br>
        🧠 Thinking
    </div>
    """, unsafe_allow_html=True)

# ---------------- INPUT ----------------
prompt = st.text_input("", placeholder="Message Astra GPT...")

# ---------------- SEND LOGIC ----------------
def ai_reply(text):
    if st.session_state.mode == "fast":
        return f"⚡ Fast answer:\n{text}"

    if st.session_state.mode == "research":
        return f"🔍 Research based answer:\n{text}\n\n(analysis + explanation)"

    if st.session_state.mode == "thinking":
        time.sleep(1)
        return f"🧠 Thinking deeply...\n{text}"

if st.button("Send"):
    if prompt:
        st.session_state.messages.append({"role":"user","content":prompt})

        reply = ai_reply(prompt)
        st.session_state.messages.append({"role":"assistant","content":reply})

        st.rerun()

# ---------------- BOTTOM BAR ----------------
st.markdown("""
<div class="bottom-bar">
  <div class="row">
    <span class="icon">＋</span>
    <span class="icon">☰</span>
    <input class="input" placeholder="Message Astra GPT...">
    <span class="icon">🎤</span>
    <span class="icon">➤</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------- CONTROLS ----------------
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("➕"):
        st.session_state.show_attach = not st.session_state.show_attach
        st.session_state.show_dashboard = False
        st.rerun()

with c2:
    if st.button("☰"):
        st.session_state.show_dashboard = not st.session_state.show_dashboard
        st.session_state.show_attach = False
        st.rerun()

with c3:
    mode = st.selectbox("Mode", ["fast","research","thinking"])
    st.session_state.mode = mode
