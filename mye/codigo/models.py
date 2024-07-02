import cx_Oracle


class Empleado:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def devolverdato(self,miOficio):
        cursor = self.connection.cursor()
        try:
            consulta = ("SELECT apellido,oficio, salario FROM emp where UPPER(oficio)=UPPER(:p1)")
            cursor.execute(consulta, (miOficio,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

        cursor = connection.cursor()


class MiraPass:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def devolverpass(self, miemail):
        cursor = self.connection.cursor()
        try:
            aaa = cursor.var(cx_Oracle.STRING)
            print("wjh.gfqouñwhfglasdhglasjfdhglasfdg")
            args=(miemail,aaa)
            cursor.callproc('RETORNAPASS', args)

            print(aaa.getvalue())

        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        return aaa