print("E P I C   B A T T L E")
print()
print("Select your move(R,P or S)")
print()
first = input("player1: ")
print()
secound = input("player2: ")
print()
if first == "R" and secound == "R":
  print("Tie")
elif first == "R" and secound == "P":
  print("Player2 wins")
elif first == "R" and secound == "S":
  print("Player1 Wins")
elif first == "p" and secound == "P":
  print("Tie")
elif first == "P" and secound == "S":
  print("Player2 wins")
elif first == "P" and secound == "R":
  print("Player1 Wins")
elif first == "S" and secound == "S":
  print("Tie")
elif first == "S" and secound == "R":
  print("Player2 wins")
elif first == "S" and secound == "P":
  print("Player1 Wins")
else:
  print("Invalid Input")