# s1 = {1,2,5,6}
# s2 = {3,6,7}
# print(s1.union(s2))
# print(s1.intersection(s2))

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.remove("Delhi")
print(cities)


cities = {"Tokyo","Madrid","Berlin","Delhi"}
item = cities.pop()
print(item)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.clear()
print(cities)

info = {"Carla",19,False,5.9}
if "Carla" in info:
    print("Carla is present")
else:
    print("Carla is absent")    


