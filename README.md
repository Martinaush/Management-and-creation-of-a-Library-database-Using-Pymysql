# Project_3

Find here an explanation of each script:

  1-. Creation_of_books: it has been downloaded a dataset from github containing load of books. Moreover, it has been modified in order to extract 'bookid', 'title' , 'author' and
'quantityinstock'. The name of the csv is as follows "books.csv"
Note: as books.csv is in the repository this .py do not be executed.

  2-. Create_Database: with this python script we have used the library pymyslq to create a new database called "Library" which has this tables:
  
      - Stocklist: containg information about books available
      
      - Backorderlist: containing orders that were not placed because of lack of availability of the book
      
      - Orderlist: current orders list
      
 Moreover, with this python script we populated "Stocklist" importing data from the csv obtained in Creation_of_Books called "books.csv"
 
  3-. 01_Trigger: this trigger was executed through WorkBench BEFORE UPDATE in the table Orderlist. In specific this trigger sets fulfilled = 1 in orderlist if there is enough availability for this book. Contrary, if there is not it inserts the order in stocklist and fulfilled = 0.
  
  4-. 02_Trigger: this trigger was executed through WorkBench AFTER DELETE in the table Orderlist. In specific, when an order has been returned it updates the quantity in stock from that book in specific (if the order appeared in orderlist table as fulfilled = 1 , i.e. the book were given). 
  
  5-. 01_Store_Procedure: this store procedure was run through Workbench. Moreover, this store procedure goes by the hand with 02_Trigger because of the functionality of this script is to update the waiting list.
  (I.e. if there is someone waiting for a book and its disponibility has been updated, we need to consider if his order could be processed now)
  
  4-. Indexes: it has been created 3 indexes to do the searches in a more efficient way. These indexes have been created on each primary key of each table.
  
  
      
   
