import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.header("🤖 FAQ Chatbot")

# FAQ Database
faqs = {
    "What is CodeAlpha?": "CodeAlpha is an online platform providing virtual internships.",
    "What perks do interns get?": "Offer Letter, QR Verified Certificate, and Recommendation Letter.",
    "How do I submit tasks?": "Upload to GitHub, post a video on LinkedIn, and fill the Submission Form.",
    "What is the GitHub repository rule?": "Repository name must follow 'CodeAlpha_ProjectName' format."
}

# User query input
query = st.text_input("Ask a question about the internship:")

if st.button("Ask Bot"):
    if query.strip():
        q_list = list(faqs.keys())
        
        # Match question using Cosine Similarity
        vec = TfidfVectorizer().fit_transform(q_list + [query])
        scores = cosine_similarity(vec[-1], vec[:-1])[0]
        
        # Check if match score is greater than 30%
        if scores.max() > 0.3:
            st.info(faqs[q_list[scores.argmax()]])
        else:
            st.warning("Sorry, question not found in FAQs!")
    else:
        st.warning("Please type a question!")