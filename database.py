from sqlalchemy import create_engine, text
import datetime


#other functions
def month_str(value):
  month = int(value[1])
  if month == 1:
    return "January"
  elif month == 2:
    return "February"
  elif month == 3:
    return "March"
  elif month == 4:
    return "April"
  elif month == 5:
    return "May"
  elif month == 6:
    return "June"
  elif month == 7:
    return "July"
  elif month == 8:
    return "August"
  elif month == 9:
    return "September"
  elif month == 10:
    return "Octiber"
  elif month == 11:
    return "November"
  elif month == 12:
    return "December"
  else:
    return None


#connecting with database
username = "sql6639351"
password = "WCrfFr7VGg"
host = "sql6.freesqldatabase.com"
database_name = "sql6639351"
charset = "utf8mb4"

url = f"mysql+pymysql://{username}:{password}@{host}/{database_name}?charset={charset}"

engine = create_engine(url)


#=>loading data from database
#load jobs from database
def load_jobs():
  """loading jobs data form database and returning as list of dictingaries"""
  with engine.connect() as conn:
    data = conn.execute(text("SELECT * FROM job"))
    list_data = []
    for dic in data:
      list_data.append({
        "id": dic[0],
        "title": dic[1],
        "salary": dic[2],
        "currency": dic[3],
        "location": dic[4],
        "responsibility": dic[5],
        "requirements": dic[6]
      })
    return list_data


#liadimg contacts  from database
def load_contacts():
  """loading messages data form database and returning as list of dictingaries"""
  contact_list_data = []
  with engine.connect() as conn:
    contact_data = conn.execute(text("SELECT * FROM contact"))
    for dic in contact_data:
      contact_list_data.append({
        "sno": dic[0],
        "name": dic[1],
        "email": dic[2],
        "phone": dic[3],
        "msg": dic[4],
        "date": dic[5]
      })
  return contact_list_data

#get data from jobs
def load_posts():
  posts = []
  with engine.connect() as conn:
    database_posts = conn.execute(text("SELECT * FROM `posts`"))
  for post in database_posts:
    date = post[5]
    date = str(date).split(' ')
    date = date[0].split('-')
    post_data = {
      "sno": post[0],
      "post_title": post[1],
      "post": post[2],
      "name": post[3].title(),# modified and not checked check it when error raise
      "email":  post[4],
      "day": date[2],
      "month": month_str(date[1]),
      "year": date[0]
    }
    posts.append(post_data)
  return posts



#inserting data into database
def insert_into_contact(dic):
  """inserting data into database required dictionary in argument"""
  date_time = datetime.datetime.now()
  current_datetime = date_time.striftime("%d-%m-%Y %H:%M:%S")
  with engine.connect() as conn:
    conn.execute(
      text(
        f"INSERT INTO `contact` (`sno`,`name`,`email`,`phone`,`msg`,`date`) VALUES (NULL, '{dic['name']}','{dic['email']}','{dic['phone']}','{dic['msg']}','{current_datetime}');"
      ))
    conn.commit()


def insert_into_job(dic):
  with engine.connect() as conn:
    conn.execute(
      text(
        f"INSTER INTO `job` (`id`,`title`,`salary`,`currency`,`location`,`requirements`,`responsibility`) VALUES (NULL, '{dic['title']}','{dic['salary']}','{dic['currency']}','{dic['location']}','{dic['requirements']}','{dic['responsibility']}');"
      ))
    conn.commit()




#inserting posts data into database
def insert_into_posts(dic):
  with engine.connect() as conn:
    time = datetime.datetime.now()
    time = str(time)
    conn.execute(
      text(
        f"INSERT INTO `posts` (`sno`, `post_title`, `post`, `name`,`email`, `Datetime`) VALUES(NULL, '{dic['post_title']}', '{dic['post']}', '{dic['name']}','{dic['email']}' ,'{time}');"
      ))
    conn.commit()


if __name__ == "__main__":
  pass
  # contact_data = {
  #   'name': "ali",
  #   "email": "ali@gmail.com",
  #   "phone": 92010,
  #   "msg": "this is best website"
  # }
  #insert_into_contact(contact_data)

  # data = {
  #   "name": "Muzamil",
  #   "post_title": "Failure is not an option",
  #   "post":
  #   "Many say exploration is part of our destiny, but it’s actually our duty to future generations."
  # }
  #insert_into_posts(data)

  #print(load_posts())
