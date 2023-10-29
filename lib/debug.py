#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.reader import Reader
import ipdb

Reader.drop_table()
Reader.create_table()

alyssa = Reader.create("Alyssa", "Horror", "Harry Potter")
yax = Reader.create("Yaxenis", "Fantasy", "Game of Thrones")
shania = Reader.create("Shania", "Young Adult Fiction", "The Cruel Prince")



ipdb.set_trace()
