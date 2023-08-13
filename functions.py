# class config:
#   def __init__(self,name, email, phone, message):
#     self.name = name
#     self.email = email
#     self.phone = phone
#     self.message = message

#   def save_in_config(self):
#     with open('templates/config/config.json', 'w'):

 
def save_in_config(dic, name, email, phone, message):
  dic['contact'].append({
    "name": name,
    "email": email,
    "phone": phone,
    "message": message
  })


if __name__ == '__main__':
  #testing code for main files
  dice = {
    "jbs": [565,4656,54656,46,5,654,65,465,46,546,5,684,68654],
    "contact": []
  }
  while True:
    inpname = input("name: ")
    if inpname == "break":
      break
    inpemail = input('email: ')
    inpphone = input('phone: ')
    inpmessage = input('message: ')

    save_in_config(dice, inpname, inpemail, inpphone, inpmessage)
    print(dice)
