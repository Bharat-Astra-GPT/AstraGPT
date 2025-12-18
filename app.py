import streamlit as st

# Mohammad Sartaj's Astra GPT - Professional Setup
st.set_page_config(page_title="Bharat Astra GPT", layout="wide")

# State Management for Pop-ups
if "plus_open" not in st.session_state: st.session_state.plus_open = False
if "dash_open" not in st.session_state: st.session_state.dash_open = False
if "messages" not in st.session_state: st.session_state.messages = []

# --- CSS: DESIGN MEIN ROOH ---
st.markdown("""
<style>
    .stApp { background-color: #0d0d0f; color: white; }
    header, footer, .stSidebar { visibility: hidden; }

    /* Main Floating Container */
    .main-footer-container {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 92%;
        max-width: 700px;
        background: #1a1a1c;
        border-radius: 30px;
        padding: 10px 20px;
        border: 1px solid #2d2d2f;
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
        z-index: 9999;
    }

    /* Input Box Inside Container */
    .input-wrapper {
        display: flex;
        align-items: center;
        background: transparent;
        margin-bottom: 5px;
    }

    /* Icon Rows */
    .icon-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 5px;
        padding-top: 5px;
        border-top: 1px solid #2d2d2f;
    }
    
    .icon-group { display: flex; align-items: center; gap: 20px; }

    /* Plus Pop-up (The White Menu) */
    .attachment-card {
        position: absolute;
        bottom: 110%;
        left: 0;
        width: 100%;
        background: #ffffff;
        border-radius: 25px;
        padding: 20px;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
        animation: slideUp 0.3s ease-out;
    }

    /* Dashboard Pop-up (The Glassy Menu) */
    .dashboard-card {
        position: absolute;
        bottom: 110%;
        right: 0;
        width: 250px;
        background: rgba(30, 30, 32, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid #3d3d3f;
        border-radius: 20px;
        padding: 15px;
        box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
        animation: fadeIn 0.3s ease-out;
    }

    @keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    .menu-item { text-align: center; color: #333; font-size: 12px; font-weight: bold; cursor: pointer; }
    .circle-icon { background: #f0f2f5; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 5px; font-size: 20px; }
    
    .dash-btn { color: #d1d1d1; padding: 12px; border-radius: 10px; display: flex; align-items: center; gap: 10px; cursor: pointer; transition: 0.2s; }
    .dash-btn:hover { background: #2d2d2f; color: white; }

    /* Gemini Send Button Animation */
    .send-btn-active { color: #fff !important; cursor: pointer; }
</style>
""", unsafe_allow_html=True)

# --- CHAT INTERFACE ---
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
        <div style="font-size:14px; margin-bottom:10px; opacity:0.7;">Dashboard Dashboard ☰</div>
        <div class="dash-btn">🖼️ Create Images</div>
        <div class="dash-btn">🔍 Research</div>
        <div class="dash-btn">💡 Thinking</div>
        <div class="dash-btn">⚙️ Settings</div>
    </div>
    """, unsafe_allow_html=True)

# 3. Input & Send Area
col_text, col_send = st.columns([9, 1])
with col_text:
    user_input = st.text_input("", placeholder="Ask Bharat Astra GPT...", key="main_input", label_visibility="collapsed")
with col_send:
    if st.button("❯", key="send_logic"): # Gemini Style Send
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "assistant", "content": f"Sartaj's Astra AI processing: {user_input}"})
            st.session_state.plus_open = False
            st.session_state.dash_open = False
            st.rerun()

# 4. Bottom Icons Row
c1, c2, c3, c4 = st.columns([1, 1, 6, 1])
with c1:
    if st.button("＋", key="p_btn"):
        st.session_state.plus_open = not st.session_state.plus_open
        st.session_state.dash_open = False
        st.rerun()
with c2:
    if st.button("⚙️", key="s_btn"): # Setting icon as Dashboard trigger
        st.session_state.dash_open = not st.session_state.dash_open
        st.session_state.plus_open = False
        st.rerun()
with c4:
    st.button("🎤", key="m_btn")

st.markdown('</div>', unsafe_allow_html=True)
            
