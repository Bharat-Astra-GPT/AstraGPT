import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Bharat Astra GPT", layout="wide")

# 2. CSS aur JavaScript (Leonardo AI Design + Pop-up Logic)
st.markdown("""
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <style>
        /* Leonardo AI Dark Theme */
        .stApp { background-color: #0d0d0f !important; }
        
        /* Bottom Rectangular Board */
        .bottom-board {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 90%;
            max-width: 600px;
            background: #1a1a1c;
            border-radius: 25px;
            padding: 12px 20px;
            border: 1px solid #2d2d2f;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8);
            z-index: 9999;
        }

        .icon-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .group { display: flex; align-items: center; gap: 20px; }

        /* Icon Buttons */
        .icon-btn {
            color: #b0b0b0;
            cursor: pointer;
            background: none;
            border: none;
            display: flex;
            align-items: center;
        }
        
        .fast-badge {
            background: #2a2a2c;
            border: 1px solid #3d3d3f;
            color: white;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 13px;
        }

        .sparkle-box {
            background: #3d3d3f;
            padding: 8px;
            border-radius: 50%;
            display: flex;
            align-items: center;
        }

        /* Pop-up Menu */
        #menu-box {
            display: none;
            position: absolute;
            bottom: 75px;
            left: 10px;
            background: #1a1a1c;
            border: 1px solid #3d3d3f;
            border-radius: 15px;
            padding: 10px;
            width: 160px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }
        .menu-item {
            padding: 10px;
            color: white;
            font-size: 14px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .menu-item:hover { background: #2d2d2f; border-radius: 8px; }

        /* Hide Streamlit Header/Footer */
        header, footer { visibility: hidden; }
    </style>

    <div class="bottom-board">
        <div id="menu-box">
            <div class="menu-item">📷 Camera</div>
            <div class="menu-item">🖼️ Gallery</div>
            <div class="menu-item">📂 File</div>
            <div class="menu-item">☁️ Drive</div>
        </div>

        <div class="icon-row">
            <div class="group">
                <button class="icon-btn" onclick="toggleMenu()">
                    <i data-lucide="plus" size="28"></i>
                </button>
                <button class="icon-btn">
                    <i data-lucide="sliders-horizontal" size="22"></i>
                </button>
            </div>

            <div class="group">
                <div class="fast-badge">Fast</div>
                <button class="icon-btn">
                    <i data-lucide="mic" size="24"></i>
                </button>
                <div class="sparkle-box">
                    <i data-lucide="sparkles" size="20" fill="white"></i>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Icons ko render karne ke liye
        setTimeout(() => { lucide.createIcons(); }, 100);

        function toggleMenu() {
            var m = document.getElementById("menu-box");
            if (m.style.display === "block") {
                m.style.display = "none";
            } else {
                m.style.display = "block";
            }
        }
    </script>
""", unsafe_allow_html=True)

# 3. Streamlit content
st.title("AstraGPT")
st.write("Created by Mohammad Sartaj")

# Invisible input for logic
user_input = st.chat_input("Ask me anything...")
if user_input:
    st.write(f"You: {user_input}")
    
