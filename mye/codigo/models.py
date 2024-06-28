import cx_Oracle


class Datos:
    def __init__(self):
        try:
            self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        except cx_Oracle.DatabaseError as e:
            print(f"Error connecting to database: {e}")
            self.connection = None