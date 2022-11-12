"""#1
n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()    

n = 5
for i in range(0,n+1):
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print()  """
    
"""#2 
lower = 900
upper = 1000

print("Prime numbers between", lower, "and",upper,"are:")
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)    """
            
#3
nterms = int(input("How many terms? "))           
n1,n2 = 0,1
count=0 

if nterms <= 0:
    print("please enter a positive integer")
elif nterms == 1:
    print("fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("fibonacci sequence:") 
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1        