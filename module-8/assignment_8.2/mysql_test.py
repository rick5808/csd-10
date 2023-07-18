'''
Author: Rick McARdle
'''
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print(f"\n Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}.")

    input("\n\a Press any key to continue...") 
     
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  the supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  the specified database does not exist")

    else:
        print(err)

finally:
    db.close()



 