# lib/helpers.py
from models.reader import Reader
from models.book import Book

def exit_program():
    print("Goodbye!")
    exit()

def list_readers():
    readers = Reader.get_all()
    for reader in readers:
        print(f"{reader.id}: {reader.name}")

def return_reader_by_id(id_):
    reader = Reader.return_by_id(id_)
    print(reader) if reader else print(f'Reader {id_} not found.')

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
    id_ = input("Enter the reader's id you wish to delete:")
    if  reader := Reader.return_by_id(id_):
        reader.delete()
        print(f'Success! Reader {id_} has been deleted.')
    else:
        print(f'Reader {id_} not found.')

def update_reader():
    id_ = input("Enter reader's id: ")
    if reader := Reader.return_by_id(id_):
        try:
            name = input("Enter reader's new name: ")
            reader.name = name
            favorite_genre = input("Enter reader's new favorite genre: ")
            reader.favorite_genre = favorite_genre
            favorite_book = input("Enter reader's new favorite book: ")
            reader.favorite_book = favorite_book
            reader.update()
            print(f'Success! {reader.name} has been updated.')
        except Exception as exc:
            print("Error updating reader: ", exc)
    else:
        print(f"Reader {id_} not found.")

def list_books_by_reader(id_):
    if reader := Reader.return_by_id(id_):
        books = reader.books()
        for book in books:
            print(book)
    else:
        print(f'Reader {id_} not found.')

def create_book(reader_id):
    title = input("Enter the book's title: ")
    page_count = input("Enter the book's page count: ")
    try:
        book = Book.create(title, int(page_count), int(reader_id))
        print(f'Success! {book.title} has been added.')
    except Exception as exc:
        print('Error adding new book: ', exc)