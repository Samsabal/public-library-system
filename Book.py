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
        self.pages = pages
        self.title = title
        self.year = year

    def writeToDatabase(self, book):
        with open('BookDatabase.json') as json_file:
            data  = json.load(json_file)
            
            book_data = {
                "author": self.author,
                "country": self.country,
                "imageLink": self.imageLink,
                "language": self.language,
                "link": self.link,
                "pages": self.pages,
                "title": self.title,
                "year": self.year
            }
            data.append(book_data)

            self.writeToJson(data)
    
    def writeToJson(self, data):
        with open("BookDatabase.json", 'w',) as f:
            json.dump(data, f, indent=4)
        
    def showBook(self):
        print("[Book] Author: " + self.author)
        print("[Book] Country: " + self.country)
        print("[Book] Image Link: " + self.imageLink)
        print("[Book] Language: " + self.language)
        print("[Book] Link: " + self.link)
        print("[Book] Pages: " + str(self.pages))
        print("[Book] Title: " + self.title)
        print("[Book] Year: " + str(self.year))
        
        if (True):
            input("Would you like loan this book (y/n): ")
        else:
            input("No book available, press any key to go back!")

