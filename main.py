from flask import Flask, render_template

app = Flask(__name__)

#routing home page
@app.route("/")
def home():
  return render_template()