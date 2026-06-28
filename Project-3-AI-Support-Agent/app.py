import streamlit as st

st.title("AI Customer Support Agent")

st.write(
    "Ask questions and get AI-powered support responses."
)

question = st.text_input("Customer Question")

if question:

    response = f"""
    AI Response:

    Thanks for your question:
    {question}

    This is a demo support agent.
    """

    st.write(response)
