import mysql.connector
import sys


class DbTop500:
    def __init__(self):
        self.conectado = False
        self.db_name = 'top500'

    def connect(self, database=True):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=self.db_name if(database) else None
        )
        self.conectado = True

    def disconnect(self):
        self.db.close()
        self.conectado = False

    def create_database(self, drop_if_exists=True):
        self.connect(False)

        cursor = self.db.cursor()
        if(drop_if_exists):
            cursor.execute("DROP DATABASE IF EXISTS %s" % self.db_name)
        cursor.execute("CREATE DATABASE %s" % self.db_name)
        cursor.execute('''
            CREATE TABLE %s.registros (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                rank VARCHAR(255), 
                site VARCHAR(255), 
                pais VARCHAR(255), 
                system VARCHAR(255), 
                cores INT, 
                rmax DOUBLE(11,2), 
                rpeak DOUBLE(11,2), 
                power INT, 
                año INT, 
                mes INT
            )''' % self.db_name)
        cursor.close()

        self.disconnect()

    def insert(self, data: {}):
        if(not self.conectado):
            self.connect()

        cursor = self.db.cursor()
        sql = "INSERT INTO registros VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (None, ) + tuple(data.values())
        print(values)

        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

    def query_count_paises(self, anio_igual=None, anio_mayor=None, descendente=True, limite=None) -> list:
        if(not self.conectado):
            self.connect()

        cursor = self.db.cursor()
        query = "SELECT pais, COUNT(*) AS count FROM registros"

        if(anio_igual is not None):
            query += " WHERE año = %s" % anio_igual
        elif(anio_mayor is not None):
            query += " WHERE año > %s" % anio_mayor

        query += " GROUP BY pais ORDER BY `count`"
        query += " DESC" if(descendente) else " ASC"

        if(limite is not None):
            query += " LIMIT %s" % limite

        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result



if __name__ == '__main__':
    db = DbTop500()
    db.create_database()
