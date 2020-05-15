import Book

class BookItem():  
    """"This is a BookItem class"""
    def __init__(self, copies, ISBN):
        self.copies = copies
        self.ISBN = ISBN

    def loanBook(self):
        pass

    def writeToDatabase(self):
        with open("BookDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([self.copies, self.ISBN])