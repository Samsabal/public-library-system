import csv
import LoanAdministrationCSV

import csv
import LoanAdministrationCSV
import BookItemCSV

class LoanItem():  
    """This is a LoanItem class"""
    def __init__(self, subscriberNumber, days, ISBN):
        self.subscribernumber = subscriberNumber
        self.days = days
        self.ISBN = ISBN

    def loanAvailabilityCheck(ISBN):
        pass
        coppiesCount = 0
        for ISBN in BookItemCSV.readFromBookItemCSV():
            if ISBN == BookItemCSV.readFromBookItemCSV.ISBN:
                return BooBookItemCSV.readFromBookItemCSV.copies

        for loanItem in readFromLoanItemCSV:
            if ISBN == loanItem.ISBN:
                coppiesCount += 1
        
        if coppies - coppiesCount > 0:
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