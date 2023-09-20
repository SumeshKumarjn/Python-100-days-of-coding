print("TIP CALCULATOR")
print()
spend = float(input("How much did you spend? "))
print()
tip = int(input("What is the percentage do you want to tip? "))
print()
number = int(input("How many people in your group? "))
print()
answer = tip/100*spend + spend
final_answer = answer / number
answer = round(answer,2)
print()
print("You each owe $",final_answer)
