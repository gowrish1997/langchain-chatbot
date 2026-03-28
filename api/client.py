import requests
import streamlit as st

def get_response(user_input):
    response = requests.post("http://localhost:8000/essay/invoke", json={"input": {"topic": user_input}})
    if response.status_code == 200:
        return response.json()["output"]['content']
    else:
        return f"Error: {response.status_code}"


st.title("LangServe Essay Generator")
user_input = st.text_input("Enter a topic for the essay:")
if st.button("Generate Essay"):
    essay = get_response(user_input)
    st.write(essay)