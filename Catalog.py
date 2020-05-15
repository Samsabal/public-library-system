
import Book
import BookJSON
import json

class Catalog():
    """This is a catalog class"""
    def searchBook(self):
        bookList = BookJSON.readFromBookJSON()
        foundBooks = []
        searchKeywords = []
        print("[Catalog] Please type in your search criteria (title, author, country).")
        print("[Catalog] You can type in more than one or type 'none' for no criteria")
        searchInput = input("[Catalog] >>> ")

        if "none" in searchInput.lower():
            iteration = 1
            for book in bookList:
                print("[Catalog] " + str(iteration) + " - " + book.title)
                iteration += 1
                
            print("[Catalog]")
            chosenBook = int(input("[Catalog] Please input book number: "))
            print("[Catalog]")
            print("[Catalog] Your chosen book: " + bookList[chosenBook-1].title)
            # Hierboven moet ik verwijzen naar de bookList[chosenBook-1].page

        if "title" in searchInput.lower():
                searchKeywords.append(input("[Catalog] Fill in the title >>> "))

        if "author" in searchInput.lower():
                searchKeywords.append(input("[Catalog] Fill in the author >>> "))

        if "country" in searchInput.lower():
                searchKeywords.append(input("[Catalog] Fill in the country >>> "))    

        for criteria in searchKeywords:
            for book in bookList:
                if criteria.lower() in book.title.lower():
                    foundBooks.append(book)
                if criteria.lower() in book.author.lower():
                    foundBooks.append(book)
                if criteria.lower() in book.country.lower():
                    foundBooks.append(book)

        print("[Catalog]")
        iteration = 1
        for book in foundBooks:
            print("[Catalog] " + str(iteration) + " - " + book.title)
            iteration += 1

        print("[Catalog]")
        chosenBook = int(input("[Catalog] Please input book number: "))
        print("[Catalog]")
        foundBooks[chosenBook-1].showBook()
        # Hierboven moet ik verwijzen naar de bookList[chosenBook-1].page
            
