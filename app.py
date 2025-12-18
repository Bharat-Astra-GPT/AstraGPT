import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Bharat Astra GPT",
    page_icon="✨",
    layout="wide"
)

# ================= SESSION STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_menu" not in st.session_state:
    st.session_state.show_menu = False

# ================= THEME =================
st.markdown("""
<style>
.stApp { background-color:#0d0d0f; color:white; }

.chat-wrap {
    max-width:820px;
    margin:auto;
    padding-bottom:160px;
}

.msg {
    padding:14px 18px;
    border-radius:14px;
    margin-bottom:12px;
    font-size:15px;
}
.user {
    background:#1a1a1c;
    border:1px solid #2d2d2f;
    margin-left:auto;
}
.bot {
    background:#0d0d0f;
    border:1px solid #1f1f22;
    color:#cfcfcf;
}

.bottom-bar {
    position:fixed;
    bottom:18px;
    left:0;
    right:0;
    display:flex;
    justify-content:center;
}

.bar-inner {
    width:92%;
    max-width:820px;
    background:#1a1a1c;
    border-radius:24px;
    padding:10px 12px;
    border:1px solid #2d2d2f;
}

.popup {
    background:#1a1a1c;
    border:1px solid #2d2d2f;
    border-radius:18px;
    padding:10px;
    margin-bottom:10px;
}

.popup div {
    padding:10px 14px;
    border-radius:12px;
}
.popup div:hover {
    background:#2a2a2c;
}
</style>
""", unsafe_allow_html=True)

# ================= CHAT =================
st.markdown("<div class='chat-wrap'>", unsafe_allow_html=True)

for m in st.session_state.messages:
    cls = "user" if m["role"] == "user" else "bot"
    st.markdown(
        f"<div class='msg {cls}'>{m['content']}</div>",
        unsafe_allow_html=True
    )

# ================= POPUP MENU =================
if st.session_state.show_menu:
    st.markdown("""
    <div class="popup">
        <div>📷 Camera</div>
        <div>🖼️ Gallery</div>
        <div>📂 File</div>
        <div>☁️ Drive</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ================= INPUT BAR =================
st.markdown("<div class='bottom-bar'>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1,6,1])

with c1:
    if st.button("➕"):
        st.session_state.show_menu = not st.session_state.show_menu

with c2:
    text = st.text_area(
        "",
        placeholder="Ask Bharat Astra GPT…",
        height=55,
        label_visibility="collapsed"
    )

with c3:
    send = st.button("➤")

st.markdown("</div>", unsafe_allow_html=True)

# ================= SEND LOGIC =================
if send and text.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": text
    })
    st.session_state.messages.append({
        "role": "assistant",
        "content": "🤖 Astra GPT received your message."
    })
    st.session_state.show_menu = False
    st.rerun()
