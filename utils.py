import os
from docx import Document

def parse_file(file_path):
    # Replace with actual PyMuPDF or python-docx parsing
    return f"Parsing done for file: {os.path.basename(file_path)}"

def generate_proposal(parsed_text, prompt):
    """
    AI generation with prompt.
    Replace this with Google Generative AI integration.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    # Example: pass parsed_text + prompt to AI
    return f"AI-generated '{prompt}' based on parsed text:\n\n{parsed_text}"

def export_to_word(proposal_text):
    templates_dir = os.path.join(os.getcwd(), "templates")
    os.makedirs(templates_dir, exist_ok=True)
    word_path = os.path.join(templates_dir, "generated_proposal.docx")
    doc = Document()
    doc.add_paragraph(proposal_text)
    doc.save(word_path)
    return word_path
