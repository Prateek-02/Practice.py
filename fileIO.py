#Reading a file
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()



#Writing a file
f = open('myfile.txt', 'w')
f.write("Hello World!")
f.close()


with open('myfile.txt', 'a') as f:
    f.write("Hey Good morning")

#Appending a file
f = open('myfile.txt', 'a')
f.write("Hello World!")
f.close()