from flask import Flask, render_template, request
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API key securely
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    mood = request.form["mood"]
    platform = request.form["platform"]

    prompt = f"I am feeling {mood} today. Generate a unique, creative and engaging social media post for {platform}. Make it genuine and relatable. Just give the post, nothing else."

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    post = response.choices[0].message.content
    return render_template("index.html", post=post, mood=mood, platform=platform)

if __name__ == "__main__":
    app.run(debug=True)