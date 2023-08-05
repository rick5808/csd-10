'''
Rick McArdle
Cybr 410 WhatAbook
'''

import mysql.connector
from mysql.connector import errorcode

_user_id = ''

def show_menu():
    print()
    print ("MAIN MENU")    
    print ("    1. View Books")
    print ("    2. View Store Locations")
    print ("    3. My Account")
    print ("    4. Exit")
    print ()
    get_main_menu_input()

def show_account_menu():   
    global _user_id
    _user_id = validate_user(_user_id)
    if _user_id == '':
        show_menu()
    else:
        print()    
        print ("Account Menu")
        print ("    1. Wishlist")
        print ("    2. Add Book")
        print ("    3. Main Menu")
        print()  
        get_account_menu_input()

def show_books(cursor):        
    sql = 'select book_id, book_name, details, author from book;'
    cursor.execute(sql)
    books = cursor.fetchall ()
    print (f"-- DISPLAYING BOOKS --")
    for book in books:
        print (f"Book ID: {book[0]}")
        print (f"Book Name: {book[1]}")
        print (f"Details: {book[2]}")
        print (f"Author: {book[3]}")
        print()
    show_menu()

def show_locations():     
    sql = 'select store_id, locale from store;'
    _cursor.execute(sql)
    stores = _cursor.fetchall ()
    print (f"-- DISPLAYING LOCATIONS --")
    for store in stores:
        print (f"Store ID: {store[0]}")
        print (f"Locale: {store[1]}")
        print()
    show_menu()

def get_main_menu_input():
    choice = input ("What do you want do, select option 1,2,3, or 4 to quit: ")
    if choice =="1":
        show_books(_cursor)   
    elif choice == "2":
        show_locations()   
    elif choice == "3":
        show_account_menu()
    elif choice == "4":
        quit()
    else:
        print("Please, you must select 1,2,3, or 4 to quit")
        show_menu()        

def show_wishlist():
    sql = f'''select b.book_id, b.book_name, b.details, b.author 
        from wishlist as w 
        join book as b on w.book_id = b.book_id 
        where w.user_id = {_user_id}
        order by b.book_id;'''
    _cursor.execute(sql)
    wishlist_books = _cursor.fetchall ()
    print()
    print ("-- WISHLIST BOOKS --")
    for book in wishlist_books:
        print (f"Book ID: {book[0]}")
        print (f"Book Name: {book[1]}")
        print (f"Details: {book[2]}")
        print (f"Author: {book[3]}")
        print()
    show_account_menu()

def add_book(user_id):
    try:
        show_books_to_add(user_id)
        get_add_book_input(user_id)
    except Exception as e:
        print(f"Could not add book. Please try again. ({str(e)})") 
    finally:            
        show_account_menu()
    
def get_account_menu_input():     
    choice = input ("Select an option 1, 2, 3: ")
    if choice == "1":        
        show_wishlist()
    elif choice == "2":
        add_book(_user_id)
    elif choice == "3":
        show_menu()   

def validate_user(user_id):
    if user_id != '':
        return user_id 
    else: 
        user_id = input("Please Enter your User ID: ")

        sql = f'SELECT count(*) as user_count FROM user where user_id = {user_id};'
        _cursor.execute(sql)
        record = _cursor.fetchone ()
        count = record[0]
        if count == 0:
            print ('User Not Found')
            return ''
        else:
            print ('User Found')
            return user_id          
                
def show_books_to_add(user_id):
    sql = f'''select book_id, book_name, details, author 
        from book  
        where book_id not in (select book_id from wishlist where user_id = {user_id});'''
    _cursor.execute(sql)
    books = _cursor.fetchall ()
    print (f"-- AVAILABLE BOOKS --")
    for book in books:
        print (f"Book ID: {book[0]}")
        print (f"Book Name: {book[1]}")
        print (f"Details: {book[2]}")
        print (f"Author: {book[3]}")
        print()
     
def get_add_book_input(user_id):
    book_id = input ("Please enter book ID: ")
    sql = f'insert into wishlist (user_id, book_id) values ({user_id}, {book_id});'
    _cursor.execute(sql)
    print("book added!")
    show_account_menu()

def main():
    print ("Welcome To Whatabook")
    print 
     
    config = {
        "user": "whatabook_user",
        "password": "MySQL8IsGreat!",
        "host": "127.0.0.1",
        "database": "whatabook",
        "raise_on_warnings": True
    }     

    try:
        db = mysql.connector.connect(**config)
        print(f"\n Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}.")
        global _cursor
        _cursor = db.cursor ()
        show_menu()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  the supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  the specified database does not exist")
        else:
            print(err)

    finally:
        db.close()



















# Using the special variable
# __name__
if __name__=="__main__":
    main()