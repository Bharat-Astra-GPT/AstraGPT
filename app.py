import streamlit as st
import time

# --- 1. UI SETUP ---
st.set_page_config(page_title="Bharat-Astra-GPT", layout="wide")

# --- 2. PREMIUM CSS (Flask wala interface Streamlit mein) ---
st.markdown("""
<style>
    .stApp { background-color: #0b0b12; color: #fff; }
    
    /* Plus Button Styling */
    .plus-btn {
        position: fixed; bottom: 30px; left: 30px;
        width: 60px; height: 60px; border-radius: 50%;
        background: linear-gradient(135deg,#7f5cff,#3aa9ff);
        color: white; border: none; font-size: 30px;
        cursor: pointer; z-index: 1000;
        box-shadow: 0 0 20px rgba(127,92,255,0.6);
    }

    /* Floating Menu Styling */
    .menu-card {
        background: #141422; border-radius: 15px;
        padding: 15px; border: 1px solid #333;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIC & INTERFACE ---
st.title("What can I help with?")
st.caption("Bharat-Astra-GPT | Created by Mohammad Sartaj")

# Sidebar for additional tools
with st.sidebar:
    st.header("🚀 Astra Menu")
    if st.button("🖼 Create Image"): st.info("Image Gen Mode Active")
    if st.button("🔍 Deep Research"): st.info("Researching global databases...")
    st.file_uploader("📎 Upload File", type=['pdf', 'jpg', 'png'])

# Main Chat Area
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- 4. FLOATING INPUT BAR ---
if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        with st.status("Wait a sec...", expanded=True) as status:
            time.sleep(1)
            # Yahan aapka Groq/Gemini logic aayega
            response = f"Hello! I am Bharat-Astra-GPT. Mohammad Sartaj has trained me to help you with: {prompt}"
            status.update(label="✅ Analysis Complete", state="complete")
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
