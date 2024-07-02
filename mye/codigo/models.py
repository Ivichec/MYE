from django.db import models

# Create your models here.
import cx_Oracle

class Diccionario:

    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    #def insertdato(self, idper, nombre, img, idserie):

    def devolverRoles(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT NOMBRE FROM myeROLES where nombre != 'Admin'")
            roles = cursor.fetchall()
            for A, in roles:
                roles1 = [rol[0] for rol in roles]
                print(roles1)


        except self.connection.Error as error:
            print("Error: ", error)

        return roles1
