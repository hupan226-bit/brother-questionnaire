from flask import Flask, request
import json
import os

app = Flask(__name__)

BROTHER_PASSWORD = "banana123"
DATA_FILE = "answers.json"
def load_answers():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_answer(answer):
    answers = load_answers()
    answers.append(answer)

    with open(DATA_FILE, "w") as f:
        json.dump(answers, f, indent=2)
@app.route("/")
def home():
    return """
    <html>
    <body style="font-family:Arial;max-width:700px;margin:auto;padding:20px;">

    <h1>Questions For My Brother</h1>

    <a href="/login">
        <button>Start</button>
    </a>

    </body>
    </html>
    """

@app.route("/login")
def login():
    return """
    <html>
    <body style="font-family:Arial;max-width:700px;margin:auto;padding:20px;">

    <h1>Enter Password</h1>

    <form method="post" action="/check">

        <input type="password" name="password">

        <br><br>

        <button type="submit">Continue</button>

    </form>

    </body>
    </html>
    """

@app.route("/check", methods=["POST"])
def check():
    password = request.form["password"]

    if password == BROTHER_PASSWORD:
        return """
        <h1>Access Granted</h1>
        <p>Password is correct.</p>
        <a href='/questions'>Go to Questions</a>
        """
    else:
        return """
        <h1>Wrong Password</h1>
        <a href='/login'>Try Again</a>
        """

@app.route("/questions")
def questions():
    return """
    <html>
    <body style="font-family:Arial;max-width:800px;margin:auto;padding:20px;">

    <h1>Questions For My Brother</h1>

   <form method="post" action="/submit">

    <p>1. What is your favorite childhood memory?</p>
    <textarea name="q1" rows="4" cols="60"></textarea>

    <p>2. What is the best advice you've ever received?</p>
    <textarea name="q2" rows="4" cols="60"></textarea>

    <p>3. What achievement are you most proud of?</p>
    <textarea name="q3" rows="4" cols="60"></textarea>

    <p>4. If you could instantly learn one skill, what would it be?</p>
    <textarea name="q4" rows="4" cols="60"></textarea>

    <p>5. What is one thing you want people to remember about you?</p>
    <textarea name="q5" rows="4" cols="60"></textarea>

    <br><br>
   <button type="submit">
    Submit Answers
    </button>

    </form>

    </body>
    </html>
    """
@app.route("/submit", methods=["POST"])
def submit():

    answer = {
        "q1": request.form["q1"],
        "q2": request.form["q2"],
        "q3": request.form["q3"],
        "q4": request.form["q4"],
        "q5": request.form["q5"]
    }

    save_answer(answer)

    return """
    <h1>Thank You</h1>
    <p>Your answers have been received.</p>
    """
if __name__ == "__main__":
    app.run(debug=True)
