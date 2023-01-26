a = "hello"
b = "hello"

print(a==b)      #exact location of object in memory
print(a is b)    #value

a = 5
b = "5"
print(a == b)
print(a is b)

a = [1,2,5]
b = [1,2,5]
print(a == b)
print(a is b)