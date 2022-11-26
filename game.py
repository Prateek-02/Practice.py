print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
  quit()

print("Okay! Let's play")

question = ("What does CPU stand for? ")
print(question)
answer = input("answer: ")
if answer == "central processing unit":
  print("Correct!")
else:
  print("Incorrect!")

question = ("What does GPU stand for? ")
print(question)
answer = input("answer: ")
if answer == "graphics processing unit":
  print("Correct!")
else:
  print("Incorrect!")

question = ("What does RAM stand for? ")
print(question)
answer = input("answer: ")
if answer == "random access memory":
  print("Correct!")
else:
  print("Incorrect!")

question = ("What does ROM stands for?  ")
print(question)
answer = input("answer: ")
if answer == "read only memory":
  print("Correct!")
else:
  print("Incorrect!")
  
print("Thank you")  