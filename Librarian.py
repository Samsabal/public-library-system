import Person
import csv

def readFromLibrarianCSV():
    numberList = []

    with open ("LibrarianDatabase.csv", mode ='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for r in csv_reader:
            numberList.append( (r[0]) )

    return numberList

def librarianCheck(number):
        numberList = readFromLibrarianCSV()
        if number in numberList:
            return True

class Librarian(Person.Person):  
    """This is a Librarian class"""

    def __init__(self, number):
        self.number = number

    def writeToDatabase(self):
        pass

    
    