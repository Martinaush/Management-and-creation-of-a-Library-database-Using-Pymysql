# Project_3

Find here an explanation of each script:

  1-. Creation_of_books: it has been downloaded a dataset from github containing load of books. Moreover, it has been modified in order to extract 'bookid', 'title' , 'author' and
'quantityinstock'. The name of the csv is as follows "books.csv"

  2-. Create_Database: with this python script we have used the library pymyslq to create a new database called "Library" which has this tables:
  
      - Stocklist: containg information about books available
      
      - Backorderlist: containing orders that were not placed because of lack of availability of the book
      
      - Orderlist: current orders list
      
 Moreover, with this python script we populated "Stocklist" importing data from the csv obtained in Creation_of_Books called "books.csv"
      
   
