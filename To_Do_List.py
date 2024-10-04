#-------------------------------------------------------------------------------------------------#
#------------------------------------------ TO - DO LIST -----------------------------------------#

def display_menu():
    print("\n...Welcome to the To-Do List !...")
    print("\n1 - Add a New Task")
    print("2 - Delete a Task")
    print("3 - Show All Tasks")
    print("4 - Exit")
    option = int(input("\nChoose your option : "))
    return option

def add_task(all_tasks):

    print("\nAdd New Task ")
    tasks = []
    ser_no=int(input("Enter Serial Number "))
    date=str(input("Enter Date : "))
    task=str(input("Enter the Task : "))
    tasks.append(date)
    tasks.append(task)
    tasks.append(ser_no)
    all_tasks.append(tasks)
    print("\nTask added successfully ..!")


def delete_task(all_tasks):
    ser_no = input("\nEnter Serial Number of the task to be deleted : ")

    for i, tasks in enumerate(all_tasks):
        if tasks[0] == ser_no:
            print("\nDeleting the following tasks:")
            print(tasks)
            del all_tasks[i]
            print("\nTask deleted successfully!")
            return
    print("No tasks found with the Serial Number ", ser_no)


def display_all_tasks(all_tasks):
    if len(all_tasks) == 0:
        print("\nNo Tasks available to display ...")
    else:
        print("\nAll Contacts : ")
        for tasks in all_tasks:
            display_task(tasks)


def display_task(tasks):
    print("Serial Number : ",tasks[0])
    print("Date : ",tasks[1])
    print("Task : ",tasks[2])
    print("-" * 30)


def main():
    all_tasks=[
        [1,"24/09/24","Prepare for test ."]
        ]

    while True:
        option = display_menu()

        if option == 1:
            add_task(all_tasks)
        elif option == 2:
            delete_task(all_tasks)
        elif option == 3:
            display_all_tasks(all_tasks)
        elif option == 4:
            print("Exiting the To-Do List... Goodbye !")
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()