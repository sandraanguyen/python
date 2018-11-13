#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  November 12, 2018
# SANDRA NGUYEN
# Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

objFileName = "/Users/sandra/Desktop/Sandra Nguyen A5/ToDo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

f = open(objFileName, "r")
#for each line in txt file
for line in f:
    #split each line by comma
    strLine = line.split(",")
    #first token becomes task, second token becomes priority
    dicRow = {"Task":strLine[0].strip(), "Priority":strLine[1].strip()}
    lstTable.append(dicRow)
f.close()


# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("The current items in the ToDo lists are: ")
        #Iterates through list and prints each task & priority
        for eachRow in lstTable:
            print("Task is: " + eachRow["Task"] + "  |||  Priority is: " + eachRow["Priority"])

    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
    	#prompts user for the task, and priority
        strTask = str(input("Add the task here: ")).strip()
        strPrio = str(input("Add the priority level here: ")).strip()
        #adds user input to a dictionary row
        dicRow = {"Task":strTask,"Priority":strPrio}
        #appending user input to the list
        lstTable.append(dicRow)
        print("Thanks. Your " + strTask + ", " + strPrio + " was added.")

    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        strRemove = str(input("What task do you want to remove? "))
        #tracks which row will need to be deleted
        intCounter = 0
        #checks through the list to see if task matches what user wants removed
        for perRow in lstTable:
            if(perRow["Task"] == strRemove):
                del lstTable[intCounter]
            intCounter += 1
        print("Your task of '" + strRemove + "' has been removed if found.")

    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        strSave = input("Do you want to save to text file? (y/n) ")
        #if user wants to save, opens objFile and writes to file. Then closes
        if(strSave.lower() == "y"):
            print("I'm saving.......")
            objFile = open(objFileName, 'w')
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            print("Save completed.")
        else:
            print("alright, not saving. ")

    elif (strChoice == '5'):
        break #and Exit the program

