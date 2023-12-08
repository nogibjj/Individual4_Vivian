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


@app.route("/team")
def team():
    selected = request.args.get("selectedOption")
    ## TODO call OpenAI API, get a introduction
    prompt = f"give me a short introduction for {selected}"
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
    rslt = response.choices[0].message["content"]
    return render_template("result.html", selected=selected, intro=rslt)


def a():
    assert 1 == 1


if __name__ == "__main__":
    app.run(port=8000)
