import sqlite3

db = sqlite3.connect("contacts.sqlite")

def Create_database():
    db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
    
def Fill_database_with_test_data():
    db.execute("INSERT INTO contacts(name, phone, email) VALUES('Test', 12345, 'test@email.com')")
    db.execute("INSERT INTO contacts(name, phone, email) VALUES('Brian', 67890, 'brian@email.com')")
    
def Print_all_data_in_database_using_for_loop():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM contacts")
    for name, phone, email in cursor:
        print(name)
        print(phone)
        print(email)
        print("-" * 20)
    cursor.close()

def Print_all_data_in_database_using_fetchall():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM contacts")
    print(cursor.fetchall())
       
def Close_connection_to_database():
    db.commit()
    db.close()
    

#Create_database()
#Fill_database_with_test_data()
Print_all_data_in_database_using_for_loop()
Print_all_data_in_database_using_fetchall()
Close_connection_to_database()