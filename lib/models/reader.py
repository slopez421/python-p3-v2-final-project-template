from models.__init__ import CURSOR, CONN

class Reader: 
    all = {}

    def __init__(self, name, favorite_genre, favorite_book, id=None):

        self.name = name
        self.favorite_genre = favorite_genre
        self.favorite_book = favorite_book
        self.id = id
    
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
            DROP TABLE IF EXISTS readers;
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
    
    @classmethod
    def create(cls, name, favorite_genre, favorite_book):
        reader = cls(name, favorite_genre, favorite_book)
        reader.save()
        return reader

    def update(self):
        sql = """
            UPDATE readers SET name = ?, favorite_genre = ?, favorite_book = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.favorite_genre, self.favorite_book, self.id))
        CONN.commit()
  
    def delete(self):
        sql = """
            DELETE FROM readers
            WHERE name = ?
        """
        
        CURSOR.execute(sql, (self.name, ))
        CONN.commit()
         
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def return_instance_from_db(cls, row):

        reader = cls.all.get(row[0])

        if reader:
            reader.name = row[1]
            reader.favorite_genre = row[2]
            reader.favorite_book = row[3]
        else: 
            reader = cls(row[1], row[2], row[3])
            reader.id = row[0]
            cls.all[reader.id] = reader

        return reader
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM readers
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.return_instance_from_db(row) for row in rows]
    
    @classmethod
    def return_by_id(cls, id):
        sql = """
            SELECT * FROM readers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id, )).fetchone() 
        return cls.return_instance_from_db(row) if row else None
    
    @classmethod
    def return_by_favorite_book(cls, favorite_book):
        sql = """
            SELECT * FROM readers
            WHERE favorite_book = ?
        """

        row = CURSOR.execute(sql, (favorite_book, )).fetchone() 
        return cls.return_instance_from_db(row) if row else None
    
    def books(self):
        from models.book import Book
        sql = """
            SELECT *
            FROM books 
            WHERE reader_id = ?
            """
        CURSOR.execute(sql, (self.id,))

        rows = CURSOR.fetchall()
        return [Book.return_instance_from_db(row) for row in rows]