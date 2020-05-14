class Book():  
    """"This is a book class"""
    def __init__(self, author, country, imageLink, language, link, pages, 
    title, year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.title = title
        self.year = year
    
    #def writeToDatabase():
        
    def Sleep(self):
        print(self.author + " slaapt")