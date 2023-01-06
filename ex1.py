import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
hour = int(time.strftime("%H"))
hour = int(input("Enter Hour: "))
print(hour)

if hour>0 and hour<12:
    print("Good Morning")
elif hour>=12 and hour<=17:
    print("Good Afternoon")    
else:
    print("Good Night")


# timestamp = time.strftime("%M")
# print(timestamp)
# timestamp = time.strftime("%S")
# print(timestamp)
