
class Person():  
    """"This is a person class"""
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
    
    #def writeToDatabase():
        

    
    def Sleep(self):
        print(self.username + " slaapt")