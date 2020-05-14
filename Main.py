import Person
import PersonCSV
import BookJSON

CURRENTUSER = 0

def setup():
    userList = PersonCSV.readFromPersonCSV()
    for user in userList:
        user.Sleep()

    bookList = BookJSON.readFromBookJSON()
    for book in bookList:
        book.Sleep()

def register():
    pass
    #naam = input("Hier naam: ")
    #age = input("Hier age: ")
    #land = input("Hier land: ")
    #person = Person(naam, land, leeftijd)
    #person.writeToDatabase()


def login():
    username = input("Please login with your username: ")
    # met username kijken welke class person subclass het is
    # return person.type() aan de mainmenu
    #person = Person(naam, land, leeftijd)
    #person.checkUsername()
    #CURRENTUSER = 

def mainMenu():
    while True:
        if(True):
            print("1. Search book")
            print("2. Logout")
            print("3. Add book")
            print("4. Make backup")
            print("5. Restore backup")
            print("6. Register user")
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


    
