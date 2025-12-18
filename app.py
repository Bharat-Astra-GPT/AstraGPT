import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Bharat Astra GPT",
    page_icon="✨",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- LEONARDO AI STYLE UI (CSS) ----------------
st.markdown("""
<script src="https://unpkg.com/lucide@latest"></script>
<style>
    /* Main Background */
    .stApp {
        background-color: #0d0d0f !important;
    }

    /* Chat Messages Styling */
    .chat-box {
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        max-width: 80%;
    }
    .user-msg { background: #1a1a1c; border: 1px solid #2d2d2f; margin-left: auto; color: white; }
    .bot-msg { background: #262629; border: 1px solid #3d3d3f; color: #e5e7eb; }

    /* Floating Bottom Board (Fixed like Screenshot) */
    .bottom-container {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 700px;
        background: #1a1a1c;
        border-radius: 30px;
        padding: 12px 20px;
        border: 1px solid #2d2d2f;
        box-shadow: 0 10px 40px rgba(0,0,0,0.7);
        z-index: 1000;
    }

    .icon-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .group { display: flex; align-items: center; gap: 20px; }

    .icon-btn {
        color: #b0b0b0;
        cursor: pointer;
        transition: 0.2s;
        display: flex;
        align-items: center;
    }
    .icon-btn:hover { color: white; }

    .fast-badge {
        background: #2a2a2c;
        border: 1px solid #3d3d3f;
        color: white;
        padding: 4px 15px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 500;
    }

    .sparkle-icon {
        background: #3d3d3f;
        padding: 8px;
        border-radius: 50%;
        display: flex;
        align-items: center;
    }

    /* Pop-up Menu */
    #upload-menu {
        display: none;
        position: absolute;
        bottom: 80px;
        left: 10px;
        background: #1a1a1c;
        border: 1px solid #3d3d3f;
        border-radius: 20px;
        padding: 10px;
        width: 170px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .menu-item {
        padding: 10px;
        color: white;
        display: flex;
        align-items: center;
        gap: 10px;
        cursor: pointer;
        border-radius: 10px;
    }
    .menu-item:hover { background: #2d2d2f; }

    /* Hide Streamlit components that break design */
    #MainMenu, footer, header {visibility: hidden;}
</style>

<div class="bottom-container">
    <div id="upload-menu">
        <div class="menu-item">📸 Camera</div>
        <div class="menu-item">🖼️ Gallery</div>
        <div class="menu-item">📂 File</div>
        <div class="menu-item">☁️ Drive</div>
    </div>

    <div class="icon-row">
        <div class="group">
            <div class="icon-btn" onclick="toggleMenu()">
                <i data-lucide="plus" size="28"></i>
            </div>
            <div class="icon-btn">
                <i data-lucide="sliders-horizontal" size="22"></i>
            </div>
        </div>

        <div class="group">
            <div class="fast-badge">Fast</div>
            <div class="icon-btn">
                <i data-lucide="mic" size="24"></i>
            </div>
            <div class="sparkle-icon">
                <i data-lucide="sparkles" size="20" fill="white"></i>
            </div>
        </div>
    </div>
</div>

<script>
    lucide.createIcons();
    function toggleMenu() {
        var m = document.getElementById("upload-menu");
        m.style.display = (m.style.display === "block") ? "none" : "block";
    }
</script>
""", unsafe_allow_html=True)

# ---------------- CHAT INTERFACE ----------------
st.title("AstraGPT")
st.caption("Created by Mohammad Sartaj")

# Container for messages to keep them above the bottom bar
chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        div_class = "user-msg" if msg["role"] == "user" else "bot-msg"
        st.markdown(f'<div class="chat-box {div_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# ---------------- INPUT LOGIC ----------------
# Niche ka gap cover karne ke liye space
st.write("<br><br><br><br><br><br>", unsafe_allow_html=True)

with st.container():
    # Invisible input to handle chat
    query = st.chat_input("Ask Bharat Astra GPT...")
    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        # AI Response
        st.session_state.messages.append({"role": "assistant", "content": f"Astra AI: Recieved your message: {query}"})
        st.rerun()
