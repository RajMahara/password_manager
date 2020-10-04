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

def menu():
    print('*****************************')
    print('* i : inserir nova senha    *')
    print('* r : recuperar uma senha   *')
    print('* s : sair                  *')
    print('*****************************')

while True: 
    menu()
    op = input('o que deseja fazer? ')
    if op not in ['l','i','r','s']:
        print('Opção Inválida!')
        continue
    if op == 's':
        break

conn.close()