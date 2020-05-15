import csv

class Subscriber():  
    """This is a Subscriber class"""
    def __init__(self, number):
        self.number = number
    
    def writeToDatabase(self):
        with open("SubscriberDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([self.number])

