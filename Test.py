import sqlite3 

con = sqlite3.connect("Ace.db")

cursor = con.cursor()
cursor.execute("CREATE TABLE Ranking (Name text, number int, time_score int)")
cursor.execute('INSERT INTO SCHOOL VALUES("김동현",1,60)')