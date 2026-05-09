from flask import Flask, render_template, request

app = Flask(__name__)

# Scam keywords
scam_keywords = [
    "otp",
    "bank account",
    "urgent",
    "click link",
    "win money",
    "lottery",
    "free offer",
    "verify account"
]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    risk = ""

    if request.method == "POST":
        message = request.form["message"].lower()

        score = 0

        for word in scam_keywords:
            if word in message:
                score += 1

        if score >= 2:
            result = "⚠ Scam Alert Detected!"
            risk = "High Risk"
        elif score == 1:
            result = "⚠ Suspicious Message"
            risk = "Medium Risk"
        else:
            result = "✅ Safe Message"
            risk = "Low Risk"

    return render_template("index.html", result=result, risk=risk)

if __name__ == "__main__":
    app.run(debug=True)