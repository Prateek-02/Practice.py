# countries = ("Spain","Italy","India","England","Germany")
# temp = list(countries)
# temp.append("Russia")           #add item at the end
# temp.pop(3)                     #remove item from given index
# temp[2]  = "Finland"            #change item in the given index
# countries = tuple(temp)
# print(countries)

tup1 = (0,1,2,3,2,3,1,3,2,1,5,3,6,7,3)
# res = tup1.count(3)
res = tup1.index(3,4,8)
print("index of 3 is:",res)
# print("Count of 3 is:",res)