import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('admin', 'password'))
cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('user1', 'password1'))
connection.commit()
connection.close()

connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("SELECT id, name, password FROM users")
results = cursor.fetchall()
connection.close()

for (id, name, password) in results:
    print(f'id = {id}, name = {name}, password = {password}')
