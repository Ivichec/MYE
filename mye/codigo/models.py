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

    def insertarUsuario(self, nombre, apellido, email, password, rol):
        cursor = self.connection.cursor()
        try:
            consulta = "INSERT INTO DEPT VALUES(:p1, :p2, :p3), :p4, :p5"
            cursor.execute(consulta, (nombre, apellido, email, password, rol))
            self.connection.commit()
            return True
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return False
        finally:
            cursor.close()

    class MiraPass:
        def __init__(self):
            self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

        def devolverpass(self, miemail):
            cursor = self.connection.cursor()
            try:
                aaa = cursor.var(cx_Oracle.STRING)
                print("wjh.gfqouñwhfglasdhglasjfdhglasfdg")
                args = (miemail, aaa)
                cursor.callproc('RETORNAPASS', args)

                print(aaa.getvalue())

            except self.connection.Error as error:
                print("Error: ", error)
            cursor.close()
            return aaa


class MiraPass:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def devolverpass(self, miemail):
        cursor = self.connection.cursor()
        try:
            aaa = cursor.var(cx_Oracle.STRING)
            print("wjh.gfqouñwhfglasdhglasjfdhglasfdg")
            args = (miemail, aaa)
            cursor.callproc('RETORNAPASS', args)

            print(aaa.getvalue())

        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        return aaa



#utiizando el procedimiento almacenado RETONRAIDUSR, nos trae el id de usuario
    def devolverId(self, miemail):
        cursor = self.connection.cursor()
        try:
            var1 = cursor.var(cx_Oracle.NUMBER)
            print("wjh.gfqouñwhfglasdhglasjfdhglasfdg")
            args = (miemail, var1)
            cursor.callproc('RETORNAIDUSR ', args)

            print(var1.getvalue())

        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        return var1.getvalue()

    def TraeDiccionarios(self,idusuario):
        #me hace falta traer la id con la función que ha puesto Iván
        cursor = self.connection.cursor()

        try:
            consulta = ("SELECT myeDICCIONARIOS.TITULO FROM myeDICCIONARIOS where USRID=:p1")
            cursor.execute(consulta, (idusuario,))
            print(cursor)
        except self.connection.Error as error:
            print("Error: ", error)

        return cursor