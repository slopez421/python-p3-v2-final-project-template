# lib/cli.py

from helpers import (
    exit_program,
    list_readers,
    return_reader_by_id,
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
            reader_menu_choices()
            while True:
                choice = input("> ")
                if choice == "0":
                    exit_program()
                elif choice:
                    return_reader_by_id(choice)
                    while True:
                        reader_details_menu()
                        choice = input("> ")
                        if choice == "0":
                            exit_program()
                        elif choice == "1":
                            update_reader()
                        elif choice == "2":
                            delete_reader()
                        else:
                            print("Invalid choice.")
                else:
                    print("invalid choice.")
                reader_menu_choices()
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
        menu()
        choice = input("> ")


def menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all Readers")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

def reader_menu_choices():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select the corresponding number to see the reader's details.")
    print("0. Exit the program.")
    list_readers()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

def reader_details_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select an option.")
    print("0. Exit the program.")
    print("1. Update Reader")
    print("2. Delete Reader")
    print("3. See reader's books")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    

if __name__ == "__main__":
    main()