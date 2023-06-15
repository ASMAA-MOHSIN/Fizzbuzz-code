# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"

def reg_user():
    '''Add a new user to the user.txt file'''
    new_username = input("New Username: ")

        # - Request input of a new password
    new_password = input("New Password: ")

        # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")  
            list_user = []
        # - Request input of a new username
            with open('user.txt', 'r') as file:
                for line in file:
                    index = line.split(";")
                    list_user.append(index[0])
                    #existing_usernames = file.readlines().split(";")
                #print(existing_usernames)
# Check if the new username already exists
            print(list_user)
            if new_username in list_user:
                print("Username already exists.")
            else:
    # Write the new username to the file
                with open('user.txt', 'a') as file:
                    file.write(new_username + '\n')
                print("Username added successfully.")                
            username_password[new_username] = new_password
            
            # with open("user.txt", "w") as out_file:
            #     user_data = []
            #     for k in username_password:
            #         user_data.append(f"{k};{username_password[k]}")
            #     out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
    else:
            print("Passwords do not match")

def view_mine(): 
    with open("tasks.txt", "r") as file:
     data = file.readlines()
    print(data)
    data_dict = {}
    for count, val in enumerate(data):
     data_dict[count] = val.strip()
     val_split = val.strip().split(";")
     print(val_split)
     print(f"Username: {val_split[0]}\nTask: {val_split[1]}")
     print(f"{count}: {val}")

    print(data_dict)

 #with open('tasks.txt', 'r') as j:
    #for text in j:
        #print(text)



    # Read existing usernames from file
#             with open('user.txt', 'r') as file:
#                     existing_usernames = file.readline()  #.splitlines()
# # Check if the new username already exists
#                     if new_username in existing_usernames:
#                         print("Username already exists.")
#                     else:
#     # Write the new username to the file
#                         with open('user.txt', 'a') as file:
#                             file.write(new_username + '\n')
#                             print("Username added successfully.")
 
   
     # Read all lines in the file and check if the username already exists
            # for lines in out_file:
            #     lines = out_file.readline
            # if new_username in lines:
            #     print("Error: Username already exists.")
            #     #return False 

            
# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
gr - Generate reports
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
    
    elif menu == 'gr':
        print ("Genterating reports")
        # Specify the paths of the source file and destination file
    # source_file_path = 'tasks.txt'
    # destination_file_path = 'task_overview.txt'

    # #with open ("task_overview.txt", "w") as files:
    # def copy_file(source_file_path, destination_file_path):
    # # Open the source file in read mode and the destination file in write mode
    #     with open(source_file_path, 'r') as source_file, open(destination_file_path, 'w') as destination_file:
    #     # Read the contents of the source file
    #         contents = source_file.read()
        
    #     # Write the contents to the destination file
    #         destination_file.write(contents)
        
    #     print("File copied successfully!")

# Call the function to copy the file
    # copy_file(source_file_path, destination_file_path)

#     def copy_file2(source_file_path, destination_file_path):
#     # Open the source file in read mode and the destination file in write mode
#      with open(source_file_path, 'r') as source_file, open(destination_file_path, 'w') as destination_file:
#         # Read the contents of the source file
#         contents = source_file.read()
        
#         # Write the contents to the destination file
#         destination_file.write(contents)
        
#     print("File copied successfully!")

# # Specify the paths of the source file and destination file
#     source_file_path = 'user.txt'
#     destination_file_path = 'user_overview.txt'

# # Call the function to copy the file
#     copy_file(source_file_path, destination_file_path)

    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")


    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            


    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        for t in task_list:
            if t['username'] == curr_user:
                disp_str = f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)
                
    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")