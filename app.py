
import streamlit as st
import requests

st.title("Deep Infra API Demo")

model_name = st.text_input("Enter the name of the model you want to use:")
input_text = st.text_input("Enter the input text:")

if st.button("Submit"):
    url = f"https://api.deepinfra.com/v1/inference/{model_name}"
    data = {"input": input_text}
    response = requests.post(url, json=data)
    output = response.json()["output"]
    st.write(f"Output: {output}")

