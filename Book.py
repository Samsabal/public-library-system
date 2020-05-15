import json

class Book():  
    """This is a book class"""
    def __init__(self, author, country, imageLink, language, link, pages, 
    title, year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.title = title
        self.year = year
    
    def writeToDatabase(self, book):
        self.book = book
        jsonData = self.book

        with open("BookDatabase.json", 'w',) as outfile:
            json.dump(jsonData, outfile)
           
            json_writer.writerow([self.author, self.country, self.imageLink, self.language, self.link, self.pages, 
            self.title, self.year])
