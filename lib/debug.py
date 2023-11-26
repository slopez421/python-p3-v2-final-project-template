#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.reader import Reader
from models.book import Book
import ipdb

Reader.drop_table()
Reader.create_table()
Book.drop_table()
Book.create_table()

alyssa = Reader.create("Alyssa", "Horror", "Harry Potter")
yax = Reader.create("Yaxenis", "Fantasy", "Game of Thrones")
shania = Reader.create("Shania", "Young Adult Fiction", "The Cruel Prince")

Book.create_table()
book_1 = Book.create("Cruel Prince", 102, 3)
book_2 = Book.create("They Both Die at the End", 1001, 2)
book_3 = Book.create("ACOSF", 1211, 1)
ipdb.set_trace()
