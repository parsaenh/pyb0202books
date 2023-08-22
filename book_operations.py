
import xlsxwriter as xl
from os import system
clear = lambda : system("cls")

from pickle import load
with open("books_info.info","rb") as books_info:
    books = load(books_info)


# defining an add to exel 
def add_book():
    clear()
    global books                 # global list of all books (optional code)
    book={}
    book["title"]=input("Enter title of the book : ")
    book["author"]=input("Enter author of the book : ")
    book["pages"]=int(input("Enter pages of the book : "))
    book["price"]=float(input("Enter price of the book : "))
    book["isbn"]=input("Enter ISBN of the book : ")
    books.append(book)
    input("Press any key to continue")


def delete_book():
    clear()
    isbn=input("Enter your ISBN to delete book: ")
    for book in books:
        if book["isbn"]==isbn:
            #asking insurance question
            books.remove(book)
            input("Book has been deleted successfully. Press any key to continue")
            break
    else:
        input("This book IS NOT in books database ! Press any key to continue")


def find_book():
    clear()
    isbn=input("Enter ISBN to find your book : ")
    for book in books:
        if book["isbn"]==isbn:
            print("-------------------------------------")
            print(f"Title : {book['title']}")
            print(f"Author : {book['author']}")
            print(f"Pages : {book['pages']}")
            print(f"Price : {book['price']}")
            print(f"ISBN : {book['isbn']}")
            print("-------------------------------------")
            break
    else:
        input("This book IS NOT in books database ! Press any key to continue")    


def list_book():
    clear()
    for book in books:
        print("-------------------------------------")
        print(f"Title : {book['title']}")
        print(f"Author : {book['author']}")
        print(f"Pages : {book['pages']}")
        print(f"Price : {book['price']}")
        print(f"ISBN : {book['isbn']}")
        print("-------------------------------------")
    input("Press any key to continue")


def myfind():
    clear()
    #item_key = input("What is your search basis? : (title/author/pages/price/isbn)")
    pass


def save_books():
    from pickle import dump
    with open("books_info.info","wb") as books_info:
        dump(books,books_info)
        input("Books has been saved successfully! Press any key to continue")
