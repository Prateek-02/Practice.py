marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Harry is awesome")
#     index += 1   

for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Harry is awesome")
    index += 1     
    


fruits = ["apple","banana","mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

