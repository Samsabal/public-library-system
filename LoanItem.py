import csv
import LoanAdministrationCSV
import BookItemCSV
import Book

class LoanItem():  
    """This is a LoanItem class"""
    def __init__(self, subscriberNumber, days, ISBN):
        self.subscribernumber = subscriberNumber
        self.days = days
        self.ISBN = ISBN

    def loanAvailabilityCheck(ISBN, author, title):
        pass
        copiesCount = 0
        copies = 0
        for book in BookItemCSV.readFromBookItemCSV():
            if author == book.author and title == book.author:
                copies = book.copies

        for loanItem in LoanAdministrationCSV.readFromLoanItemCSV():
            if ISBN == loanItem.ISBN:
                copiesCount += 1
        
        if copies - copiesCount > 0:
            return True
        else:
            return False

    def writeToDatabase(self):
        number = int(self.subscribernumber)
        with open("LoanAdministrationDatabase.csv", 'a+', newline='') as write_obj:
         #  Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
         #  Add contents of list as last row in the csv file
            csv_writer.writerow(number, self.days, self.ISBN)