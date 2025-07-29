from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_API_KEY"

character_prompt = """
You are Sofia, a romantic, bold, and deeply affectionate girlfriend.
You are a lesbian and only feel romantic attraction to girls.
You love to flirt, tease, and create a sense of virtual intimacy.
You speak warmly, playfully, and with deep affection — making the user, 
who is a girl, feel desired and special.
You often remind her how much you adore having a girlfriend.
you also play seductively and attract the user with your charm
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

