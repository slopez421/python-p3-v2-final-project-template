# lib/helpers.py
from models.reader import Reader
from models.book import Book

def list_all_readers():
    count = 0
    readers = Reader.get_all()
    for reader in readers:
        count +=1
        print(f'{count}: {reader}')

def create_reader():
    name = input("Enter the reader's name: ")
    favorite_genre = input("Enter the reader's favorite genre: " )
    try:
        reader = Reader.create(name, favorite_genre)
        print(f"Success! {reader.name} has been added to the library.")
    except Exception as exc:
        print("Error adding reader: ", exc)

def return_reader_by_choice(id_):
    from cli import all_readers_menu
    reader = Reader.find_by_id(id_)
    if reader:
         print(reader)
    else:
        print(f'Reader {id_} not found.')
        all_readers_menu()


def update_reader(id_):
    if reader := Reader.find_by_id(id_):
        try:
            name = input("Enter the reader's new name: ")
            reader.name = name
            favorite_genre = input("Enter the reader's new favorite genre: ")
            reader.favorite_genre = favorite_genre
            reader.update()
            print(f'Success! Reader {name} has been updated.')
        except Exception as exc:
            print("Error updating reader: ", exc)
    else:
        print(f"Reader {id_} not found.")
        
def delete_reader(id_):
    if reader := Reader.find_by_id(id_):
        try:
            reader.delete()
            print(f"Reader has been deleted.")
        except Exception as exc:
            print("Error deleting reader: ", exc)

def list_books(id_):
    reader = Reader.find_by_id(id_)
    if books := reader.books():
        for book in books:
            print(f'{book.title} has {book.page_count} pages and belongs to {reader.name}.')
    else:
        print("This reader has no books.")

def update_book(reader_id):
    id_ = input("Enter the id of the book you'd like to update: ")
    if book := Book.find_by_id(id_):
        if book.reader_id == int(reader_id):
            try: 
                title = input("Enter the new title for the book: ")
                book.title = title
                page_count = input("Enter the new page count for the book: ")
                book.page_count = int(page_count)
                book.update()
                print(f"Success! {book.title} has been updated.")
            except Exception as exc:
                print("Error updating book: ", exc)
        else:
            print(f"Error! Book {id_} does not belong to this reader.")
    else:
        print(f"Book {id_} does not exist.")

def delete_book(reader_id):
    id_ = input("Enter the id of the book you'd like to delete: ")
    if book := Book.find_by_id(id_):
        if book.reader_id == int(reader_id):
            book.delete()
            print("The book has been deleted.")
        else: 
            print(f"Error! Book {id_} does not belong to this reader.")
    else:
        print(f"Book {id_} does not exist.")

def create_book(reader_id):
    title = input("Enter the title of the book: ")
    page_count = input("Enter the number of pages in this book: ")
    try:
        book = Book.create(title, int(page_count), int(reader_id))
        print(f"Success! {book.title} has been added to the library.")
    except Exception as exc:
        print("Error adding book: ", exc)

def exit_program():
    print("Goodbye!")
    exit()