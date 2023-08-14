from flask import Flask, render_template, request
import json
from database import load_jobs

#getting datafrom json
#with open("templates/config/config.json") as f:
  #config_data = json.load(f)
  #JOBS = config_data["JOBS"]

#function for adding data in json
def save_in_dic(dic, name, email, phone, message):
  dic['contact'].append({
    "name": name,
    "email": email,
    "phone": phone,
    "message": message
  })
  
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route("/about")
def about():
  return render_template('about.html')


#route contact
@app.route("/contact", methods=["GET", "POST"])
def contact():

  if request.method == "POST":
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    msg = request.form.get("messaage")
  return render_template("contact.html")


@app.route("/post")
def post():
  JOBS = load_jobs()
  return render_template("post.html", jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
