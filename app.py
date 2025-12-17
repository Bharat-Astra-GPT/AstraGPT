import streamlit as st
from groq import Groq
import google.generativeai as genai
from fpdf import FPDF
import base64

# --- CONFIG ---
st.set_page_config(page_title="Bharat Astra Ultimate", layout="wide")

# Mohammad Sartaj Identity & Professor Mode
NCERT_PROMPT = "You are Bharat Astra Pro, created by Mohammad Sartaj. You are an expert teacher. Provide NCERT based notes, explain complex topics simply, and if asked for notes, format them clearly."

# --- PDF GENERATOR FUNCTION ---
def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=text)
    return pdf.output(dest="S").encode("latin-1")

# --- SIDEBAR ---
with st.sidebar:
    st.title("🚀 Astra Super-AI")
    st.info("Dev: Mohammad Sartaj")
    mode = st.radio("Select Mode", ["📚 NCERT & Study Notes", "🎨 4K Image Studio", "🎬 Video & Research"])

# --- MODE 1: STUDY & NOTES ---
if mode == "📚 NCERT & Study Notes":
    st.title("📖 NCERT Specialist & PDF Maker")
    query = st.text_area("Konsa topic padhna hai ya kiske notes chahiye?")
    
    if st.button("Generate Pro Notes"):
        with st.status("🤔 Astra Professor is Thinking...", expanded=True):
            genai.configure(api_key=st.secrets["GEMINI_KEY"])
            model = genai.GenerativeModel('gemini-1.5-pro')
            response = model.generate_content(NCERT_PROMPT + " " + query)
            notes_text = response.text
            st.markdown(notes_text)
            
            # PDF Download Option
            pdf_data = create_pdf(notes_text)
            st.download_button(label="📥 Download Notes as PDF", data=pdf_data, file_name="Astra_Notes.pdf", mime="application/pdf")

# --- MODE 2: 4K IMAGE STUDIO ---
elif mode == "🎨 4K Image Studio":
    st.title("🖼️ 4K Image Generator")
    prompt = st.text_input("Describe your 4K Masterpiece:")
    if st.button("Generate 4K"):
        # Using a high-res seed and upscale parameters
        url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=3840&height=2160&model=flux&nologo=true"
        st.image(url, caption="Bharat Astra 4K Generation")
        st.markdown(f"[🔗 Download Full 4K Image]({url})")

# --- MODE 3: VIDEO & RESEARCH ---
elif mode == "🎬 Video & Research":
    st.title("🎬 Video & Deep Research")
    # Video Logic (Redirecting to top-tier AI video engines)
    st.subheader("Text to Video (4K)")
    st.write("Current best 4K Video Engines (Open Access):")
    st.link_button("Luma Dream Machine (Free/Paid)", "https://lumalabs.ai/dream-machine")
    st.link_button("Runway Gen-3", "https://runwayml.com/")
    
