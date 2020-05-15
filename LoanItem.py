import LoanAdministration

class LoanItem(LoanAdministration.LoanAdministration):  
    """This is a LoanItem class"""
    def __init__(self, subscriberNumber, days, ISBN):
        self.subscribernumber = subscriberNumber
        self.days = days
        self.ISBN = ISBN
