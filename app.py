import streamlit as st

# Mohammad Sartaj's Astra GPT Setup
st.set_page_config(
    page_title="Bharat Astra GPT",
    page_icon="✨",
    layout="wide"
)

# ================= LEONARDO PREMIUM DARK UI =================
st.markdown("""
<style>
    /* Leonardo AI Deep Dark Background */
    .stApp {
        background-color: #0d0d0f !important;
        color: white;
    }

    /* Message Styling */
    .chat-container { padding-bottom: 150px; }
    .msg-box {
        padding: 15px 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        max-width: 85%;
        font-family: 'Inter', sans-serif;
    }
    .user-msg { background: #1a1a1c; border: 1px solid #2d2d2f; margin-left: auto; }
    .bot-msg { background: #0d0d0f; border: 1px solid #1a1a1c; margin-right: auto; color: #d1d1d1; }

    /* The Main Rectangular Board (Fixed at Bottom) */
    .bottom-board {
        position: fixed;
        bottom: 25px;
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

    .icon-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .group { display: flex; align-items: center; gap: 18px; }

    /* Button & Icon Styling */
    .icon-btn {
        background: none;
        border: none;
        cursor: pointer;
        color: #b0b0b0;
        display: flex;
        align-items: center;
        transition: 0.2s;
    }
    .icon-btn:hover { color: white; }

    .fast-badge {
        background: #2a2a2c;
        border: 1px solid #3d3d3f;
        color: #ffffff;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
    }

    .sparkle-btn {
        background: #3d3d3f;
        padding: 8px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Pop-up Menu Logic */
    .popup-menu {
        position: absolute;
        bottom: 80px;
        left: 10px;
        background: #1a1a1c;
        border: 1px solid #3d3d3f;
        border-radius: 20px;
        padding: 10px;
        width: 180px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .menu-item {
        padding: 10px 15px;
        color: white;
        font-size: 14px;
        border-radius: 12px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .menu-item:hover { background: #2d2d2f; }

    /* Hide Streamlit elements */
    header, footer, .stChatInputContainer { visibility: hidden; position: absolute; }
</style>
""", unsafe_allow_html=True)

# ================= SESSION STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "show_menu" not in st.session_state:
    st.session_state.show_menu = False

# ================= CHAT DISPLAY =================
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for m in st.session_state.messages:
    cls = "user-msg" if m["role"] == "user" else "bot-msg"
    st.markdown(f'<div class="msg-box {cls}">{m["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ================= BOTTOM INTERFACE =================

# 1. Pop-up Menu (Sirf tab dikhega jab Plus click ho)
if st.session_state.show_menu:
    st.markdown("""
    <div class="bottom-board" style="border:none; background:transparent; box-shadow:none;">
        <div class="popup-menu">
            <div class="menu-item">📷 Camera</div>
            <div class="menu-item">🖼️ Gallery</div>
            <div class="menu-item">📂 File</div>
            <div class="menu-item">☁️ Drive</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 2. Main Rectangular Board
with st.container():
    # Board UI with SVGs
    st.markdown(f"""
    <div class="bottom-board">
        <div class="icon-row">
            <div class="group">
                <div style="color:white; cursor:pointer;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></div>
                <div style="opacity:0.6;"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg></div>
            </div>
            <div class="group">
                <div class="fast-badge">Fast</div>
                <div style="color:white;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path></svg></div>
                <div class="sparkle-btn"><svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Invisible Streamlit Buttons (Taaki click kaam kare)
    cols = st.columns([0.8, 6.2, 1, 1, 1])
    with cols[0]:
        if st.button(" ", key="plus_btn", help="Toggle Menu"):
            st.session_state.show_menu = not st.session_state.show_menu
            st.rerun()
    with cols[1]:
        user_input = st.text_input("", placeholder="Ask Bharat Astra GPT...", label_visibility="collapsed")
    with cols[4]:
        if st.button("➤", key="send_btn"):
            if user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                st.session_state.messages.append({"role": "assistant", "content": f"Astra AI created by Mohammad Sartaj: Recieved your query '{user_input}'"})
                st.session_state.show_menu = False
                st.rerun()

# ================= INFO =================
st.sidebar.title("Astra GPT")
st.sidebar.info("Developer: Mohammad Sartaj")
    
