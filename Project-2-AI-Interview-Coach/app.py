import streamlit as st

st.title("AI Interview Coach")

st.write("Practice interviews and get AI feedback")

role = st.text_input("Enter your target role")

question = st.text_area("Enter your interview answer")

if st.button("Get Feedback"):
    st.success("AI feedback will appear here")
