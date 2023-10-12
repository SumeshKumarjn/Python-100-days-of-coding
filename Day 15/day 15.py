print("ANIMELECTION")
print("____________")
print()
print("welcome to animelection")
print()
animal = ""
while animal != "Quit" and animal != "quit":
  animal = input("What animal do you want? ")
  if animal == "Quit" or animal == "quit":
    break
  elif animal == "Dog" or animal == "dog":
    print("Woof")
  elif animal == "Cat" or animal == "cat":
    print("Meow")
  elif animal == "Bird" or animal == "bird":
    print("Tweet")
  elif animal == "Cow" or animal == "cow":
    print("Moooooo")
  elif animal == "Pig" or animal == "pig":
    print("oink")
  else:
    print("I don't know the animal,Do you want to exit? ")
print("Goodbye")