from flask import Flask, render_template

app = Flask(__name__)

#routing home page
@app.route("/")
def home():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/post")
def post():
  return render_template("post.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug=True)