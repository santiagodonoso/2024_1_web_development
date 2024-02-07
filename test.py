import sqlite3
db = sqlite3.connect("company.db")
sql = db.execute("SELECT * FROM users")
users = sql.fetchall()
print(users)













