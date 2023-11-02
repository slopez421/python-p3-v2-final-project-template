# lib/helpers.py
from models.reader import Reader

def exit_program():
    print("Goodbye!")
    exit()

def list_readers():
    readers = Reader.get_all()
    for reader in readers:
        print(f"{reader.id}: {reader.name}")

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

def delete_reader():
    name = input("Enter the reader's name you wish to delete:")
    if  reader := Reader.return_by_name(name):
        reader.delete()
        print(f'Reader {name} has been deleted.')
    else:
        print(f'Reader {name} not found.')

def update_reader():
    name = input("Enter reader's name: ")
    if reader := Reader.return_by_name(name):
        try:
            name = input("Enter reader's name: ")
            reader.name = name
            favorite_genre = input("Enter reader's favorite genre: ")
            reader.favorite_genre = favorite_genre
            favorite_book = input("Enter reader's favorite book: ")
            reader.favorite_book = favorite_book
            reader.update()
        except Exception as exc:
            print("Error updating reader: ", exc)
        else:
            print(f"Reader {name} not found.")