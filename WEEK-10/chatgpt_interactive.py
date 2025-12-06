from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Initialize Groq client using the key from .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Welcome to the interactive chatbot! Type 'exit' to quit.\n")

while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Make a chat completion request
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    # Print the assistant's reply
    print("Assistant:", completion.choices[0].message.content)
