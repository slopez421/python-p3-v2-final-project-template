# lib/cli.py

from helpers import (
    exit_program,
    list_readers,
    return_reader_by_id,
    create_reader,
    delete_reader,
    update_reader,
    list_books_by_reader,
    create_book
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
                elif choice == "00":
                    create_reader()
                elif choice:
                    return_reader_by_id(choice)
                    reader_id_choice = choice
                    while True:
                        reader_details_menu()
                        choice = input("> ")
                        if choice == "0":
                            exit_program()
                        elif choice == "1":
                            update_reader(reader_id_choice)
                        elif choice == "2":
                            delete_reader(reader_id_choice)
                            # have to find a way to loop back to the previous menu once deleted.
                        elif choice == "3":
                            list_books_by_reader(reader_id_choice)
                        elif choice == "4":
                            create_book(reader_id_choice)
                        else:
                            print("Invalid choice.")
                else:
                    print("Invalid choice.")
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
    print("00. Add new Reader")
    list_readers()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

def reader_details_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select an option.")
    print("0. Exit the program.")
    print("1. Update Reader")
    print("2. Delete Reader")
    print("3. See reader's books")
    print("4. Add a new book to reader's library")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    

if __name__ == "__main__":
    main()