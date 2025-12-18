import streamlit as st

# Mohammad Sartaj's AI Interface
def load_interface():
    st.markdown(
        """
        <style>
        /* Leonardo AI Style Background */
        .main {
            background-color: #0d0d0f;
        }
        
        /* Floating Rectangular Board */
        .bottom-board {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 90%;
            max-width: 500px;
            background-color: #1a1a1c;
            border-radius: 24px;
            padding: 15px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
            z-index: 1000;
            border: 1px solid #2d2d2f;
        }

        .icon-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .left-group, .right-group {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .icon-btn {
            background: none;
            border: none;
            color: white;
            cursor: pointer;
            font-size: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0.8;
        }

        .fast-btn {
            background: #2a2a2c;
            border: 1px solid #3d3d3f;
            border-radius: 20px;
            padding: 5px 15px;
            font-size: 14px;
            color: white;
        }

        /* Pop-up Menu */
        #menu-container {
            display: none;
            position: absolute;
            bottom: 70px;
            left: 10px;
            background: #1a1a1c;
            border: 1px solid #2d2d2f;
            border-radius: 15px;
            padding: 10px;
            width: 150px;
            box-shadow: 0px 5px 15px rgba(0,0,0,0.4);
        }

        .menu-item {
            padding: 8px;
            color: white;
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            font-size: 14px;
        }

        .menu-item:hover {
            background: #2d2d2f;
            border-radius: 8px;
        }
        </style>

        <div class="bottom-board">
            <div id="menu-container">
                <div class="menu-item">📷 Camera</div>
                <div class="menu-item">🖼️ Gallery</div>
                <div class="menu-item">📄 File</div>
                <div class="menu-item">☁️ Drive</div>
            </div>
            
            <div class="icon-row">
                <div class="left-group">
                    <button class="icon-btn" onclick="toggleMenu()">➕</button>
                    <button class="icon-btn">⚙️</button>
                </div>
                
                <div class="right-group">
                    <div class="fast-btn">Fast</div>
                    <button class="icon-btn">🎤</button>
                    <button class="icon-btn" style="background: #3d3d3f; border-radius: 50%; padding: 5px;">✨</button>
                </div>
            </div>
        </div>

        <script>
        function toggleMenu() {
            var x = document.getElementById("menu-container");
            if (x.style.display === "block") {
                x.style.display = "none";
            } else {
                x.style.display = "block";
            }
        }
        </script>
        """,
        unsafe_allow_html=True
    )

load_interface()
st.title("AstraGPT")
      
