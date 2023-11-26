# lib/cli.py

from helpers import (
    exit_program,
    list_readers,
    return_reader_by_id,
    create_reader,
    delete_reader,
    update_reader,
    list_books_by_reader,
    create_book,
    update_book
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            reader_menu()
        else:
            print("Invalid choice")
        menu()
        choice = input("> ")

def reader_menu():
            reader_menu_choices()
            while True:
                choice = input("> ")
                if choice == "0":
                    exit_program()
                elif choice == "00":
                    main()
                elif choice == "000":
                    create_reader()
                elif choice:
                    indiv_reader_choices(choice)
                else:
                    print("Invalid choice.")
                reader_menu_choices()
                
def indiv_reader_choices(choice):
                    return_reader_by_id(choice)
                    reader_id_choice = choice
                    while True:
                        reader_details_menu()
                        choice = input("> ")
                        if choice == "0":
                            exit_program()
                        elif choice == "00":
                            reader_menu()
                        elif choice == "1":
                            update_reader(reader_id_choice)
                        elif choice == "2":
                            delete_reader(reader_id_choice)
                        elif choice == "3":
                            list_books_by_reader(reader_id_choice)
                            while True:
                                book_menu()
                                choice = input("> ")
                                if choice == "00":
                                    create_book(reader_id_choice)
                                    list_books_by_reader(reader_id_choice)
                                elif choice == "0":
                                    exit_program()
                                elif choice == "1":
                                    update_book(reader_id_choice)
                        elif choice == "5":
                            print("Implement delete book.")
                        else:
                            print("Invalid choice.")

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
    print("00. Go back.")
    print("000. Add new Reader")
    list_readers()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

def reader_details_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select an option.")
    print("0. Exit the program.")
    print("00. Go back.")
    print("1. Update Reader")
    print("2. Delete Reader")
    print("3. See reader's books")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
def book_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please choose an option.")
    print("0. Exit the program.")
    print("00. Add new book to the library.")
    print("1. Update a book.")
    print("2. Delete a book.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
    main()