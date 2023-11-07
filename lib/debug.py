#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.reader import Reader
from models.book import Book
import ipdb

Reader.drop_table()
Reader.create_table()

alyssa = Reader.create("Alyssa", "Horror", "Harry Potter")
yax = Reader.create("Yaxenis", "Fantasy", "Game of Thrones")
shania = Reader.create("Shania", "Young Adult Fiction", "The Cruel Prince")

Book.create_table()
book_1 = Book("Cruel Prince", 102, 3)
ipdb.set_trace()
