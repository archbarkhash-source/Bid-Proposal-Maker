import streamlit as st
import os
from utils import parse_file, generate_proposal, export_to_word
import dotenv

# Load environment variables
dotenv.load_dotenv()

st.set_page_config(page_title="Bid Proposal Maker", page_icon="📑")
st.title("📑 Bid Proposal Maker")
st.caption("Upload solicitation files → generate proposal sections → export to Word")

# File upload
uploaded_file = st.file_uploader("Upload PDF or Word file", type=["pdf", "docx"])

if uploaded_file:
    # Save uploaded file
    templates_dir = os.path.join(os.getcwd(), "templates")
    os.makedirs(templates_dir, exist_ok=True)
    file_path = os.path.join(templates_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File uploaded: {uploaded_file.name}")

    # Parse file
    parsed_text = parse_file(file_path)
    st.text_area("Parsed Content", parsed_text, height=300)

    # Prompt selection for AI generation
    st.subheader("Select Proposal Section to Generate")
    prompt_options = [
        "Draft Cover Letter",
        "Draft Technical Proposal and Approach",
        "Add Construction Project Schedule",
        "Add Past Performance",
        "Add Safety Plan",
        "Add QA/QC Plan"
    ]
    selected_prompt = st.selectbox("Choose Section", prompt_options)

    # Generate proposal section
    if st.button("Generate Section"):
        proposal_text = generate_proposal(parsed_text, selected_prompt)
        st.text_area("AI Proposal Output", proposal_text, height=400)

    # Export to Word
    if st.button("Export to Word"):
        word_file = export_to_word(proposal_text)
        st.success(f"Proposal exported: {word_file}")

