#MAP
# def cube(x):
#     return x**3
# print(cube(2))

# l = [1,2,4,6,4,3]
# # newl = []
# for item in l:
#     newl.append(cube(item))
# newl = list(map(lambda x:x**3,l))
# print(newl)


#FILTER
# def filter_func(a):
#     return a>2

# newnewl = list(filter(lambda x: x>2,l))
# print(newnewl)


#REDUCE
from functools import reduce
num = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y,num)
print(sum)
