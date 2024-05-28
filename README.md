### Library CLI Application

Welcome to the reader library!
If you've ever found yourself wanting to keep track of the books you've read but have poor memory (like me!), this application is perfect for you. 

Through CLI menus, you can add Readers to the database or Books that belong to each Reader. You may see all Readers, update a Reader, or delete that Reader if they no longer wish to use the application. 

Similarly, you may add Books belonging to that Reader to track, update a Book, or delete a Book. 

#### CLI Menus

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