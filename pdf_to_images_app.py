<<<<<<< HEAD
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
            poppler_path = os.path.join(os.getcwd(), "poppler")
            pages = convert_from_bytes(
                pdf_file.read(),
                poppler_path=poppler_path
            )
            
            for i, page in enumerate(pages):
                image_path = os.path.join(folder_path, f"page_{i+1}.png")
                page.save(image_path, "PNG")
            
            st.success(f"✅ PDF converted! {len(pages)} images saved in {folder_path}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
=======
import streamlit as st
from pdf2image import convert_from_bytes
import os

import streamlit as st
from pdf2image import convert_from_bytes
import os

st.title("📄 PDF to Images Converter")

pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
folder_path = st.text_input("Enter folder path to save images (e.g., C:\\Users\\aditi\\Documents\\PDF_Pages)")

if st.button("Convert PDF to Images"):
    if pdf_file is None:
        st.error("❌ Please upload a PDF file first.")
    elif folder_path.strip() == "":
        st.error("❌ Please enter a valid folder path.")
    else:
        os.makedirs(folder_path, exist_ok=True)
        try:
            pages = convert_from_bytes(
                pdf_file.read(),
                poppler_path=r"C:\Users\aditi\Downloads\Release-25.07.0-0\poppler-25.07.0\Library\bin"
            )
            for i, page in enumerate(pages):
                image_path = os.path.join(folder_path, f"page_{i+1}.png")
                page.save(image_path, "PNG")
            st.success(f"✅ PDF converted! {len(pages)} images saved in {folder_path}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
>>>>>>> 1e2746c8ff77ddb572e5b69ba5b45885fdc3650b
