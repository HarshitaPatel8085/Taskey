import json
from datetime import datetime
from prettytable import PrettyTable


def display(ID):
    with open('data.json','r') as f:
        task=json.load(f)
    ID=int(ID)    
    table=PrettyTable(["Task ID","Task","Status","CreatedAt","UpdatedAt"])    
    for i in task:
        if(i["id"]==ID):
            table.add_row([i["id"],i["description"],i["status"],i["createdAt"],i[ "updatedAt"]])
            print(table)
            break
    return

def add_task(desc):
    try:
        with open('data.json', 'r') as f:
            task = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        task = []

    time=datetime.now().strftime("%Y-%m-%d at %H:%M")

    ID=task[-1]["id"]+1 if task else 1

    newtask={
       "id":ID,
        "description":desc,
        "status":"todo",
        "createdAt":time,
        "updatedAt":time
    }
    task.append(newtask)
    with open('data.json', 'w') as f:
        json.dump(task, f, indent=4)
    display(ID)    
    return ID

def update(id,desc):
    with open('data.json','r') as f:
        task=json.load(f)
    
    task_id=int(id)
    found=False
    for i in task:
        if(i["id"]==task_id):
            i["description"]=desc
            i["updatedAt"]=datetime.now().strftime("%Y-%m-%d at %H:%M")
            found=True
            break
    if found:
        with open('data.json','w') as f:
            json.dump(task,f,indent=4) 
        display(task_id)     
        return found
    return False  

def mark(task_id):
    with open('data.json','r') as f:
        task=json.load(f)
    task_id=int(task_id) 
    found=False
    for k in task:
        if(k["id"]==task_id):    
            k["status"]="in-progress"
            k["updatedAt"]=datetime.now().strftime("%Y-%m-%d at %H:%M")
            found=True
    if(found):        
        with open('data.json','w') as f:
            json.dump(task,f,indent=4)
        display(task_id)     
        return True
    return False    

def done(task_id):
    with open('data.json','r') as f:
        task=json.load(f)
    task_id=int(task_id) 
    found=False
    for k in task:
        if(k["id"]==task_id):    
            k["status"]="done"
            k["updatedAt"]=datetime.now().strftime("%Y-%m-%d at %H:%M")
            found=True
    if(found):        
        with open('data.json','w') as f:
            json.dump(task,f,indent=4) 
        display(task_id)    
        return True
    return False    

def delete(task_id):
    with open('data.json','r') as f:
        task=json.load(f)
    task_id=int(task_id)
    found=False
    for k in task:
        if(k["id"]==task_id):
            found=True
            task=[i for i in task if not (i["id"]==task_id)]  
            break
    if(found):
        with open ('data.json','w') as f:
            json.dump(task,f,indent=4) 
            return True
    return False  

def list(sort_by=None): 
    with open('data.json','r') as f:
        task=json.load(f)
    if not task:
        print("Your task list is currently empty")
        return 
    
    if sort_by is None:
        table=PrettyTable(["Task ID","Task","Status","CreatedAt","UpdatedAt"])
        for i in task:
            table.add_row([i["id"],i["description"],i["status"],i["createdAt"],i[ "updatedAt"]])
        print(table) 
    else:
        table=PrettyTable(["Task ID","Task","CreatedAt","UpdatedAt"])
        for i in task:
            if i["status"] == sort_by:
                table.add_row([i["id"],i["description"],i["createdAt"],i[ "updatedAt"]])
        print(table)
    return       