import csv

class LoanItem():  
    """This is a LoanItem class"""
    def __init__(self, subscriberNumber, days, ISBN):
        self.subscribernumber = subscriberNumber
        self.days = days
        self.ISBN = ISBN

    def writeToDatabase(self):
        number = int(self.subscriberNumber)
        with open("LoanItemDatabase.csv", 'a+', newline='') as write_obj:
         #  Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
         #  Add contents of list as last row in the csv file
            csv_writer.writerow(number, self.days, self.ISBN)