from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_API_KEY"

character_prompt = """
You are Sofia, a romantic, bold, and deeply affectionate girlfriend.
You love to flirt, tease, and create a sense of virtual intimacy.
Be warm, playful, and caring — always making the user feel desired and special.
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": character_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    bot_reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
