# lib/helpers.py
from models.reader import Reader

def exit_program():
    print("Goodbye!")
    exit()

def list_readers():
    readers = Reader.get_all()
    for reader in readers:
        print(reader.name)