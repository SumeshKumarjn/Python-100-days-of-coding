print("Fill-in the blank Lyrics!")
print("(complete the lyrics, see if you're as cool as me)")
print("(Song Name: PHOTOGRAPH by Edsheeran)")
print()
counter = 1
while True :
  gap_one = input("Loving can hurt, loving can _______ sometimes ")
  if gap_one == "hurt" :
    print("Correct")
    print()
    counter += 1
  else:
    print("Nope it's wrong")
    print()
  gap_two = input("But it's the only _____ that I know ")
  if gap_two == "thing":
    print("Correct")
    print()
    counter += 1
  else:
    print("Nope it's wrong")
    print()
  gap_three = input("When it gets hard, you know it can get hard _________ ")
  if gap_three == "sometimes":
    print("Correct")
    print()
    counter += 1 
  else:
    print("Nope it's wrong")
    print()
  gap_four = input("It is the only thing makes us __________ ")
  if gap_four == "feel alive":
    print("Correct")
    print()
    counter += 1
    break
  else:
    print("Nope it's wrong")
print()
print("Well Done, ADIOS:)")
print("You got it in",counter,"attempts")