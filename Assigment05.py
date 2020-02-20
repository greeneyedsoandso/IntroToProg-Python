# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# JDSmith,2.19.2020, added functionality to all sections
# JDSmith,2.18.2020,started editing for assignment 5
# RRoot,1.1.2030,Created started script
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
strTask = ''  # Task entry
strPriority = ''  # Priority entry

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.

objFile = open('ToDoList.txt', 'r')
for row in objFile:
    i, v = row.split(',')
    dicRow = {'task': i, 'priority': v}
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
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(str(row['task'] + ', ' + row['priority'].strip()))
        print('-' * 55)  # a divider before the menu displays again
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while (True):
            strTask = input('Task: ')
            strPriority = input('Priority: ')
            lstTable.append({'task': strTask, 'priority': strPriority})
            strChoice = input("Exit to menu? (y/n): ")
            if strChoice.lower() == 'y':
                break
        print('\n' + '-'*55 + '\nCurrent data:')
        for row in lstTable:
            print(str(row['task'] + ', ' + row['priority'].strip()))
        print('-' * 55)  # a divider before the menu displays again
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Exit loop
        while (True):
            strTask = input('Task to remove: ')
            strStatus = 'Row not found'  # Boolean flag method
            for row in lstTable:
                if row['task'].lower() == strTask.lower():
                    lstTable.remove(row)
                    strStatus = 'Row removed.'
            print(strStatus)
            print('Updated data:', lstTable)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Consider adding other confirmation of content
        objFile = open("ToDoList.txt", 'w')
        for row in lstTable:
            objFile.write(str(row['task'] + ',' + str(row['priority'])))
        objFile.close()
        print('Saved in file!')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Happy planning!')
        break  # and Exit the program5
# TODO: add message for not-menu entry
