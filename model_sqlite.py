from sqlite3 import *
from .model import create_uid

def connectdb():
    '''Connexion à la base de données'''
    return connect('data/data.db')

def initTable():
    '''Création des tables'''
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS code (
            uid INTEGER(30) PRIMARY KEY,
            code TEXT DEFAULT '# Insert your code here ...',
            language VARCHAR(25) DEFAULT 'Python'
        )
    ''')
    conn.commit()
    conn.close()

def getAllCodes():
    '''Sélectionne tous les codes'''
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM code
        ORDER BY uid DESC
    ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result

def getAllLanguages():
    '''Sélectionne tous les langages'''
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM languages
        ORDER BY uid DESC
    ''')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result

def getCode(uid):
    '''Sélectionne un code'''
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM code
        WHERE uid = ?
    ''', (uid,))
    result = cur.fetchone()
    conn.commit()
    conn.close()
    return result

def createCode():
    '''Crée/Enregistre un code'''
    conn = connectdb()
    cur = conn.cursor()
    uid = create_uid()
    cur.execute('''
        INSERT INTO code (uid) values (?)
    ''', (uid,))
    conn.commit()
    conn.close()
    return uid

def updateCode(uid, code, lang):
    '''Modifie le code'''
    conn = connectdb()
    cur = conn.cursor()
    result = cur.execute('''
        UPDATE code 
        SET code = ?, language = ?
        WHERE uid = ?
    ''', (code, lang, uid))
    conn.commit()
    conn.close()
    return result
