import mysql.connector


class DbTop500:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )

    """Crea base de datos y borra si existia una anterior si no se le indica lo contrario
    Retorna True si todo sale bien y False si ocurre un error"""
    def create_database(self, drop_if_exists=True) -> bool:
        try:
            cursor = self.db.cursor()
            if(drop_if_exists):
                cursor.execute("DROP DATABASE IF EXISTS top500")
            cursor.execute("CREATE DATABASE top500")
            return True
        except:
            return False
        

if __name__ == '__main__':
    db = DbTop500()
    print(db.create_database(False))