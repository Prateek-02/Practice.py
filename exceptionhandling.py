# a = input("enter the num: ")
# print(f"multiplication table of {a} is : ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
        
# except:
#     print("Invalid Input")        
    
# print("Some imp lines of code")   
# print("End of programme")

try:
    num = int(input("enter an ineger: "))
    a = [6,7]
    print(a[num])
except ValueError:
    print("number entered is not an integer.")
    
except IndexError:
    print("index out of range")    