# lib/cli.py

from helpers import (
    exit_program,
    list_readers,
    return_reader_by_name,
    return_reader_by_favorite_book,
    create_reader
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_readers()
        elif choice == "2":
            return_reader_by_name()
        elif choice =="3":
            return_reader_by_favorite_book()
        elif choice == "4":
            create_reader()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all readers.")
    print("2. Find a reader by name.")
    print("3. Find a reader by their favorite book.")
    print("4. Create a new reader.")
    print("5. Find book by name.")


if __name__ == "__main__":
    main()