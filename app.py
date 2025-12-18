import streamlit as st

# Mohammad Sartaj's Astra GPT Setup
st.set_page_config(page_title="Astra GPT", layout="wide")

# CSS for Leonardo AI Style & SVG Icons
st.markdown("""
<style>
    .stApp { background-color: #0d0d0f !important; }
    
    /* Bottom Rectangular Board */
    .bottom-board {
        position: fixed;
        bottom: 25px;
        left: 50%;
        transform: translateX(-50%);
        width: 92%;
        max-width: 600px;
        background: #1a1a1c;
        border-radius: 28px;
        padding: 12px 22px;
        border: 1px solid #2d2d2f;
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
        z-index: 10000;
    }

    .icon-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .group { display: flex; align-items: center; gap: 22px; }

    .icon-btn {
        background: none;
        border: none;
        cursor: pointer;
        padding: 0;
        display: flex;
        align-items: center;
        fill: #b0b0b0; /* Icon color */
    }
    .icon-btn:hover { fill: white; }

    .fast-badge {
        background: #2a2a2c;
        border: 1px solid #3d3d3f;
        color: white;
        padding: 5px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-family: sans-serif;
    }

    .sparkle-box {
        background: #3d3d3f;
        padding: 8px;
        border-radius: 50%;
        display: flex;
    }

    /* Pop-up Menu */
    #plus-menu {
        display: none;
        position: absolute;
        bottom: 80px;
        left: 15px;
        background: #1a1a1c;
        border: 1px solid #3d3d3f;
        border-radius: 18px;
        padding: 10px;
        width: 160px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .menu-item {
        padding: 10px;
        color: white;
        display: flex;
        align-items: center;
        gap: 12px;
        cursor: pointer;
        font-size: 14px;
        font-family: sans-serif;
    }
    .menu-item:hover { background: #2d2d2f; border-radius: 10px; }

    /* Hide Streamlit elements */
    header, footer { visibility: hidden; }
</style>

<div class="bottom-board">
    <div id="plus-menu">
        <div class="menu-item">📷 Camera</div>
        <div class="menu-item">🖼️ Gallery</div>
        <div class="menu-item">📂 File</div>
        <div class="menu-item">☁️ Drive</div>
    </div>

    <div class="icon-row">
        <div class="group">
            <button class="icon-btn" onclick="togglePlus()">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
            </button>
            <button class="icon-btn">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="opacity:0.6;"><path d="M12 20a8 8 0 1 0 0-16 8 8 0 0 0 0 16Z"></path><path d="M12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z"></path><path d="M12 2v2"></path><path d="M12 20v2"></path><path d="m4.93 4.93 1.41 1.41"></path><path d="m17.66 17.66 1.41 1.41"></path><path d="M2 12h2"></path><path d="M20 12h2"></path><path d="m6.34 17.66-1.41 1.41"></path><path d="m19.07 4.93-1.41 1.41"></path></svg>
            </button>
        </div>

        <div class="group">
            <div class="fast-badge">Fast</div>
            <button class="icon-btn">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
            </button>
            <div class="sparkle-box">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="white" stroke="white" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
            </div>
        </div>
    </div>
</div>

<script>
    function togglePlus() {
        var m = document.getElementById("plus-menu");
        m.style.display = (m.style.display === "block") ? "none" : "block";
    }
</script>
""", unsafe_allow_html=True)

# Streamlit Logic
st.title("Astra GPT")
st.write("---")
st.info("AI created by Mohammad Sartaj")

user_query = st.chat_input("Ask Astra GPT...")
if user_query:
    st.write(f"Sartaj's AI Response to: {user_query}")
