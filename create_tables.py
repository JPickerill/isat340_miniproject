import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "create table celebs(celebID interger PRIMARY KEY, firstname text, lastname text, age int, email text, photo text, bio text)"
sql2 = "create table members(memberID interger PRIMARY KEY, firstname text, lastname text, age int, email text, bio text)"
cursor.execute(sql)
cursor.execute(sql2)
conn.commit()
conn.close()
