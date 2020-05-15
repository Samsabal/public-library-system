import Person

class Subscriber(Person.Person):  
    """This is a subscriber class"""
    def __init__(self, number):
        self.number = number

    def writeToDatabase(self):
        pass


# Librarian, Subscriber, BookItem, LoanItem,LoanAdministaretor