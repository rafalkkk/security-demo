import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

# ERROR - string manipulation for SQL query - B608
# SQL Injection password:    ' OR 1=1 OR ''='
query1 = f"SELECT * FROM users WHERE name = '{username}' AND password = '{password}'"

print(f'User validation with {query1}')
c.execute(query1)
result = c.fetchone()

if result:
    print("Login successful")
else:
    print("Login failed")

# ERROR - SQL string manipulation possible - B608 - silenced by "nosec"
query2 = f"SELECT * FROM users WHERE name = ? AND password = ?"  # nosec 

# B608 - still may raise errors
print(f'User validation with {query2}')
c.execute(query2, (username, password))
# B608 correction by moving the code into execute command
# c.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))

result = c.fetchone()

if result:
    print("Login successful")
else:
    print("Login failed")

        

a_long_text = 'aaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccdddddddddddddddddddeeeeeeeeeeeeefggggggggggggggggghhhhhhhhhhhhhhhh'
result = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzvvvvvvvvvvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwuu' + a_long_text
