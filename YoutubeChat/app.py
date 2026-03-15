import streamlit as st
from youtube_utils import fetch_transcript
from rag_pipeline import build_rag

st.title("🎥 YouTube RAG Assistant")

with st.form("rag_form"):

    url = st.text_input("Enter YouTube URL")

    question = st.text_input("Enter your question")

    submit = st.form_submit_button("Generate Answer")

if submit:

    if not url.strip():
        st.warning("Please enter a YouTube URL")
        st.stop()

    if not question.strip():
        st.warning("Please enter a question")
        st.stop()

    with st.spinner("Processing video..."):

        transcript = fetch_transcript(url)

        rag_chain = build_rag(transcript)

        answer = rag_chain.invoke(question)

    st.write("### Answer")
    st.write(answer)