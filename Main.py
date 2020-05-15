import Person
import PersonCSV
import BookJSON
import Librarian
import Subscriber

CURRENTUSER = 0

def setup():
    global userList, bookList
    userList = PersonCSV.readFromPersonCSV()

    for user in userList:
        print(user.username)

    bookList = BookJSON.readFromBookJSON()
    for book in bookList:
        book.Sleep()

def checkUsername(username):
    global userList, CURRENTUSER

    for user in userList:
        if username == user.username:
            CURRENTUSER = user.number
    if CURRENTUSER == 0:
        print("This username does not excist, please try again!")
        login()
        
    

def register():
    pass
    #naam = input("Hier naam: ")
    #age = input("Hier age: ")
    #land = input("Hier land: ")
    #person = Person(naam, land, leeftijd)
    #person.writeToDatabase()


def login():
    username = input("Please login with your username:\n")
    checkUsername(username)  

def mainMenu():
    while True:
        if Librarian.librarianCheck(CURRENTUSER):
            print("1. Search book")
            print("2. Logout")
            print("3. Add book")
            print("4. Make backup")
            print("5. Restore backup")
            print("6. Register user")
        #elif subscriber.subscriberCheck(CURRENTUSER):
        #    print("1. Search book")
        #    print("2. Logout")
        #    print("3. Add book")
        #    print("4. Make backup")
        #    print("5. Restore backup")
        #    print("6. Register user")
        else:
            print("1. Search book")
            print("2. Logout")
        
        option = input("\n")
        if option == "1":
            pass
            
        elif option == "2":
            pass

        elif option == "3":
            pass

        elif option == "4":
            pass

        elif option == "5":
            pass

        elif option == "6":
            pass
        else:
            print("Invalid input. Please try again.\n")

setup()
login()
mainMenu()


    
