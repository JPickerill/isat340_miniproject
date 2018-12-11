import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql3 = "create table info(username text PRIMARY KEY, password text)"
cursor.execute(sql3)
conn.commit()
conn.close()
