#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Recreation of a menu to interact with the database

import pymysql

def print_menu():
    
    print("*"*30)
    
    print("MENU")
    
    print("*"*30)
    
    print("0-. Exit the menu")
    
    print("1-. Place an order")
    
    print("2-. Search a book by its id (to see its disponibility)")
    
    print("3-. An order has been returned")
    


def Menu():
    
    option = -1 # Key of the menu
    
    
    # Create a connection object

    databaseServerIP  = "127.0.0.1"  # IP address of the MySQL database server

    databaseUserName  = "root"   # User name of the database server

    databaseUserPassword = ""   # Password for the database user


    newDatabaseName = "Library" # Name of the database that is to be created

    cusrorType = pymysql.cursors.DictCursor

    connectionInstance = pymysql.connect(host=databaseServerIP, 
                                         user=databaseUserName, 
                                         password=databaseUserPassword,
                                         cursorclass=cusrorType)
    
    # Create a cursor object

    cursorInstance = connectionInstance.cursor()      
    
    # Using our database
    
    sqlStatement = "USE " + newDatabaseName
    
    cursorInstance.execute(sqlStatement)
    
    
    
    # Checking value passed
    
    while option != 0:
        
        option = -1
        
        # Printing menu
    
        print_menu()
        
        while True:
        
            try:

                while option < 0 or option > 5:
                
                    option = input("Please give me what you want to do: \t")

                    option = int(option)

                    if option < 0 or option > 5:

                        print("Please give me an appropiate number... ")

                break

            except:

                continue

        
        if option == 1:
            
            bookid = int(input("Please tell me the desire id book\t"))
            
            # Checking if the id exists
                
            sqlStatement = "SELECT * FROM stocklist WHERE stocklist.bookid = %d"%bookid
                
            cursorInstance.execute(sqlStatement)
                
            rows = cursorInstance.fetchall()
                
            if len(rows) == 0:
                    
                print("\n")
                
                print("-"*38)

                print("Exeception occured: No book under this id")

                print("-"*38)

                print("\n")     
                
                pass
                
            # If the book exists
            
            else:
                
                name = input("Please give me your name\t")

                address = input("Please tell me your address\t")

                quantity = int(input("Please give me the quantity of books you desire\t"))

                sqlStatement = "INSERT INTO orderlist(bookid, orderername, ordereraddress, quantity) VALUES (%d, '%s', '%s', %d)"                         % (bookid, name, address, quantity)

                cursorInstance.execute(sqlStatement)

                connectionInstance.commit()
            
            
        if option == 2:
            
            bookid = int(input("Please give me your book: \t"))
            
            try: 
            
                sqlStatement = "SELECT * FROM stocklist WHERE stocklist.bookid = %d" %bookid

                cursorInstance.execute(sqlStatement)

                rows = cursorInstance.fetchall()

                dicti = rows[0]

                print("\n")

                print("-"*38)

                print("Bookd id: %d" % dicti['bookid'])

                print("Booktitle: %s" % dicti['booktitle'])

                print("Author: %s"% dicti['author'])

                print("Quantity in Stock: %d"%dicti['quantityinstock'])

                print("-"*38)

                print("\n")
                
            except Exception as e:
                
                print("\n")
                
                print("-"*38)

                print("Exeception occured: No book under this id")
                      
                print("-"*38)

                print("\n")     
                
                pass
            
        
        if option == 3:
            
            order = int(input("Please tell me your orderid to return your book: \t"))
            
            # Checking if the order exists and obtaining the bookid
                
            sqlStatement = "SELECT * FROM orderlist WHERE orderlist.orderid = %d"%order
                
            cursorInstance.execute(sqlStatement)
                
            rows = cursorInstance.fetchall()
                
            if len(rows) == 0:
                    
                print("\n")
                
                print("-"*38)

                print("Exeception occured: No order under this id")

                print("-"*38)

                print("\n")     
                
                pass
            
            else:
                
                dicti = rows[0]
                
                bookid = dicti['bookid']
                
                # We delete the order from the table
                
                sqlStatement = "DELETE FROM orderlist WHERE orderlist.orderid = %d;"%order
                
                cursorInstance.execute(sqlStatement)
                
                connectionInstance.commit()
                
                # We call the store procedure to update the waiting list (if any update)
                
                sqlStatement = "call library.waiting_list(%d, @PEOPLE);"%(bookid)
                
                cursorInstance.execute(sqlStatement)
                
                connectionInstance.commit()
                
                sqlStatement2 = "select @PEOPLE;"
                
                cursorInstance.execute(sqlStatement2)
                
                people = cursorInstance.fetchall()
                
                print("There have been updated from the waiting list ",people, "people ")
                
                connectionInstance.commit()
                
                
Menu()        

