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

if "show_plus" not in st.session_state:
    st.session_state.show_plus = False

# ================= PREMIUM THEME =================
st.markdown("""
<style>
/* ---- BACKGROUND ---- */
body {
    background: radial-gradient(circle at top, #0b1220, #020617);
}

/* ---- CONTAINER ---- */
.chat-container {
    max-width: 880px;
    margin: auto;
    padding-bottom: 140px;
}

/* ---- MESSAGE ---- */
.msg {
    padding: 14px 18px;
    border-radius: 18px;
    margin-bottom: 12px;
    font-size: 15px;
    line-height: 1.5;
    animation: fadeIn 0.25s ease-in;
}
.user {
    background: #0f172a;
    border-left: 4px solid #38bdf8;
    color: #e5e7eb;
}
.bot {
    background: #111827;
    border-left: 4px solid #a78bfa;
    color: #e5e7eb;
}

/* ---- INPUT BOARD ---- */
.input-wrap {
    position: fixed;
    bottom: 18px;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
}

.input-board {
    width: 880px;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(10px);
    border-radius: 22px;
    padding: 10px;
    box-shadow: 0 0 0 1px #1f2937;
}

/* ---- BUTTONS ---- */
.icon-btn {
    background: #1e293b;
    border: none;
    color: white;
    font-size: 18px;
    padding: 9px 13px;
    border-radius: 50%;
    cursor: pointer;
}
.icon-btn:hover {
    background: #334155;
}

/* ---- PLUS PANEL ---- */
.plus-panel {
    background: #020617;
    border-radius: 16px;
    padding: 10px;
    margin-bottom: 10px;
    box-shadow: 0 0 0 1px #1f2937;
}
.plus-item {
    padding: 10px 14px;
    border-radius: 12px;
    background: #0f172a;
    margin-bottom: 8px;
    color: #e5e7eb;
    font-size: 14px;
}

/* ---- ANIMATION ---- */
@keyframes fadeIn {
    from { opacity:0; transform:translateY(6px); }
    to { opacity:1; transform:translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# ================= CHAT =================
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for m in st.session_state.messages:
    cls = "user" if m["role"] == "user" else "bot"
    st.markdown(
        f"<div class='msg {cls}'>{m['content']}</div>",
        unsafe_allow_html=True
    )

# ================= PLUS PANEL =================
if st.session_state.show_plus:
    st.markdown("""
    <div class="plus-panel">
        <div class="plus-item">📷 Camera</div>
        <div class="plus-item">🖼️ Gallery</div>
        <div class="plus-item">📁 File</div>
        <div class="plus-item">☁️ Drive</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ================= INPUT FIXED BOARD =================
st.markdown("<div class='input-wrap'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,6,1])

with col1:
    if st.button("➕"):
        st.session_state.show_plus = not st.session_state.show_plus

with col2:
    text = st.text_area(
        "",
        placeholder="Message Bharat Astra GPT…",
        height=55,
        label_visibility="collapsed"
    )

with col3:
    send = st.button("✨")

st.markdown("</div>", unsafe_allow_html=True)

# ================= SEND LOGIC =================
if send and text.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": text
    })
    st.session_state.messages.append({
        "role": "assistant",
        "content": "🤖 Ultra-Pro response placeholder."
    })
    st.session_state.show_plus = False
    st.rerun()
