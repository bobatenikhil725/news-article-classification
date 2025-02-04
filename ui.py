import streamlit as st
import requests

st.title("Hello, Streamlit!")

name = st.text_input("Enter your name", "Guest")

if st.button("Submit"):
    response = requests.get(f"http://127.0.0.1:5000/about?name={name}")
    if response.status_code == 200:
        st.write(response.text)
    else:
        st.write(f"Failed to fetch data. Status code: {response.status_code}")

if st.button("Call Home API"):
    response = requests.get("http://127.0.0.1:5000/")
    if response.status_code == 200:
        st.write(response.text)
    else:
        st.write(f"Failed to fetch data. Status code: {response.status_code}")

         git config --global user.email "bobatenikhil725@gmail.com"
         git config --global user.name "bobatenikhil725"