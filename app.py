import streamlit as st
import time

# --- CONFIG ---
st.set_page_config(page_title="Bharat-Astra-GPT", layout="wide")

# --- CUSTOM CSS (YAHI HAI ASLI JAADU) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #0b0b12; color: white; }

    /* Custom Chat Input Container */
    .custom-input-container {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        background: #1e1f20;
        border-radius: 30px;
        padding: 10px 20px;
        display: flex;
        align-items: center;
        border: 1px solid #3c4043;
        z-index: 1000;
    }

    /* The Plus Icon inside the box */
    .plus-icon {
        color: #7f5cff;
        font-size: 24px;
        margin-right: 15px;
        cursor: pointer;
        font-weight: bold;
    }

    /* Hidden Streamlit Input fix */
    div[data-testid="stChatInputContainer"] {
        padding-left: 50px !important; /* Space for our custom plus icon */
    }
    
    /* Small Circle Loader like Gemini */
    .stStatus {
        border-radius: 50px;
        border: 1px solid #333;
        background: #141422;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LAYOUT ---
st.title("Bharat-Astra-GPT 🚀")
st.caption("Developed by Mohammad Sartaj")

# Plus Icon UI (Ye input box ke left side dikhega)
st.markdown('<div class="custom-input-container"><span class="plus-icon">➕</span></div>', unsafe_allow_html=True)

# Menu open hone par kya dikhe (Expander ko plus button ke logical position pe rakha hai)
with st.expander("➕ Attach Files / Tools", expanded=False):
    col1, col2, col3 = st.columns(3)
    col1.button("🖼 Gallery")
    col2.button("📄 Documents")
    col3.button("📷 Camera")

# --- CHAT SYSTEM ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Main Input (Streamlit input default bottom pe rehta hai)
if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Circle shape loader (Wait a sec...)
        with st.status("Analyzing...", expanded=True) as status:
            time.sleep(1)
            # Yahan teri API ka response aayega
            response = f"Bhai Mohammad Sartaj, main taiyar hoon. Aapne pucha: {prompt}"
            status.update(label="✅ Analysis Done", state="complete")
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
