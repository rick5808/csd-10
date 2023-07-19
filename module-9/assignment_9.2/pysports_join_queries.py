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
    
    sql = '''SELECT p.player_id, p.first_name, p.last_name, t.team_name 
    FROM player p
    INNER JOIN team t ON p.team_id = t.team_id;'''

    cursor = db.cursor ()
    cursor.execute(sql)
    players = cursor.fetchall ()
    print ("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print (f"Player ID: {player[0]}")
        print (f"First Name: {player[1]}")
        print (f"Last Name: {player[2]}")
        print (f"Team Name: {player[3]}")
        print()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  the supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  the specified database does not exist")
    else:
        print(err)

finally:
    db.close()
 