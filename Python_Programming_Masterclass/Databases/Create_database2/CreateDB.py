import sqlite3

db = sqlite3.connect("contacts.sqlite")

def Fetch_all_data():
    for name, phone, email in db.execute("SELECT * FROM contacts"):
        print(name)
        print(phone)
        print(email)
        print("-" * 20)
    db.close()
    
def Update_one_record():
    update_sql = "UPDATe contacts SET email = 'update@email.com' WHERE phone = 12345"
    update_cursor = db.cursor()
    update_cursor.execute(update_sql)
    update_amount = update_cursor.rowcount
    print(f"{update_amount} rows updated.\n")
    update_cursor.close()

Update_one_record()
Fetch_all_data()