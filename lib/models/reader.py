from models.__init__ import CURSOR, CONN

class Reader: 
    all = {}

    def __init__(self, name, favorite_genre, favorite_book, id=None):

        self.name = name
        self.favorite_genre = favorite_genre
        self.favorite_book = favorite_book
    
    def __repr__(self):
        return f"<Reader {self.name}'s favorite book is {self.favorite_book}. Reader {self.name}'s favorite genre is {self.favorite_genre}."
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else: 
            raise ValueError("Please enter a non-empty string.")
   
    @property
    def favorite_genre(self):
        return self._favorite_genre
    
    @favorite_genre.setter
    def favorite_genre(self, favorite_genre):
        if isinstance(favorite_genre, str) and len(favorite_genre):
            self._favorite_genre = favorite_genre
        else: 
            raise ValueError("Please enter a non-empty string.")
    
    @property
    def favorite_book(self):
        return self._favorite_book
    
    @favorite_book.setter
    def favorite_book(self, favorite_book):
        if isinstance(favorite_book, str) and len(favorite_book):
            self._favorite_book = favorite_book
        else: 
            raise ValueError("Please enter a non-empty string.")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS readers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            favorite_genre TEXT,
            favorite_book TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS readers
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO readers (name, favorite_genre, favorite_book)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.favorite_genre, self.favorite_book))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        ##Look this up
    

