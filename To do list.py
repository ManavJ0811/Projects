print(":Welcome to our To-Do list app:")
print("1: ADD TASK:")
print("2: REMOVE TASK:")

tasks = [] 

user = int(input("press '1' for adding the task: "))

while True:
    if user == 1:
        a = input("ADD YOUR TASK ('q' to quit): ").lower()
        if a == "q":
            break
        tasks.append(a)
    else:
        print("enter a valid input next time!")
        quit()
    
             
print(f"Your added task's are : {tasks} ")
while True:
    more = input("Press 's' to save and quit, or 'r' to remove tasks: ").lower()
    
    if more == "r":
        print("\nCurrent tasks:", tasks)
        remove_tasks = input("Enter task to remove: ").lower()
        
        if remove_tasks in tasks:
            tasks.remove(remove_tasks)
            print(f"Task removed. Remaining tasks: {tasks}")
        else:
            print("Task not found in the list!")
            
    elif more == "s":
        print("Your tasks have been saved!")
        print(f"Final task list: {tasks}")
        quit()
    else:
        print("Invalid input! Please enter 'r' to remove tasks or 's' to save and quit.")
        continue

