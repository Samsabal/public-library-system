import Book

class BookLibrary(Book.Book):  
    """"This is a book class"""

        
    def addBook(self):
        number = 99  #This needs to be a genarated number
        print("Add a Book by filling in the information.\n")
        author = input("Author: ")
        country = input("Country: ")
        imageLink = input("ImageLink: ")
        language = input ("Language: ")
        link = input("Link: ")
        pages = input("Pages: ")
        title = input("Title: ")
        year = input("Year: ")
        ISBN = input("ISBN: ")
        copies = input("Copies: ")
        book = Book.Book(author, country, imageLink, language, link, pages, 
        title, year)
        bookItem = BookItem.BookItem(copies, ISBN)
        book.writeToDatabase(book)
        bookItem.writeToDatabase()
