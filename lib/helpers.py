# lib/helpers.py
from models.reader import Reader

def exit_program():
    print("Goodbye!")
    exit()

def list_readers():
    readers = Reader.get_all()
    for reader in readers:
        print(reader.name)

def return_reader_by_name():
    name = input("Enter the reader's name: ")
    reader = Reader.return_by_name(name)
    print(reader) if reader else print(f'Reader {name} not found.')

def return_reader_by_favorite_book():
    book = input("Enter the reader's favorite book: ")
    reader = Reader.return_by_favorite_book(book)
    print(reader) if reader else print(f'There are no readers whose favorite book is {book}')

def create_reader():
    name = input('Enter the reader\'s name: ')
    favorite_genre = input('Enter the reader\'s favorite genre: ')
    favorite_book = input('Enter the reader\'s book: ')
    try:
        reader = Reader.create(name, favorite_genre, favorite_book)
        print(f'Success! {reader}')
    except Exception as exc:
        print("Error creating reader: ", exc)