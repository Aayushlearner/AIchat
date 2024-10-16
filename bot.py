import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from groq import Groq

st.title("welcome to chatbot")

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
prompt = st.text_input("Enter a prompt: ")

if st.button("Submit"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    st.write(chat_completion.choices[0].message.content)