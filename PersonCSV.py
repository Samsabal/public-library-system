import csv
import Person

personCSV = "PersonDatabase.csv"

def readFromPersonCSV():
    userList = []

    with open(personCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #line_count = 0

        for r in csv_reader:
            userList.append( Person.Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]) )
            
    return userList

def writeToPersonCSV(row_contents):
    with open(personCSV, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)

#readFromPersonCSV()

#for user in userList:
#    if(user.username == "Ancion"):
#        user.Sleep()