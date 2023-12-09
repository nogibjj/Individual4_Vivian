from flask import Flask, render_template, request
from dotenv import load_dotenv
import openai
import os

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submitTrip")
def team():
    dest = request.args.get("destination")
    numTravelers = request.args.get("numTravelers")
    duration = request.args.get("duration")
    ## TODO call OpenAI API, get a introduction
    prompt = (f"give me a 50-word travel plan for {numTravelers} people " 
              f"to {dest} for {duration} days.")
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
    rslt = response.choices[0].message["content"]
    return render_template("result.html", intro=rslt)


def a():
    assert 1 == 1


if __name__ == "__main__":
    app.run(port=8000)
