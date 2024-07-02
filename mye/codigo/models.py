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
