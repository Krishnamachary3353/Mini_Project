import streamlit as st
import ollama

def get_output(question):
    # Use Ollama's chat endpoint to query Mistral 7B
    response = ollama.chat(
        model="mistral", 
        messages=[{"role": "user", "content": question}]
    )
    return response['message']['content']

st.title("EduGenius Chatbot using Mistral (Ollama)")

user_input = st.text_input("Enter your question or text:")
if st.button("Generate Response"):
    result = get_output(user_input)
    st.write(result)
