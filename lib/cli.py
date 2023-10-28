# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all readers.")
    print("2. Find a reader by name.")
    print("3. Find a reader by id.")
    print("4. List all books.")
    print("5. Find book by name.")


if __name__ == "__main__":
    main()
