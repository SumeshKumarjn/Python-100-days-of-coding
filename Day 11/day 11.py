print("Secounds Calculator!")
print("--------------------")
print()
sec = int(input("How many secounds in a minute? "))
print()
min = int(input("How many minutes in an hour? "))
print()
hour = int(input("How many hours in a day? "))
print()
month = int(input("How many months are there in a year? "))
print()
days = int(input("How many days are there in a year? "))
print()
yearone = input("If it was a leap year, then ?? ")
year = days * hour * min * sec
print()
if yearone == "one more extra day":
  print(year + 24)
else:
  print(year)
print()
print("There are",year,"secounds per year :)")