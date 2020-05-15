import Book

class BookItem(Book.Book):  
    """"This is a BookItem class"""
    def __init__(self, copies):
        self.copies = copies

    def loanBook(self):
        pass

    def writeToDatabase(self):
        pass