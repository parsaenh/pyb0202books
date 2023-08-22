# V 3.2.0
import book_operations as bo




#----------------------main----------------------


while True:
    bo.clear()
    print("===========================================")
    print("Press A to add a Book")
    print("Press D to delete a Book")
    print("Press F to find a Book")
    print("Press L to list all Book")
    print("Press S to save all Book")
    print("Press Q to quit application")
    print("===========================================")
    choice=input("enter your choice ").upper()
    if   choice == "A" :
        bo.add_book()
    elif choice == "D" :
        bo.delete_book()
    elif choice == "F" :
        bo.find_book()
    elif choice == "L" :
        bo.list_book()
    elif choice == "S" :
        bo.save_books()
    elif choice == "Q" :
        print("See you Later!")
        break
    else:
        input("Wrong Choice! Press any key to continue")
