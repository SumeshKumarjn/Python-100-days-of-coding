print("Math Game!")
print()
num = int(input("Name your multiplies: "))
print()
print("Let's begin!")
print()

counter = 0
for i in range(1, 11):
  ans = i*num
  print(i, "x" , num, "=")
  final = int(input("> "))
  if final == ans:
    print("You got it Correct")
    counter += 1
  else:
    print("Nope its wrong, Correct answer is",ans)

if counter == 10:
  print("You got all 10 questions correct!")
else:
  print("You got", counter, "out of 10 correct.")