import streamlit as st
from deep_translator import GoogleTranslator

# ------------------ PAGE SETUP ------------------
st.set_page_config(page_title="AI Language Translator", page_icon="🌐")
st.title("🌐 AI Language Translator")
st.markdown("""
Translate English text to multiple languages and vice versa:
- Hindi, Urdu, Russian, French, Spanish, German, Japanese, Chinese, Italian, Persian, Bengali
""")

# ------------------ LANGUAGE OPTIONS ------------------
languages = {
    "Hindi": "hi",
    "Urdu": "ur",
    "Russian": "ru",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Italian": "it",
    "Persian": "fa",
    "Bengali": "bn"
}

mode = st.radio("Choose translation mode:", ["English → Other Language", "Other Language → English"])
source_text = st.text_area("Enter your text here:")

if source_text.strip():
    st.subheader("Translations:")
    if mode == "English → Other Language":
        for lang_name, lang_code in languages.items():
            try:
                translated = GoogleTranslator(source='en', target=lang_code).translate(source_text)
                st.markdown(f"**{lang_name}:** {translated}")
            except Exception as e:
                st.markdown(f"**{lang_name}:** ❌ Error")
    else:  # Other Language → English
        for lang_name, lang_code in languages.items():
            try:
                translated = GoogleTranslator(source=lang_code, target='en').translate(source_text)
                st.markdown(f"**{lang_name} → English:** {translated}")
            except Exception as e:
                st.markdown(f"**{lang_name} → English:** ❌ Error")
