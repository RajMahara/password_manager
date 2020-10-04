import sqlite3

MASTER_PASSWORD = "123456"

conn = sqlite3.connect('password.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOR EXISTS user (
    service TEXT NOT NULL,  
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

conn.close()