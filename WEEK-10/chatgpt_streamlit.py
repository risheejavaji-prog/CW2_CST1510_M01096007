import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Initialize Groq client using the key from .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Streamlit app UI
st.title("Groq Chatbot ")
st.write("Choose a domain and ask me anything!")

# Dropdown menu for domain selection
domain = st.selectbox(
    "Select a domain:",
    ["General", "Cybersecurity", "Data Science", "IT"]
)

# Map domain to system prompt
if domain == "Cybersecurity":
    system_prompt = "You are a cybersecurity expert who explains threats, defenses, and best practices."
elif domain == "Data Science":
    system_prompt = "You are a data science mentor who explains ML, statistics, and data analysis clearly."
elif domain == "IT":
    system_prompt = "You are an IT support specialist who helps with troubleshooting and system administration."
else:
    system_prompt = "You are a helpful assistant."

# Input box for user query
user_input = st.text_input("You:", "")

if user_input:
    # Make a chat completion request
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    # Display the assistant's reply
    st.write("Assistant:", completion.choices[0].message.content)
