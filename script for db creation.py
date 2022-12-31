import sqlite3
Cricketgame=sqlite3.connect('cricketgame.db')
curschool=Cricketgame.cursor()
curschool.execute('''CREATE TABLE Team (
Name TEXT (50),
Players TEXT (50),
Value INTEGER);''')
Cricketgame.close()
