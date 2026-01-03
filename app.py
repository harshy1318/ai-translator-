import streamlit as st
from googletrans import Translator

# ================= PAGE SETUP =================
st.set_page_config(page_title="Universal Translator", page_icon="🌐", layout="centered")
st.markdown("<h1 style='text-align:center;color:#1A237E;'>🌐 Universal Translator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Translate English ↔ Ancient Scripts & Modern Languages & Morse Code</p>", unsafe_allow_html=True)

translator = Translator()

# ================= ANCIENT SCRIPTS =================
brahmi_cons = {
    "k":"𑀓","g":"𑀕","c":"𑀘","j":"𑀚",
    "t":"𑀢","d":"𑀤","n":"𑀦",
    "p":"𑀧","m":"𑀫","y":"𑀬",
    "r":"𑀭","l":"𑀮","v":"𑀯",
    "s":"𑀲","h":"𑀳"
}
brahmi_ind_vowels = {"a":"𑀅","aa":"𑀆","i":"𑀇","ii":"𑀈","u":"𑀉","uu":"𑀊","e":"𑀏","o":"𑀑"}
brahmi_dep_vowels = {"a":"","aa":"𑀸","i":"𑀺","ii":"𑀻","u":"𑀼","uu":"𑀽","e":"𑀾","o":"𑁀"}
brahmi_rev = {v:k for k,v in brahmi_cons.items()}
brahmi_rev.update({v:k for k,v in brahmi_ind_vowels.items()})

tamil = {"a":"அ","i":"இ","u":"உ","e":"எ","o":"ஒ",
         "k":"க","t":"த","n":"ந","p":"ப","m":"ம",
         "y":"ய","r":"ர","l":"ல","v":"வ","s":"ஸ","h":"ஹ"}
tamil_rev = {v:k for k,v in tamil.items()}

hebrew = {"a":"א","b":"ב","g":"ג","d":"ד","h":"ה","k":"כ","l":"ל","m":"מ","n":"נ","r":"ר","s":"ש","t":"ת","y":"י","v":"ו"}
hebrew_rev = {v:k for k,v in hebrew.items()}

aramaic = {"a":"𐡀","b":"𐡁","g":"𐡂","d":"𐡃","h":"𐡄","k":"𐡊","l":"𐡋","m":"𐡌","n":"𐡍","r":"𐡓","s":"𐡔","t":"𐡕"}
aramaic_rev = {v:k for k,v in aramaic.items()}

greek = {"a":"Α","b":"Β","g":"Γ","d":"Δ","e":"Ε","k":"Κ","l":"Λ","m":"Μ","n":"Ν","o":"Ο","p":"Π","r":"Ρ","s":"Σ","t":"Τ","u":"Υ"}
greek_rev = {v:k for k,v in greek.items()}

latin = {chr(i): chr(i).upper() for i in range(97,123)}
latin_rev = {v:k for k,v in latin.items()}

# ================= MORSE =================
MORSE = {
    'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....',
    'i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.',
    'q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',' ':'/'
}
REV_MORSE = {v:k for k,v in MORSE.items()}

# ================= HELPER FUNCTIONS =================
def english_to_brahmi(text):
    text = text.lower()
    i, out = 0, ""
    while i < len(text):
        if i+1 < len(text) and text[i:i+2] in brahmi_ind_vowels:
            out += brahmi_ind_vowels[text[i:i+2]]
            i += 2
        elif text[i] in brahmi_ind_vowels:
            out += brahmi_ind_vowels[text[i]]
            i += 1
        elif text[i] in brahmi_cons:
            cons = brahmi_cons[text[i]]
            vowel = ""
            if i+1 < len(text) and text[i+1] in brahmi_dep_vowels:
                vowel = brahmi_dep_vowels[text[i+1]]
                i += 1
            out += cons + vowel
            i += 1
        else:
            out += text[i]
            i += 1
    return out

def brahmi_to_english(text):
    return "".join(brahmi_rev.get(c, c) for c in text)

def to_script(text, mapping):
    return "".join(mapping.get(c.lower(), c) for c in text)

def from_script(text, rev_map):
    return "".join(rev_map.get(c, c) for c in text)

def english_to_morse(text):
    return " ".join(MORSE.get(c.lower(), c) for c in text)

def morse_to_english(code):
    return "".join(REV_MORSE.get(c,'') for c in code.split())

# ================= MODERN LANGUAGES =================
modern_languages = {
    "Hindi": "hi", "Urdu": "ur", "Russian": "ru", "French": "fr",
    "Spanish": "es", "German": "de", "Japanese": "ja", "Chinese": "zh-CN",
    "Italian": "it", "Persian": "fa", "Bengali": "bn"
}

def translate_text(text, dest_lang):
    try:
        result = translator.translate(text, dest=dest_lang)
        return result.text
    except:
        return "Translation Error"

# ================= UI =================
mode = st.selectbox(
    "Choose Translation Mode",
    ["English → All", "All → English", "English ↔ Morse"]
)
text = st.text_input("Enter text:")

if text:
    st.markdown("---")
    
    # ================= ANCIENT SCRIPTS =================
    if mode == "English → All":
        st.subheader("📝 Ancient Scripts")
        st.success("Brahmi: " + english_to_brahmi(text))
        st.success("Tamil: " + to_script(text, tamil))
        st.success("Hebrew: " + to_script(text, hebrew))
        st.success("Aramaic: " + to_script(text, aramaic))
        st.success("Greek: " + to_script(text, greek))
        st.success("Latin: " + to_script(text, latin))
        
        st.subheader("🌐 Modern Languages")
        for lang, code in modern_languages.items():
            st.success(f"{lang}: {translate_text(text, code)}")
    
    elif mode == "All → English":
        st.subheader("📝 Ancient Scripts → English")
        st.success("Brahmi: " + brahmi_to_english(text))
        st.success("Tamil: " + from_script(text, tamil_rev))
        st.success("Hebrew: " + from_script(text, hebrew_rev))
        st.success("Aramaic: " + from_script(text, aramaic_rev))
        st.success("Greek: " + from_script(text, greek_rev))
        st.success("Latin: " + from_script(text, latin_rev))
        
        st.subheader("🌐 Modern Languages → English")
        for lang, code in modern_languages.items():
            st.success(f"{lang} → English: {translate_text(text, 'en')}")
    
    else:
        sub = st.selectbox("Morse Mode", ["English → Morse", "Morse → English"])
        if sub == "English → Morse":
            st.success("📡 " + english_to_morse(text))
        else:
            st.success("🔤 " + morse_to_english(text))
