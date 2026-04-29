from flask import Flask, render_template, request, session
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "moodapp123"
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def home():
    history = session.get("history", [])
    return render_template("index.html", history=history)

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

    history = session.get("history", [])
    history.insert(0, {"mood": mood, "platform": platform, "post": post})
    history = history[:5]
    session["history"] = history

    return render_template("index.html", post=post, mood=mood, platform=platform, history=history)

if __name__ == "__main__":
    app.run(debug=True)