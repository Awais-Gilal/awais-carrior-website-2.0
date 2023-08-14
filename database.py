from sqlalchemy import create_engine, text, insert


def tup_into_dict_contact(tup):
  return {
    'sno': tup[0],
    'name': tup[1],
    'email': tup[2],
    'phone': tup[3],
    'msg': tup[4],
    'time': tup[5]
  }


def tup_into_dict_job(tup):
  return {
    "id": tup[0],
    "title": tup[1],
    "salary": tup[2],
    "corrency": tup[3],
    "location": tup[4],
    "responsibility": tup[5],
    "requirements": tup[6],
    "time": tup[7],
  }


username = "sql6639351"
password = "WCrfFr7VGg"
host = "sql6.freesqldatabase.com"
database_name = "sql6639351"
charset = "utf8mb4"

url = f"mysql+pymysql://{username}:{password}@{host}/{database_name}?charset={charset}"
# mysql+pymysql://sql6639351:WCrfFr7VGg@sql6.freesqldatabase.com/sql6639351?charset=utf8mb4

engine = create_engine(url)


def load_jobs():
  result_dict = []
  with engine.connect() as conn:
    result = conn.execute(text("select * from job"))
    for row in result:
      result_dict.append(tup_into_dict_job(row))
    return result_dict


if __name__ == "__main__":

  print(load_jobs())
