from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Initialize Groq client using the key from .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Make a simple API call
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! What is AI?"}
    ]
)

# Print the response
print(completion.choices[0].message.content)

