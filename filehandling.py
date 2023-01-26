#Readline method
# f = open('myfile2.txt','r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student {i} in Maths is: {m1}")
#     print(f"Marks of student {i} in English is: {m2}")
#     print(f"Marks of student {i} in SST is: {m3}")   
#     print(line)
    
    
    
#Writeline method
# f = open('myfile3.txt','w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()




#seek()
# with open('myfile.txt','r') as f:
#     f.seek(10)
#     data = f.read(5)
#     print(data)



#tell()
# with open('myfile.txt','r') as f:
#     f.seek(10)
    
#     print(f.tell())
#     data = f.read(5)
#     print(data)


#truncate
with open('sample.txt','w') as f:
    f.write('Hello world')
    f.truncate(5)
    
with open('sample.txt','r') as f:
    print(f.read())
    

    