from flask import Flask, render_template, request
from database import load_posts, insert_into_posts, load_jobs, insert_into_job, insert_into_contacts

# initilizing flask app
app = Flask(__name__)


#creating route for home page.
@app.route('/home')
@app.route("/")
def home():
  posts = load_posts()
  return render_template("index.html", posts=posts)


@app.route("/posts/form", methods=["POST", "GET"])
def post_form():
  if request.method == "POST":
    data = {
      "name": request.form.get("name"),
      "post_title": request.form.get("post_title"),
      "post": request.form.get("post"),
      "email": request.form.get("email")
    }
    insert_into_posts(data)
  return render_template("post_form.html")


#creating about page
@app.route("/about")
def about():
  return render_template("about.html")


#creating contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
  if request.method == "POST":
    data = {
      "name":request.form.get("name"),
      "email":request.form.get("email"),
      "phone":request.form.get("phone"),
      "message":request.form.get("message")
    }
  return render_template("contact.html")


@app.route("/jobs")
def home_jobs():
  jobs = load_jobs()
  return render_template("home_jobs.html", jobs=jobs)


@app.route("/jobs/form", methods=["GET", "POST"])
def jobs_form():
  if request.method == "POST":
    data = {
      "title": request.form.get('title'),
      "salary": request.form.get('salary'),
      "currency": request.form.get("currency"),
      "location": request.form.get("location"),
      "requirements": request.form.get("requirements"),
      "responsibility": request.form.get("responsibility")
    }
    insert_into_job(data)
  return render_template("job_form.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
#kajsdkfashdklfjshadlkfjhasdklfhatiuflkajsdfyqiwfbalkfgqvbqoi34tukdbjvfgaer tuedvn 