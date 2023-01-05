def calcGmean(a,b):
    mean = a*b/(a+b)
    print(mean)
    
def isGreater(a,b):
    if a>b:
        print("first num is greater")
    else:
        print("second num is greater")
    
a = int(input())
b = int(input())
isGreater(a,b)   
calcGmean(a,b) 
    
