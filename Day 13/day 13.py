print("Grade Generator!")
print("_-_-_-_-_-_-_-_-")
print()
name = input("Name of exam: ")
print()
score = int(input("Max. possible Score: "))
print()
u_score = int(input("Your Score: "))
print()
percentage = (u_score/score)*100
if u_score >= 90:
  print("You got", u_score,"%", "which is A+")
elif u_score >= 80 and u_score <= 89:
  print("You got", u_score,"%", "which is A-")
elif u_score >= 70 and u_score <= 79:
  print("You got", u_score,"%", "which is B")
elif u_score >= 60 and u_score <= 69:
  print("You got", u_score,"%", "which is C")
elif u_score >= 50 and u_score <= 59:
  print("You got","%", "which is D")
elif u_score >= 40 and u_score <= 49:
  print("You got","%", "which is U")
else:
  print("Sorry, You failed the exam! Better luck next time :)") 