# Create your models here.
import cx_Oracle
import requests


class Usuario:

    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    # def insertdato(self, idper, nombre, img, idserie):

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
            consultaidrol = "SELECT IDROL FROM myeROLES WHERE NOMBRE = :p1"
            cursor.execute(consultaidrol, (rol,))
            rolid = cursor.fetchone()
            args = (nombre, apellido, email, password, rolid[0])
            print("Voy a insertar:", args)
            res = cursor.callproc('ALTAUSR', args)
            print("y resulta:", res)
            return True
        except cx_Oracle.DatabaseError as error:
            print("La inserción dio error")
            return False
        finally:
            cursor.close()

    def devolverpass(self, miemail):
        cursor = self.connection.cursor()
        try:
            aaa = cursor.var(cx_Oracle.STRING)
            args = (miemail, aaa)
            cursor.callproc('RETORNAPASS', args)

            print(aaa.getvalue())

        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        return aaa

    # utiizando el procedimiento almacenado RETONRAIDUSR, nos trae el id de usuario
    def devolverId(self, miemail):
        cursor = self.connection.cursor()
        try:
            var1 = cursor.var(cx_Oracle.NUMBER)
            args = (miemail, var1)
            cursor.callproc('RETORNAIDUSR ', args)

            print(var1.getvalue())

        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        return var1.getvalue()

    def TraeDiccionarios(self, idusuario):
        # me hace falta traer la id con la función que ha puesto Iván
        cursor = self.connection.cursor()
        id = int(idusuario)
        try:
            consulta = ("SELECT myeDICCIONARIOS.TITULO, myeDICCIONARIOS.Iddic FROM myeDICCIONARIOS where USRID=:p1")
            cursor.execute(consulta, (id,))
            cursor = cursor.fetchall()

        except self.connection.Error as error:
            print("Error: ", error)
        return cursor

    def listaDiccionario(self, idDic):
        cursor = self.connection.cursor()
        try:
            consulta = ("SELECT p.PALABRA, p.IDIOMAFROM myeDICCIONARIOS d JOIN myeDICTRAD dt ON d.IDDIC = dt.DIC JOIN myeTRADUCCIONES t ON dt.TRAD = t.IDTRAD JOIN myePALABRAS p ON t.IDPALORIG = p.IDPAL OR t.IDPALDEST = p.IDPAL WHERE d.IDDIC = 1;")
            cursor.execute(consulta, (idDic,))
            cursor = cursor.fetchall()
            for A, in cursor:
                roles1 = [rol[0] for rol in cursor]
        except self.connection.Error as error:
            print("Error: ", error)

        return roles1

    def crearDic(self, id, nombre):
        cursor = self.connection.cursor()
        try:
            var1 = cursor.var(cx_Oracle.NUMBER)
            print(nombre)
            print(id)
            args = (id, nombre, var1)
            cursor.callproc('ALTADIC', args)
        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        return var1.getvalue()

    def insertarPalabra(self, id, palabraEs, idiomaEs, palabraEn, idiomaEn):
        cursor = self.connection.cursor()
        try:
            args = (id, palabraEs, idiomaEs, palabraEn, idiomaEn)
            cursor.callproc('INSERTAPALABRA', args)
        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()

    def traducirPalabra(self, id):
        cursor = self.connection.cursor()
        try:
            var1 = cursor.var(cx_Oracle.STRING)
            args = (id,var1)
            cursor.callproc('TRADUCEPALABRA', args)
        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        return var1.getvalue()


def traduccionApi(target: str, text: str, model: str = "nmt") -> dict:
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target, model=model)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result
