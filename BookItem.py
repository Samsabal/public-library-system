import Book

class BookItem(Book.Book):  
    """"This is a BookItem class"""
    def __init__(self, copies, ISBN):
        self.copies = copies
        self.ISBN = ISBN

    def loanBook(self):
        pass

    def writeToDatabase(self):
        pass