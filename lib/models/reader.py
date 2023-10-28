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
        
