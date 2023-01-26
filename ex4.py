import random

b = (input("choose , rock paper scissor: "))
a = ["rock","paper","scissor"]
c = random.choice(a)
if b==c:
    print("tie")
    marks = 0
    print(f"your point is: {marks}")
elif b=="paper" and c=="scisscor":
    print("loss")
    marks = -1
    print(f"your point is: {marks}")
elif b=="rock" and c =="paper":
    print("loss")
    marks = -1
    print(f"your point is: {marks}")
elif b=="scissor" and c=="rock":
    print("loss")
    marks = -1
    print(f"your point is: {marks}")
else:
    print("win")  
    marks = 1
    print(f"your point is:{marks}")