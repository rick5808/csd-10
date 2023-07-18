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
    #input("\n\a Press any key to continue...") 
    
    cursor = db.cursor ()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall ()
    print ("-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print (f"Team ID: {team[0]}")
        print (f"Team Name: {team[1]}")
        print (f"Mascot: {team[2]}")
        print()

    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()
    print ("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print (f"Player ID: {player[0]}")
        print (f"First Name: {player[1]}")
        print (f"Last Name: {player[2]}")
        print (f"Team ID: {player[3]}")
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



 