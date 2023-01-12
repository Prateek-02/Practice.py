import os 

if (not os.path.exists("data")):
    os.mkdir("data")                   #it will make a folder name data
    
for i in range(0,10):                 
    os.mkdir(f"data/day{i+1}")         #it will make 10 folders of day inside the data folder