import Person
import PersonCSV
import BookJSON
import Librarian
import Subscriber
import Backup

CURRENTUSER = 0

def setup():
    global userList, bookList
    userList = PersonCSV.readFromPersonCSV()

    for user in userList:
        pass
        #user.Sleep()

    bookList = BookJSON.readFromBookJSON()
    for book in bookList:
        pass
        #book.Sleep()

def checkUsername(username):
    global userList, CURRENTUSER

    for user in userList:
        if username == user.username:
            CURRENTUSER = user.number
    if CURRENTUSER == 0:
        print("This username does not exist, please try again!")
        login()
        
    

def register():
    number = 99  #This needs to be a genarated number
    print("Register a person by filling in the information.\n")
    gender = input("Gender (male/female): ")
    nameSet = input("NameSet: ")
    givenName = input("GivenName: ")
    surname = input ("Surname: ")
    streetAddress = input("Street Address: ")
    zipCode = input("Zip Code: ")
    city = input("City: ")
    emailAddress = input("Email Address: ")
    userName = input("Username: ")
    telephoneNumber = input("Telephone Number: ")
    
    personType = input("Is this person a Librarian or Subscriber (librarian/subscriber):")
    if personType != "librarian" and personType != "subscriber":
        print("Invalid input, please try again!")
        personType
    else:
        person = Person.Person(number, gender, nameSet, givenName, surname,
        streetAddress, zipCode, city, emailAddress, userName, telephoneNumber)
        person.writeToDatabase(personType)

def login():
    username = input("Please login with your username: ")
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
            Backup.backupMake()

        elif option == "5":
            pass

        elif option == "6":
            register()
        else:
            print("Invalid input. Please try again.\n")

setup()
login()
mainMenu()


    
