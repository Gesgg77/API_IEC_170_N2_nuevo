
import sqlite3
import os

def conectar():
    # Conecta 
    con = sqlite3.connect('api_iec_170.db')
    crear_tabla(con)
    return con

def crear_tabla(con):
    # Crea la tabla 
    sql = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        username TEXT,
        email TEXT,
        phone TEXT,
        website TEXT
    )
    '''
    con.execute(sql)

def insertar_objeto(user):
    con = conectar()
    cur = con.cursor()
    # Inserta 
    cur.execute(
        'INSERT INTO users VALUES (NULL,?,?,?,?,?)',
        (user.name, user.username, user.email, user.phone, user.website)
    )
    con.commit()
    con.close()

def obtener_user_name(nombre):
    con = conectar()
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE name=?', (nombre,))
    r = cur.fetchone()
    con.close()

    return r
