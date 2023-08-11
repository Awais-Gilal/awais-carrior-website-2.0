from flask import Flask, render_template
import json

app = Flask(__name__)

with open("templates/config/config.json") as f:
  JOBS = json.load(f)["JOBS"]


@app.route('/')
def index():
  return render_template('index.html')


@app.route("/about")
def about():
  return render_template('about.html')


@app.route("/contact")
def contact():
  return render_template("contact.html")


@app.route("/post")
def post():
  return render_template("post.html", jobs=JOBS)


app.run(host='0.0.0.0', port=81)
