import streamlit as st
from googletrans import Translator

trans = Translator()

st.header("🌐 AI Language Translator")

# User input text
text = st.text_area("Enter Text:")

# Target language dropdown (Hindi, English, Spanish, French)
target = st.selectbox("Select Target Language:", ["hi", "en", "es", "fr"])

if st.button("Translate"):
    if text.strip():
        res = trans.translate(text, dest=target)
        st.success(res.text)  # Output result
    else:
        st.warning("Please enter some text!")
        