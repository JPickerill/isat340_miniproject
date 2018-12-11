import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = " delete from info where username = 'gagnonop' "
cursor.execute(sql)
conn.commit()
conn.close()
