# def double(x):
#     return x*2



# In lambda function we can take multiple values at a time
def appl(fx,value):
    return 6 + fx(value)

double = lambda x: x*2
cube = lambda x: x**3
avg = lambda x,y: (x+y)/2
print(double(5))
print(cube(5))
print(avg(4,6))
print(appl(cube,2))
print(appl(lambda x: x**2,2))