# lib/cli.py

from helpers import (
    exit_program,
    list_readers,
    return_reader_by_id,
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
    print("2. List all books")

def reader_menu_choices():
    print("0. Exit the program.")
    print("Please select the corresponding number to see the reader's details.")
    list_readers()

def reader_details_menu():
    print("Please select an option.")
    print("0. Exit the program.")
    print("1. Update Reader")
    print("2. Delete Reader")
    print("3. See reader's books.")
    
def reader_info_menu():
    reader_menu_choices()
    choice = input("> ")
    while True:
        return_reader_by_id(choice)
        reader_details_menu()


if __name__ == "__main__":
    main()