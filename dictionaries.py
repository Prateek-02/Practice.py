# dic = {"Harry": "Human being","Spoon":"Object"}
# print(dic["Harry"])

info = {"name":"Karan", "age":19,"eligible":True}

# print(info["name"])
# print(info.keys())
# print(info.values())
# for key in info.keys():
#     print(info[key])

print(info.items())
for key,value in info.items():
    print((f"The value corresponding to the key {key} is {value}"))