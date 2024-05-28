### Library CLI Application

Welcome to the reader library!
If you've ever found yourself wanting to keep track of the books you've read but have poor memory (like me!), this application is perfect for you. 

Through CLI menus, you can add Readers to the database or Books that belong to each Reader. You may see all Readers, update a Reader, or delete that Reader if they no longer wish to use the application. 

Similarly, you may add Books belonging to that Reader to track, update a Book, or delete a Book. 

## CLI Menus

The CLI launches with an introductory menu (menu() )that gives the user two choices: you can exit the program or see all Readers. 

If the reader chooses to see all readers, they are brought to the next menu (all_readers_menu() ). 

The all_readers_menu() calls in text options that correspond to an Ifelif set of options so each number that the User presses then calls different functions. 

In this menu, the user is presented with the option to exit the program, go back to the previous menu, add a new Reader, while simulatanously being presented with all the readers in the database. The corresponding number in the list next to the Reader is actually the User ID so choosing the option (i.e. the id choice) is then saved into the next menu as a variable so we can pass it into the following functions. 

If the user chooses to add a new reader, they are presented with a series of input() functions that validates user input through the helper function create_reader() listed in helpers.py. 
Choosing any of the numerical options will present the user with the a new menu (indiv_reader_choices) that displays options for an individual reader. Here, the user can update the reader, delete the reader, or see the reader's associated books. 

Updating the Reader produces another series of input() entries for validating user input that connect to a corresponding function int the helper.py file. The user is then looped back to the same menu once the new Reader is added and is displayed in the list of Readers. 

Deleting a Reader will delete that Reader from the database and delete it from the corresponding dictionary of Reader objects in reader.py.

If the user chooses to see all books associated with the Reader, the reader's id (aka the number) is passed down to the next menu as a saved variable so we can see the books where reader_id = the choice number. 

This new menu is book_menu_choices(). It calls in a list of books associated with the current reader and produces an option for the user to either add a new book to the database, update a current book in the databse, or delete a book in the database. However, through validation input, a Reader can't delete a book that either doesn't exist or belongs to another Reader. 

Every menu has the choice to go back to the previous menu to keep the user looped until they decide to exit the program.

## Data Models

There are two files for our One-To-Many relationships. 
The reader.py is our Reader class. Every Reader intilializes with a name and favorite_genre that are saved as properties with setter functions in place to validate user input. The id for each object is handled by our ORM methods. The object is mapped to the Readers table as a new row and saved to the Reader.all dictionary. 

The book.py is our Book class. Every Book intilializes with a title, page_count, and reader_id that are saved as properties with setter functions in place to validate user input. The id for each object is handled by our ORM methods. The object is mapped to the Books table as a new row and saved to the Book.all dictionary. Our reader_id attribute is also specified as a foreign key in the create_table method when it is mapped to the table so it relates to the id in the Reader table. 

## Helper functions

Our helper.py file imports functions from both the Book class and the Reader class. 

list_all_readers() returns all readers in the Reader database.

creater_reader() takes in user input and saves the user's answers as attributes to create a new Reader instance and persists that object to the Reader table while validating user input.

return_reader_by_choice(choice) takes in the user's choice, passed down as the id for the Reader, and returns one reader from the database whose ID matches the choice. 

update_reader(id_) takes in user input and saves the values to the Python object whose id matches the Reader choice. Then it persists that data to the Readers table. 

delete_reader(id_) is passed in the user choice (id) and deletes the Reader instance whose values match the corresponding row in the database. The function then deletes the instance from the dictionary and the row. 

list_books(id_) takes in the user's choice as the current Reader id and returns a list of books associated with that Reader. 

create_book(reader_id) takes in user input and saves the user's answers as attributes to create a new Book instance and persists that object to the Book table while validating user input. By passing in reader_id, we also ensure this book is automatically assigned to the current Reader whose menu we're in. 

update_book(reader_id) takes in user input and saves the values to the Python object whose reader_id matches the Reader choice. Then it persists that data to the Books table.

delete_book(reader_id) is passed in the user choice (reader_id) and deletes the Book instance whose values match the corresponding row in the database. The function then deletes the instance from the dictionary and the row while ensuring the reader_id matches the current Reader the user is in. 