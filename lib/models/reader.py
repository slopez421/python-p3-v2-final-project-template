from models.__init__ import CURSOR, CONN

class Reader: 
    all = {}
    
    def __init__(self, name, favorite_genre, id = None):
        self.name = name
        self.favorite_genre = favorite_genre
        self.id = id
    
    def __repr__(self):
        return f"{self.name}'s favorite genre is {self.favorite_genre}."
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("name should be a non-empty string.")
        
    @property
    def favorite_genre(self):
        return self._favorite_genre
    
    @favorite_genre.setter
    def favorite_genre(self, favorite_genre):
        if isinstance(favorite_genre, str) and len(favorite_genre):
            self._favorite_genre = favorite_genre
        else:
            raise ValueError("favorite_genre should be a non-empty string.")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTs readers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            favorite_genre TEXT
            )"""
    
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
            INSERT INTO readers (name, favorite_genre)
            VALUES (?, ?)
            """
        
        CURSOR.execute(sql, (self.name, self.favorite_genre))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, favorite_genre):
        reader = cls(name, favorite_genre)
        reader.save()
        return reader
    
    def update(self):
        sql = """
            UPDATE readers
            SET name = ?, favorite_genre = ?
            WHERE id = ?        
        """

        CURSOR.execute(sql, (self.name, self.favorite_genre, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM readers
            WHERE id = ? """
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        reader = cls.all.get(row[0])
        if reader:
            reader.name = row[1] 
            reader.favorite_genre = row[2]
        else:
            reader = cls(row[1], row[2])
            reader.id = row[0]
            cls.all[reader.id] = reader
        return reader

    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM readers"""
       
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM readers
            WHERE id = ?"""
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM readers
            WHERE name = ?"""
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def books(self):
        from models.book import Book
        sql = """
            SELECT * FROM books
            WHERE reader_id = ?"""
        
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Book.instance_from_db(row) for row in rows]

   
        