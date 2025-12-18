import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Bharat Astra GPT",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "show_plus" not in st.session_state:
    st.session_state.show_plus = False

if "show_dashboard" not in st.session_state:
    st.session_state.show_dashboard = False

if "mode" not in st.session_state:
    st.session_state.mode = "fast"  # fast | research | image

# ---------------- CSS (EXACT DARK UI) ----------------
st.markdown("""
<style>
.stApp{
    background:#0d0d0f;
    color:white;
}

.bottom-bar{
    position:fixed;
    bottom:15px;
    left:50%;
    transform:translateX(-50%);
    width:95%;
    max-width:520px;
    background:#1a1a1c;
    border-radius:30px;
    padding:12px;
    border:1px solid #2d2d2f;
}

.row{
    display:flex;
    align-items:center;
    gap:10px;
}

.icon{
    cursor:pointer;
    font-size:20px;
    padding:6px 10px;
}

.input{
    flex:1;
    background:transparent;
    border:none;
    color:white;
    font-size:16px;
    outline:none;
}

.popup{
    background:#f0f2f5;
    color:black;
    border-radius:18px;
    padding:15px;
    margin-bottom:10px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:12px;
    text-align:center;
}

.mode-btn{
    padding:8px;
    border-radius:10px;
    margin-bottom:8px;
    background:#e4e6eb;
    cursor:pointer;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h2 style='text-align:center;'>Astra GPT</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;opacity:0.6;'>AI by Mohammad Sartaj</p>", unsafe_allow_html=True)

# ---------------- PLUS POPUP ----------------
if st.session_state.show_plus:
    st.markdown("""
    <div class="popup">
        <div class="grid">
            📷 Camera
            🖼 Gallery
            📎 Files
            ☁️ Drive
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- DASHBOARD POPUP ----------------
if st.session_state.show_dashboard:
    st.markdown("""
    <div class="popup">
        ⚡ Fast Reply<br><br>
        🔍 Research<br><br>
        🎨 Create Image
    </div>
    """, unsafe_allow_html=True)

# ---------------- INPUT ----------------
query = st.text_input("", placeholder="Ask Bharat Astra GPT...")

# ---------------- SEND BUTTON LOGIC ----------------
if st.button("Send"):
    if query:
        if st.session_state.mode == "fast":
            st.success("⚡ Fast Reply")
            st.write(query)

        elif st.session_state.mode == "research":
            st.success("🔍 Research Mode")
            st.write("Detailed research on:", query)

        elif st.session_state.mode == "image":
            st.success("🎨 Image Generation")
            st.write("Image prompt:", query)

# ---------------- BOTTOM BAR ----------------
st.markdown("""
<div class="bottom-bar">
  <div class="row">
    <span class="icon">＋</span>
    <span class="icon">☰</span>
    <input class="input" placeholder="Ask Bharat Astra GPT...">
    <span class="icon">🎤</span>
    <span class="icon">➤</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------- CONTROLS ----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Attach"):
        st.session_state.show_plus = not st.session_state.show_plus
        st.session_state.show_dashboard = False
        st.rerun()

with col2:
    if st.button("☰ Dashboard"):
        st.session_state.show_dashboard = not st.session_state.show_dashboard
        st.session_state.show_plus = False
        st.rerun()
