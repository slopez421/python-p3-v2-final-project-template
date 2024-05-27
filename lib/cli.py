# lib/cli.py

# lib/cli.py

from helpers import (
    exit_program,
    list_all_readers,
    create_reader,
    return_reader_by_choice,
    update_reader,
    delete_reader,
    list_books,
    update_book,
    delete_book,
    create_book
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            all_readers_menu()
        else:
            print("Invalid choice")

def all_readers_menu():
    while True:
        all_readers_menu__text()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "-1":
            main()
        elif choice == "+1":
            create_reader()
        elif choice:
            indiv_reader_choices(choice)
        else:
            print("Invalid choice.")

def indiv_reader_choices(choice):
    return_reader_by_choice(choice)
    reader_id = choice
    while True:
        indiv_reader_details_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "-1":
            all_readers_menu()
        elif choice == "1":
            update_reader(reader_id)
        elif choice == "2":
            delete_reader(reader_id)
            all_readers_menu()
        elif choice == "3":
            book_menu_choices(reader_id)
        else: 
            print("Invalid choice.")

def book_menu_choices(reader_id):
    while True:
        list_books(reader_id)
        book_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "-1":
            indiv_reader_choices(reader_id)
        elif choice == "+1":
            create_book(reader_id)
        elif choice == "1":
            update_book(reader_id)
        elif choice =="2":
            delete_book(reader_id)
        else:
            print("Invalid choice.")
        book_menu_choices(reader_id)


def menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all Readers")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

def all_readers_menu__text():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select the corresponding number to see the reader's details.")
    print("0. Exit the program.")
    print("-1. Go back.")
    print("+1. Add new Reader")
    list_all_readers()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

def indiv_reader_details_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select an option for this reader..")
    print("0. Exit the program.")
    print("-1. Go back.")
    print("1. Update Reader")
    print("2. Delete Reader")
    print("3. See reader's books")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

def book_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please choose an option.")
    print("0. Exit the program.")
    print("-1. Go back.")
    print("+1. Add new book to the library.")
    print("1. Update a book.")
    print("2. Delete a book.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")



if __name__ == "__main__":
    main()

