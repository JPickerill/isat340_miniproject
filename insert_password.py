import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql3="insert into info values(?,?)"
data = (("gagnonop", "happyhour"),("jackpk", "snowwhite"))
cursor.executemany(sql3,data)
conn.commit()
conn.close()
