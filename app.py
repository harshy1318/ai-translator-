import streamlit as st
from deep_translator import GoogleTranslator
from PIL import Image
import pytesseract
import easyocr

st.set_page_config(page_title="AI Translator", page_icon="🌐")
st.title("🌐 AI Language Translator")

# Select mode
mode = st.selectbox("Choose translation mode", ["Text", "Image"])

# Language selection
target_lang = st.selectbox("Translate to:", ["hi","ur","ru","fr","es","de","ja","zh-CN","it","fa","bn"])
source_lang = "en"  # English as source

if mode == "Text":
    text = st.text_input("Enter text:")
    if text:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        st.write("Translated:", translated)

else:  # Image mode
    uploaded_file = st.file_uploader("Upload an image")
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        
        # OCR using pytesseract
        ocr_text = pytesseract.image_to_string(img)
        st.write("Detected text:", ocr_text)
        
        # Translate detected text
        if ocr_text.strip():
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(ocr_text)
            st.write("Translated:", translated)
