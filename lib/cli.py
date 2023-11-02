# lib/cli.py

from helpers import (
    exit_program,
    list_readers,
    return_reader_by_name,
    return_reader_by_favorite_book,
    create_reader,
    delete_reader,
    update_reader
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_readers()
            reader_info_menu()
        #elif choice == "2":
            #return_reader_by_name()
        #elif choice =="3":
        # return_reader_by_favorite_book()
        # elif choice == "4":
        # create_reader()
        # elif choice =="5":
        # delete_reader()
        # elif choice == "6":
        # update_reader()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all Readers")
""" print("2. Find a reader by name.")
    print("3. Find a reader by their favorite book.")
    print("4. Create a new reader.")
    print("5. Delete reader by name.")
    print("6. Update reader by name.")"""

def reader_menu_choices():
    print("Please select the corresponding number to see the reader's details.")
    list_readers()

    
def reader_info_menu():
    print("Select a reader to see the details.")
    choice = input("> ")
    while True:
        if choice == "1":
            print('1. Pressed.')


if __name__ == "__main__":
    main()