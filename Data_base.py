import pymysql

def openDB(user, password, database):
    #abre conexión con la base de datos.
    db = pymysql.connect("localhost", user, password, database)
    #prepaarar el cursor
    global cursor = db.cursor()

def addTable():
    tablename = input("Indique el nombre de la tabla : ")
    while(op != )
    text = "create table "+tablename+" ("
    while()
    cursor.execute()