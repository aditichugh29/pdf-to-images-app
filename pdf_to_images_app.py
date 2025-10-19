import streamlit as st
from pdf2image import convert_from_bytes
import os

st.title("📄 PDF to Images Converter")

pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
folder_path = st.text_input("Enter folder path to save images (leave blank for default)")

if st.button("Convert PDF to Images"):
    if pdf_file is None:
        st.error("❌ Please upload a PDF file first.")
    else:
        if folder_path.strip() == "":
            folder_path = os.path.join(os.getcwd(), "PDF_Pages")
        os.makedirs(folder_path, exist_ok=True)
        
        try:
            pages = convert_from_bytes(pdf_file.read())
            
            for i, page in enumerate(pages):
                image_path = os.path.join(folder_path, f"page_{i+1}.png")
                page.save(image_path, "PNG")
            
            st.success(f"✅ PDF converted! {len(pages)} images saved in {folder_path}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
