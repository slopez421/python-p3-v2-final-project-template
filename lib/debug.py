#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.reader import Reader
from models.book import Book
import ipdb

def reset_database():

    Reader.drop_table()
    Book.drop_table()

    Reader.create_table()
    Book.create_table()

    Reader.create("Susan", "Horror")
    Reader.create("Jeff", "Fantasy")
    Reader.create("Shania", "Romance")
    Book.create("The Cruel Prince", 300, 1)
    Book.create("The Wicked King", 400, 2)
    Book.create("The Queen of Nothing", 500, 3)
    
reset_database()
ipdb.set_trace()
