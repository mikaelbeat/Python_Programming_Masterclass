import sqlite3

db = sqlite3.connect("accounts.sqlite", detect_types = sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
    local_time = row[0]
    print(f"{local_time} - {type(local_time)}")
    
db.close()