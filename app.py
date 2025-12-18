import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# ================= CONFIG & SECURITY =================
st.set_page_config(page_title="Bharat Astra GPT", page_icon="✨", layout="wide")

# Basic Security: Prevent clickjacking and hide streamlit branding
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    /* Privacy Shield */
    .reportview-container { background: #0d0d0f; }
    </style>
""", unsafe_allow_html=True)

# ================= STATE MANAGEMENT =================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "plus_menu" not in st.session_state:
    st.session_state.plus_menu = False
if "dash_menu" not in st.session_state:
    st.session_state.dash_menu = False

# ================= PREMIUM UI CSS =================
st.markdown("""
<style>
    .stApp { background-color: #0d0d0f; color: white; }
    
    /* Floating Bottom Board */
    .fixed-footer {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 95%;
        max-width: 600px;
        background: #1a1a1c;
        border-radius: 30px;
        padding: 15px 20px;
        border: 1px solid #2d2d2f;
        box-shadow: 0 10px 40px rgba(0,0,0,0.7);
        z-index: 999;
    }

    /* Input Box Gemini Style */
    .input-wrapper {
        background: #252527;
        border-radius: 20px;
        display: flex;
        align-items: center;
        padding: 5px 15px;
        margin-bottom: 15px;
        border: 1px solid #3d3d3f;
    }
    
    /* Plus Pop-up (Camera/Gallery) */
    .pop-card {
        background: #ffffff;
        border-radius: 25px;
        padding: 25px;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        position: absolute;
        bottom: 160px;
        width: 100%;
        left: 0;
        animation: slideUp 0.3s ease-out;
        box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
    }

    /* Dashboard Pop-up (Equal-to/3-line) */
    .dash-card {
        background: #1a1a1c;
        border: 1px solid #3d3d3f;
        border-radius: 20px;
        padding: 15px;
        position: absolute;
        bottom: 85px;
        left: 60px;
        width: 200px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        animation: fadeIn 0.2s ease;
    }

    @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    .menu-item { color: #1c1e21; text-align: center; font-size: 12px; font-weight: 600; cursor: pointer; }
    .icon-circle { background: #e4e6eb; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 5px; font-size: 22px; }
    
    .dash-link { color: #d1d1d1; padding: 10px; border-radius: 10px; cursor: pointer; display: flex; align-items: center; gap: 10px; }
    .dash-link:hover { background: #2d2d2f; color: white; }

    /* Hide Streamlit components */
    .stButton button { background: transparent; border: none; color: white; padding: 0; }
    .stButton button:hover { color: #fff; background: transparent; }
</style>
""", unsafe_allow_html=True)

# ================= MAIN CHAT AREA =================
st.markdown(f"<h3 style='text-align:center; color:#888;'>Astra GPT</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#555; margin-top:-15px;'>AI by Mohammad Sartaj</p>", unsafe_allow_html=True)

# Scrollable Chat
chat_container = st.container()
with chat_container:
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

# ================= DYNAMIC MENUS =================

# 1. Dashboard Menu (Research, Thinking, etc.)
if st.session_state.dash_menu:
    st.markdown("""
    <div class="fixed-footer" style="background:transparent; border:none; box-shadow:none;">
        <div class="dash-card">
            <div class="dash-link">🎨 Create Image</div>
            <div class="dash-link">🔍 Research</div>
            <div class="dash-link">💡 Thinking</div>
            <div class="dash-link">⚙️ Settings</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 2. Plus Menu (Camera, Gallery, etc.)
if st.session_state.plus_menu:
    st.markdown("""
    <div class="fixed-footer" style="background:transparent; border:none; box-shadow:none;">
        <div class="pop-card">
            <div class="menu-item"><div class="icon-circle">📷</div>Camera</div>
            <div class="menu-item"><div class="icon-circle">🖼️</div>Gallery</div>
            <div class="menu-item"><div class="icon-circle">📎</div>Files</div>
            <div class="menu-item"><div class="icon-circle">☁️</div>Drive</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER BOARD =================
st.markdown('<div class="fixed-footer">', unsafe_allow_html=True)

# Part A: Input Box & Send
with st.container():
    c_in, c_send = st.columns([9, 1])
    with c_in:
        user_input = st.text_input("", placeholder="Ask Bharat Astra GPT...", key="main_input", label_visibility="collapsed")
    with c_send:
        if st.button("➤", key="send_btn_real"):
            if user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                # AI Logic Placeholder
                st.session_state.messages.append({"role": "assistant", "content": f"Sartaj's Astra AI: I am processing your request: {user_input}"})
                st.session_state.plus_menu = False
                st.session_state.dash_menu = False
                st.rerun()

# Part B: Icons Row
b1, b2, b3, b4, b5 = st.columns([1, 1, 4, 1, 1])
with b1:
    if st.button("＋", key="p_btn"):
        st.session_state.plus_menu = not st.session_state.plus_menu
        st.session_state.dash_menu = False
        st.rerun()
with b2:
    # 3-line Dashboard Toggle
    if st.button("≡", key="d_btn"):
        st.session_state.dash_menu = not st.session_state.dash_menu
        st.session_state.plus_menu = False
        st.rerun()
with b4:
    st.button("🎤", key="m_btn")
with b5:
    st.markdown("<div style='background:#3d3d3f; padding:5px; border-radius:50%; text-align:center;'>✨</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
