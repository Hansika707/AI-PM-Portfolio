import streamlit as st

st.title("AI Study Assistant")

st.write("Upload notes and ask questions using AI")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    st.success("PDF uploaded successfully")
