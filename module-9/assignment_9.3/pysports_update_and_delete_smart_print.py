'''
Author: Rick McARdle
'''
import mysql.connector
from mysql.connector import errorcode

def print_players (cursor, operation):
    sql = '''SELECT p.player_id, p.first_name, p.last_name, t.team_name 
    FROM player p
    INNER JOIN team t ON p.team_id = t.team_id
    ORDER BY p.player_id;'''
    cursor.execute(sql)
    players = cursor.fetchall ()
    print (f"-- DISPLAYING PLAYERS AFTER {operation} --")
    for player in players:
        print (f"Player ID: {player[0]}")
        print (f"First Name: {player[1]}")
        print (f"Last Name: {player[2]}")
        print (f"Team Name: {player[3]}")
        print()

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
    cursor = db.cursor ()

    sql = '''INSERT INTO player (first_name, last_name, team_id)
    VALUES('Smeagol', 'Shire Folk', 1);'''    
    cursor.execute(sql)
    print_players(cursor, 'INSERT')

    sql = '''UPDATE player 
    SET team_id = 2,
	    first_name = 'Gollum',
        last_name = 'Ring Stealer' 
    WHERE first_name = 'Smeagol';'''    
    cursor.execute(sql)
    print_players(cursor, 'UPDATE')

    sql = '''DELETE FROM player
    WHERE first_name = 'Gollum';'''    
    cursor.execute(sql)
    print_players(cursor, 'DELETE')
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  the supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  the specified database does not exist")
    else:
        print(err)

finally:
    db.close()
 
