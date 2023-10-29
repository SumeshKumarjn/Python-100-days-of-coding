print("Totally Random One-Million-To-One")
print()
print("Let's Go!!")

import random 
correct_number = random.randint(1,10)
attempt = 1

while True:
  user_guess = int(input("What is your guess?: "))
  if user_guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if user_guess < correct_number:
    print("Too low. Try again!")
    attempt += 1
  elif user_guess > correct_number:
    print("Too high. Try again!")
    attempt += 1
    continue
  elif user_guess == correct_number:
    print("You have won!")
    break 
    exit()
  else:
    print("I don't recognize this number")
print("It took you", attempt, "guesses to get all the random number correctly!")