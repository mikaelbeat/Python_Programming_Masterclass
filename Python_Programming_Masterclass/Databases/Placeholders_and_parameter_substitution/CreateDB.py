import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Enter a name to search for: ")

for row in conn.execute(f"SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)
    
conn.close()