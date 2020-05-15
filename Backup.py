from datetime import datetime
import json
import Book
import csv

def backupBookJSON():
    with open ("BookDatabase.json", "r") as read_file:
        jsonData = json.load(read_file)

    with open("Backups\BookDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".json", 'w+') as outfile:
        json.dump(jsonData, outfile, indent = 4)     

def backupPersonCSV():
    csvData = []
    with open("PersonDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open("Backups\BookDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData)

def backupMake():
    backupBookJSON()
    backupPersonCSV()

