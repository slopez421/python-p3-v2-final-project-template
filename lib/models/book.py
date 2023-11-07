from models.__init__ import CURSOR, CONN
from models.reader import Reader
import ipdb

class Book:

    all = {}

    def __init__(self, title, page_count, reader_id, id=None):

        self.title = title
        self.page_count = page_count
        self.reader_id = reader_id
        self.id = id

    def __repr__(self):
        return f"<{self.title} has {self.page_count} pages and belongs to reader {self.reader_id}.>"

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Oops! Title must be a non-empty string.")
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            raise ValueError("Page count must be a number.")
    
    @property
    def reader_id(self):
        return self._reader_id
    
    @reader_id.setter
    def reader_id(self, reader_id):
        if isinstance(reader_id, int) and Reader.return_by_id(reader_id):
            self._reader_id = reader_id
        else:
            raise ValueError("Please make sure reader_id is an integer that references a reader in the database.")
    
    @classmethod
    def create_table(cls):
        sql = """ 
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            page_count INTEGER,
            reader_id INTEGER,
            FOREIGN KEY (reader_id) REFERENCES readers(id))
            """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """ 
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
#ipdb.set_trace()