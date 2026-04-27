import os
import json
import sys
import datetime 
import function as fun

filename='data.json'

if not (os.path.exists('data.json')):             #create json file when first run the code
    with open (filename,'w') as f:
        f.write("[]")

try:
    with open(filename,'r') as f:
       task=json.load(f)
except json.JSONDecodeError:
    task=[]


if (len(sys.argv))<2:
    print("***Welcome***")
    print("Usage:Taskey [add|update|delete|list|mark-in-progress|done] ")
    exit()

command=sys.argv[1]  

if(command=="add"):                                    #check the command
    if(len(sys.argv)>=3):
        desc1=sys.argv[2]
        id1=fun.add_task(desc1)                        #calling add function of function.py
        print("Task added succesfully (id:",id1,")")
    else:
        print("Task description is not given")  
elif(command=="update"):
    if(len(sys.argv)>3):
        id1=sys.argv[2]
        desc2=sys.argv[3]
        if(fun.update(id1,desc2)):                        #calling update function of function.py
           print("Task (id:",id1,") updated succesfully")
        else:
           print("Invalid ID")  
    else:
        print("Updated description is not given")       
elif(command=="mark-in-progress"):
    if(len(sys.argv)>=3):
        id1=sys.argv[2]
        if(fun.mark(id1)):                         #calling mark function of function.py
            print("Task (id:",id1,") updated succesfully")
        else:
            print("Task (id:",id1,") not found")   
    else:
        print("Task ID not given.Usage:Taskey [add|update|delete|list|mark-in-progress|done]")         
elif(command=="done"):
    if(len(sys.argv)>=3):
        id1=sys.argv[2]
        if(fun.done(id1)):                           #calling done function of function.py
            print("Task (id:",id1,") completed")    
        else:
            print("Task (id:",id1,") not found")  
    else:
        print("Task ID not given.Usage:Taskey [add|update|delete|list|mark-in-progress|done]")     
elif(command=="delete"):
    if(len(sys.argv)>=3):
        id1=sys.argv[2]
        if(fun.delete(id1)):                        #calling delete function of function.py
            print("Task (id:",id1,")deleted")  
        else:
            print("Task (id:",id1,") not found")  
    else:
         print("Task ID not given.Usage:Taskey [add|update|delete|list|mark-in-progress|done]")     
elif(command=="list"):
    if(len(sys.argv)==2):
        fun.list()                               #calling list function of function.py
    elif(len(sys.argv)>=3):
        fun.list(sys.argv[2])   
    else:
        print("invalid command.Usage:Tasky list [staus]") 
else:
    print("Invalid command")            
        
