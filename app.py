import streamlit as st

# Mohammad Sartaj's Astra GPT - Advanced UI
st.set_page_config(page_title="Astra GPT", layout="wide")

# State Management
if "plus_open" not in st.session_state: st.session_state.plus_open = False
if "dash_open" not in st.session_state: st.session_state.dash_open = False
if "messages" not in st.session_state: st.session_state.messages = []

# --- CSS: FIXED PREMIUM INTERFACE ---
st.markdown("""
<style>
    .stApp { background-color: #0d0d0f; color: white; }
    header, footer, .stSidebar { visibility: hidden; }

    /* Main Floating Container */
    .main-footer-container {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 95%;
        max-width: 500px;
        background: #1a1a1c;
        border-radius: 25px;
        padding: 10px;
        border: 1px solid #2d2d2f;
        z-index: 9999;
    }

    /* Input Box Inside Container */
    .stTextInput input {
        background: #252527 !important;
        border: none !important;
        color: white !important;
        border-radius: 15px !important;
        padding: 12px !important;
    }

    /* Plus Pop-up (Camera/Gallery) */
    .attachment-card {
        position: absolute;
        bottom: 120%;
        left: 0;
        width: 100%;
        background: #ffffff;
        border-radius: 20px;
        padding: 15px;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
        animation: slideUp 0.3s ease-out;
    }

    /* Dashboard Pop-up */
    .dashboard-card {
        position: absolute;
        bottom: 120%;
        right: 0;
        width: 220px;
        background: rgba(30, 30, 32, 0.98);
        border: 1px solid #3d3d3f;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
        animation: fadeIn 0.3s ease;
    }

    @keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    .menu-item { text-align: center; color: #333; font-size: 11px; font-weight: bold; }
    .circle-icon { background: #f0f2f5; width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 5px; font-size: 18px; }
    
    .dash-btn { color: #d1d1d1; padding: 10px; border-radius: 8px; display: flex; align-items: center; gap: 10px; font-size: 14px; cursor: pointer; }
    .dash-btn:hover { background: #2d2d2f; color: white; }
</style>
""", unsafe_allow_html=True)

# --- CHAT DISPLAY ---
st.markdown("<h4 style='text-align:center; opacity:0.8;'>Astra GPT</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:12px; opacity:0.5; margin-top:-15px;'>AI by Mohammad Sartaj</p>", unsafe_allow_html=True)

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# --- THE DYNAMIC INTERFACE ---
st.markdown('<div class="main-footer-container">', unsafe_allow_html=True)

# 1. Plus Pop-up Card
if st.session_state.plus_open:
    st.markdown("""
    <div class="attachment-card">
        <div class="menu-item"><div class="circle-icon">📷</div>Camera</div>
        <div class="menu-item"><div class="circle-icon">🖼️</div>Gallery</div>
        <div class="menu-item"><div class="circle-icon">📎</div>Files</div>
        <div class="menu-item"><div class="circle-icon">☁️</div>Drive</div>
    </div>
    """, unsafe_allow_html=True)

# 2. Dashboard Pop-up Card
if st.session_state.dash_open:
    st.markdown("""
    <div class="dashboard-card">
        <div style="font-size:12px; margin-bottom:8px; opacity:0.6; padding-left:10px;">Dashboard ☰</div>
        <div class="dash-btn">🖼️ Create Images</div>
        <div class="dash-btn">🔍 Research</div>
        <div class="dash-btn">💡 Thinking</div>
        <div class="dash-btn">⚙️ Settings</div>
    </div>
    """, unsafe_allow_html=True)

# 3. Input & Send Area (Gemini Style)
col_text, col_send = st.columns([8.5, 1.5])
with col_text:
    user_input = st.text_input("", placeholder="Ask Bharat Astra GPT...", key="main_input", label_visibility="collapsed")
with col_send:
    if st.button("❯", key="send_logic"): 
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "assistant", "content": f"Astra AI (Sartaj): Processing '{user_input}'..."})
            st.session_state.plus_open = False
            st.session_state.dash_open = False
            st.rerun()

# 4. Bottom Icons Row
c1, c2, c3, c4 = st.columns([1, 1, 5, 1.5])
with c1:
    if st.button("＋", key="p_btn"):
        st.session_state.plus_open = not st.session_state.plus_open
        st.session_state.dash_open = False
        st.rerun()
with c2:
    if st.button("≡", key="d_btn"): # Dashboard Trigger
        st.session_state.dash_open = not st.session_state.dash_open
        st.session_state.plus_open = False
        st.rerun()
with c4:
    st.button("🎤", key="m_btn")

st.markdown('</div>', unsafe_allow_html=True)
