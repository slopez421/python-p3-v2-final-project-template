from models.book import Book
from models.reader import Reader

def seed_data():

    Reader.drop_table()
    Book.drop_table()
    Reader.create_table()
    Book.create_table() 
    
    Reader.create("Susan", "Horror")
    Reader.create("Jeff", "Fantasy")
    Reader.create("Shania", "Romance")
    Book.create("The Cruel Prince", 300, 1)
    Book.create("The Wicked King", 400, 1)
    Book.create("The Queen of Nothing", 500, 1)
    Book.create("A Court of Thorns and Roses", 400, 2)
    Book.create("A Court of Mist and Fury", 600, 2)
    Book.create("Volo's Guide to Monsters", 250, 3)
    Book.create("Mordenkainen's Tome of Foes", 400, 3)

seed_data()
print("Database seeded.")