from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from models import Car, session


load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/exchange", methods=["GET", "POST"])
def exchange():
    if request.method == "POST":
        url = f"https://{os.getenv('API_HOST_RAPID')}/exchange"
        from_value = request.form["from"]
        to_value = request.form["to"]
        count = request.form["count"]
        querystring = {"from": from_value, "to": to_value}
        headers = {
            "X-RapidAPI-Key": os.getenv("API_KEY_RAPID"),
            "X-RapidAPI-Host": os.getenv("API_HOST_RAPID")
        }
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        result = data * int(count)
        return render_template("exchange.html", result=result)
    else:
        return render_template("exchange.html")


if __name__ == "__main__":
    app.run(debug=True)
