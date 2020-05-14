import csv
import Person


def readFromPersonCSV():
    userList = []

    with open("PersonDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #line_count = 0

        for r in csv_reader:
            userList.append( Person.Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]) )
            
    return userList

def testtest():
    return 1
#readFromPersonCSV()

#for user in userList:
#    if(user.username == "Ancion"):
#        user.Sleep()