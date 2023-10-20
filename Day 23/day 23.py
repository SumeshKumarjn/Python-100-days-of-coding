print("Replit Login System!")
print("_-_-_-_-_-_-_-_-_-_-")
print()
def login():
  name = input("What is your username: ")
  password = input("What is your password: ")
  if name == "sumesh" or name == "Sumesh" and\
   password == "sumesh123" or password =="Sumesh@123":
    print()
    print("Welcome "+ name + " to Replit!")
  else:
    print("Try Again!")
print()

login()
login()