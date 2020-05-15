import PersonCSV
import Librarian
import Subscriber

class Person():  
    """This is a person class"""
    def __init__(self, number, gender, nameSet, givenname, surname, streetaddress, 
    zipcode, city, emailAddress, username, telephonenumber):
        self.number = number
        self.gender = gender
        self.nameSet = nameSet
        self.givenName = givenname
        self.surname = surname
        self.streetAddress = streetaddress
        self.zipCode = zipcode
        self.city = city
        self.emailAddress = emailAddress
        self.username = username
        self.telephonenumber = telephonenumber
        
    def Sleep(self):
        print(self.username + " slaapt")

    def writeToDatabase(self, personType):
        row_contents = [self.number, self.gender, self.nameSet, self.givenName, self.surname,
        self.streetAddress, self.zipCode, self.city, self.emailAddress, self.username, self.telephonenumber]
        
        PersonCSV.writeToPersonCSV(row_contents)
        self.librarianOrSubscriber(personType)

    def librarianOrSubscriber(self, personType):
        if personType == "librarian":
            librarian = Librarian.Librarian(self.number)
            librarian.writeToDatabase()
        else:
            subscriber = Subscriber.Subscriber(self.number)
            subscriber.writeToDatabase()
            
