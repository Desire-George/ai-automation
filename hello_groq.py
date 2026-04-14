

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

message = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "You are a cybersecurity analyst. A user just logged in from an unusual IP at 3am. Is this suspicious? Give a brief assessment."
        }
    ]
)

print(message.choices[0].message.content)
