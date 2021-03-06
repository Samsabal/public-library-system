import Person
import PersonCSV
import BookJSON
import Librarian
import Subscriber
import Backup
import Book
import BookItem
import BookItemCSV
import LoanItem
import Catalog
from random import randint

CURRENTUSER = 0

def setup():
    global userList, bookList
    userList = PersonCSV.readFromPersonCSV()
    bookList = BookJSON.readFromBookJSON()

def checkUsername(username):
    global userList, CURRENTUSER

    for user in userList:
        if username == user.username:
            CURRENTUSER = user.number
            Book.setCurrentUses(CURRENTUSER)
    if CURRENTUSER == 0:
        print("[Login] This username does not exist, please try again!")
        login()

def register():
    number = int(userList[-1].number) + 1
    print("[Register] Register a person by filling in the information.")

    while True:
        gender = input("[Register] Gender (male/female): ")
        if gender == "male" or gender == "female":
            break
        print("[Register] Invalid input, please try again!")

    nameSet = input("[Register] NameSet: ")
    givenName = input("[Register] GivenName: ")
    surname = input ("[Register] Surname: ")
    streetAddress = input("[Register] Street Address: ")
    zipCode = input("[Register] Zip Code: ")
    city = input("[Register] City: ")
    emailAddress = input("[Register] Email Address: ")
    userName = input("[Register] Username: ")
    telephoneNumber = input("[Register] Telephone Number: ")
    
    while True:
        personType = input("[Register] Is this person a Librarian or Subscriber (librarian/subscriber): ")
        if personType == "librarian" or personType == "subscriber":
            break
        print("[Register] Invalid input, please try again!")
    
    person = Person.Person(number, gender, nameSet, givenName, surname,
    streetAddress, zipCode, city, emailAddress, userName, telephoneNumber)
    person.writeToDatabase(personType)
    print("[Register]\n[Register] Register Successful\n[Register]")
    setup()

def addBook():
    print("[Book] Add a Book by filing in the information.")
    author = input("[Book] Author: ")
    country = input("[Book] Country: ")
    imageLink = input("[Book] ImageLink: ")
    language = input ("[Book] Language: ")
    link = input("[Book] Link: ")

    while True:
        try:
            pages = int(input("[Book] Pages: "))
        except ValueError:
            print("[Book] Invalid number, please try again.")
        else:
            break
    
    title = input("[Book] Title: ")

    while True:
        try:
            year = int(input("[Book] Year: "))
        except ValueError:
            print("[Book] Invalid number, please try again.")
        else:
            break

    while True:
        try:
            ISBN = int(input("[Book] ISBN: "))
        except ValueError:
            print("[Book] Invalid number, please try again.")
        else:
            break

    while True:
        try:
            copies = int(input("[Book] Copies: "))
        except ValueError:
            print("[Book] Invalid number, please try again.")
        else:
            break

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
        
        option = input("[Menu]\n[Menu] Choice: ")
        if option == "1":
            catalog = Catalog.Catalog()
            catalog.searchBook()
            
        elif option == "2":
            setup()
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
            print("[Menu] Invalid input. Please try again.")

setup()
login()
mainMenu()


    
