from datetime import datetime
import json
import Book
import csv
import os 
import Main

def backupMakeBookJSON(backupDirectory):
    with open ("BookDatabase.json", "r") as read_file:
        jsonData = json.load(read_file)

    with open(str(backupDirectory) + "\BookDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".json", 'w+') as outfile:
        json.dump(jsonData, outfile, indent = 4)     

def backupMakePersonCSV(backupDirectory):
    csvData = []
    with open("PersonDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open(str(backupDirectory) + "\PersonDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData)

def backupRestorePersonCSV(folderName):
    fileName = os.listdir('./Backups/' + folderName)
    csvData = []
    with open('./Backups/' + folderName + "/" + fileName[1], mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open("PersonDatabase.csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData)  

def backupRestoreBookJSON(folderName):
    fileName = os.listdir('./Backups/' + folderName)
    with open ('./Backups/' + folderName + "/" + fileName[0]) as read_file:
        jsonData = json.load(read_file)

    with open("BookDatabase.json", "w") as outfile:
        json.dump(jsonData, outfile, indent = 4)     

def backupMake():
    path = "Backups\Backup_" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S")
    backupDirectory = os.mkdir(path)
    backupMakeBookJSON(path)
    backupMakePersonCSV(path)
    
def backupRestore(folderName):
    backupRestoreBookJSON(folderName)
    backupRestorePersonCSV(folderName)

def backupRestoreMenu():
    while True:
        iteration = 1
        optionList = []
        backupFile = os.listdir('./Backups')
        print("[Backup] ------------------------------------")
        print("[Backup] Select which backup you would like to restore")
        for file in backupFile:
            print("[Backup] " + str(iteration) + " - " + file)
            optionList.append(iteration)
            iteration += 1       
            
        print("[Backup] ")
        print("[Backup] Press 'q' to go back")
        print("[Backup] ")
        backupSelectOption = input("[Backup] Selection: ")

        if backupSelectOption == "q":
            Main.mainMenu()
        elif int(backupSelectOption) in optionList:
            folderName = backupFile[int(backupSelectOption)-1]
            backupRestore(folderName)
        else:
            print("[Backup] Invalid input. Please try again.")