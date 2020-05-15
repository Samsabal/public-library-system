import Person
import PersonCSV
import BookJSON
import Librarian
import Subscriber
import Backup
import Book
import BookItem
import LoanItem
import Catalog
from utils import clearConsole

CURRENTUSER = 0

def setup():
    global userList, bookList
    userList = PersonCSV.readFromPersonCSV()
    bookList = BookJSON.readFromBookJSON()
    #for book in bookList:
        #print(book.author)

def checkUsername(username):
    global userList, CURRENTUSER

    for user in userList:
        if username == user.username:
            CURRENTUSER = user.number
    if CURRENTUSER == 0:
        print("[Login] This username does not exist, please try again!")
        login()
        
def loanBook(ISBN):
    global CURRENTUSER
    LoanItem.LoanItem.writeToDatabase(CURRENTUSER, 14, ISBN)

def register():
    number = 99  #This needs to be a genarated number
    print("[Register] Register a person by filling in the information.\n")
    gender = input("[Register] Gender (male/female): ")
    nameSet = input("[Register] NameSet: ")
    givenName = input("[Register] GivenName: ")
    surname = input ("[Register] Surname: ")
    streetAddress = input("[Register] Street Address: ")
    zipCode = input("[Register] Zip Code: ")
    city = input("[Register] City: ")
    emailAddress = input("[Register] Email Address: ")
    userName = input("[Register] Username: ")
    telephoneNumber = input("[Register] Telephone Number: ")
    
    personType = input("[Register] Is this person a Librarian or Subscriber (librarian/subscriber):")
    if personType != "librarian" and personType != "subscriber":
        print("[Register] Invalid input, please try again!")
        personType
    else:
        person = Person.Person(number, gender, nameSet, givenName, surname,
        streetAddress, zipCode, city, emailAddress, userName, telephoneNumber)
        person.writeToDatabase(personType)

def addBook():
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
    bookItem = BookItem.BookItem(title, author, copies, ISBN)
    book.writeToDatabase(book)
    bookItem.writeToDatabase()

def login():
    username = input("[Login] Please login with your username: ")
    checkUsername(username)  

def mainMenu():
    global CURRENTUSER
    while True:
        if Librarian.librarianCheck(CURRENTUSER):
            print("[Menu] 1. Search book")
            print("[Menu] 2. Logout")
            print("[Menu] 3. Add book")
            print("[Menu] 4. Make backup")
            print("[Menu] 5. Restore backup")
            print("[Menu] 6. Register user")
        elif Subscriber.SubscriberCheck(CURRENTUSER):
            print("[Menu] 1. Search book")
            print("[Menu] 2. Logout")
        
        option = input("\n")
        if option == "1":
            catalog = Catalog.Catalog()
            catalog.searchBook()
            
        elif option == "2":
            clearConsole()
            CURRENTUSER = 0
            login()

        elif option == "3" and Librarian.librarianCheck(CURRENTUSER):
            addBook()

        elif option == "4" and Librarian.librarianCheck(CURRENTUSER):
            Backup.backupMake()

        elif option == "5" and Librarian.librarianCheck(CURRENTUSER):
            Backup.backupRestoreMenu()

        elif option == "6" and Librarian.librarianCheck(CURRENTUSER):
            register()
        else:
            print("[Menu] Invalid input. Please try again.\n")

setup()
login()
mainMenu()


    
