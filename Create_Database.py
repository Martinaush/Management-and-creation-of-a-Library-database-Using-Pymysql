#!/usr/bin/env python
# coding: utf-8

# In[108]:


# import the mysql client for python

import pymysql

import string

import re

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


try:

    # Create a cursor object

    cursorInstance = connectionInstance.cursor()                                    


    # SQL Statement to create a database

    sqlStatement = "CREATE DATABASE "+ newDatabaseName  


    # Execute the create database SQL statment through the cursor instance

    cursorInstance.execute(sqlStatement)
    
    
    # Using our database
    
    sqlStatement = "USE " + newDatabaseName
    
    cursorInstance.execute(sqlStatement)
    
    
    # Creating table backorderlist
    
    sqlStatement = """CREATE TABLE `library`.`backorderlist` (
      `backorderid` INT NOT NULL AUTO_INCREMENT,
      `orderid` INT NULL DEFAULT NULL,
      `quantity` INT NULL DEFAULT NULL,
      PRIMARY KEY (`backorderid`));
    """
    
    cursorInstance.execute(sqlStatement)
    
    
    # Creating table orderlist 
    
    sqlStatement = """CREATE TABLE `library`.`orderlist` (
      `orderid` INT NOT NULL AUTO_INCREMENT,
      `bookid` INT NULL DEFAULT NULL,
      `orderername` VARCHAR(45) NULL DEFAULT NULL,
      `ordereraddress` VARCHAR(45) NULL DEFAULT NULL,
      `quantity` INT NULL DEFAULT NULL,
      `fulfilled` INT NULL DEFAULT NULL,
      PRIMARY KEY (`orderid`));
    """
    
    cursorInstance.execute(sqlStatement)
    
    
    # Creating table stocklist
    
    sqlStatement = """CREATE TABLE `library`.`stocklist` (
      `bookid` INT NOT NULL,
      `booktitle` VARCHAR(300) NULL DEFAULT NULL,
      `author` VARCHAR(700) NULL DEFAULT NULL,
      `quantityinstock` INT NULL DEFAULT NULL,
      PRIMARY KEY (`bookid`));
      """

    cursorInstance.execute(sqlStatement)
    
    
    
    # Populating table stocklist

    
    import string
    
    file = open('books.csv', encoding = "utf8")

    count = 0

    for book in file:

        book = book.strip()
        
        count += 1
        
        books2 = []

        if count == 1:

            continue

        books = book.split(",")
        
        # Eliminating punctuation signs
        
        for e in books:
            
            new_string = re.sub(r'[^\w\s]', '', e)
            
            books2.append(new_string)

        sqlStatement = "INSERT INTO stocklist VALUES('%s', '%s','%s', %d);"%(books2[1],books2[2],books2[3],int(books2[4]))
        
        cursorInstance.execute(sqlStatement)
        
        connectionInstance.commit()
    

except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    connectionInstance.close()

