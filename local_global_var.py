# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"the local x is {x}")
#     print("Hello Harry")
 
# print(f"the global x is {x}")   
# hello()

x = 10             #global variable

def my_func():
    y = 5          #local variable
    print(y)
    
my_func()
print(x)



x = 10             #global variable

def my_func():
    global x
    x = 4
    y = 5          #local variable
    print(y)
    
my_func()
print(x)

