from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Secure API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Welcome to Mood Post Generator!")
print("-" * 35)

mood = input("How are you feeling today? ")
platform = input("Which platform? (instagram / linkedin / twitter) ")

print("\n🤖 AI is generating your post...\n")

prompt = f"I am feeling {mood} today. Generate a unique, creative and engaging social media post for {platform}. Make it genuine and relatable. Just give the post, nothing else."

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("✨ Your AI Generated Post:")
print("-" * 35)
print(response.choices[0].message.content)
print("-" * 35)