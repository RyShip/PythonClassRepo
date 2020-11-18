# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Rship, 11/16/20, added code to complete assignment
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = 'ToDoList.txt'
objFile = None # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(strFile, 'r')
for row in objFile:
    row = row.split(",")
    dicRow = {'Task': row[0], 'Priority': row[1].strip()}
    lstTable.append(dicRow)
objFile.close()



# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    # TODO: Add Code Here
    if (strChoice.strip() == '1'):
        print(lstTable)
        continue
   # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strFile = open('ToDoList.txt', "w")
        taskData = input('Task: ')
        priorityData = input('Priority: ')
        dicRow = {'Task': taskData, 'Priority': priorityData}
        lstTable.append(dicRow)
        continue
   # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemove = input("Choose a task to remove: ")
        for i in lstTable:
            if strRemove in ['Task'] == strRemove:
                lstTable.remove(i)
                print('removed')
                continue
   # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        strFile = open('ToDoList.txt', 'w')
        for row in lstTable:
            strFile.write(row['Task'] + ", " + row['Priority'] + "\n")
            strFile.close()
        print("data saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strInput = input('to close the program type \'exit\': ')
        if strInput == 'exit':
            break  # and Exit the program

