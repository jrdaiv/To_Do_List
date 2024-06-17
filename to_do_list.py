tasks = []
print("Pick a number below: ")
def add_task(tasks):
    while True:
        try:
            task = input("What tasks do you want to add?  ")
            if task in tasks:
                 print(f"task {task} already exist in list. Please type another task. ")
            else:
                 print(tasks)
                 tasks.append(task)
                 print("Task has been added to main list. ")
                 break
        except ValueError:
               print(tasks)
                
def view_task(tasks):
    print(f"Main tasks: {tasks} ")

def complete_task(tasks):
    while True:
          try:
               task = input("Which task has been completed? ")
               if task in tasks:
                    for i in range(len(tasks)):
                         if tasks[i] == task:
                              tasks[i] = task + "[x]"
               task = input(f"Type in {task}[x] to delete if not type menu? ")
               if task in tasks:
                    tasks.remove(task)
                    print(tasks)
                    break
               elif task == "menu":
                    break
          except: ValueError

def delete_task(tasks):
    try:
        task = input("Which item would you like to delete? ")
        tasks.remove(task)
    except:
        print(f"{tasks} item does not exist. ")

def main (tasks):
     while True:
          response = input("""  
                                     MENU 
                                1. Add Tasks 
                                2. View Tasks 
                                3. Mark Tasks As Complete 
                                4. Delete Tasks 
                                5. Quit
                           """)
          if response == "1":
               add_task(tasks)
          elif response == "2":
               view_task(tasks)
          elif response == "3":
               complete_task(tasks)
          elif response == "4":
               delete_task(tasks)
          elif response == "5":
               print("Ok, goodbye.")
               break
main(tasks)


