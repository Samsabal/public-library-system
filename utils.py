import os

def clearConsole():
    #Clears the console only in Windows
    clear = lambda: os.system("cls")
    clear()