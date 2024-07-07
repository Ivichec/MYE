# Create your models here.
import cx_Oracle
import requests


class Usuario:

    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def devolverRoles(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT NOMBRE FROM myeROLES where nombre != 'Admin'")
            roles = cursor.fetchall()
            print("Tengo los roles:", roles)
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

    def bajausr(self, id):
        cursor = self.connection.cursor()
        cursor.callproc('BORRARUSR', (id,))
        return cursor

    def modificaUsuario(self, id, nombre, apellido, email, password, rol):
        cursor = self.connection.cursor()
        try:
            consultaidrol = "SELECT IDROL FROM myeROLES WHERE NOMBRE = :p1"
            cursor.execute(consultaidrol, (rol,))
            rolid = cursor.fetchone()
            args = (id, nombre, apellido, email, password, rolid[0])
            print("Voy a insertar:", args)
            res = cursor.callproc('MODIFICARUSR', args)
            print("y resulta:", res)
            return True
        except cx_Oracle.DatabaseError as error:
            print("La inserción dio error")
            return False
        finally:
            cursor.close()

    def listausuarios(self):
        cursor = self.connection.cursor()
        try:
            consulta = ('SELECT NOMBRE, APELLIDOS, EMAIL FROM myeUSUARIOS')
            cursor.execute (consulta, )
            resul = cursor.fetchall()
            cols = [col[0] for col in cursor.description]
            # Convertir los resultados en una lista de diccionarios
            resultado_users = [dict(zip(cols, fila)) for fila in resul]
            return resultado_users
        except self.connection.Error as error:
            print("Error: ", error)
        return cursor

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
            consulta = ("SELECT p_es.PALABRA AS palabra_espanol, p_es.IDIOMA AS id_idioma_espanol, p_en.PALABRA AS palabra_ingles, p_en.IDIOMA AS id_idioma_ingles FROM myeDICCIONARIOS d JOIN myeDICTRAD dr ON d.IDDIC = dr.DIC JOIN myeTRADUCCIONES t ON dr.TRAD = t.IDTRAD JOIN myePALABRAS p_es ON t.IDPALORIG = p_es.IDPAL JOIN myePALABRAS p_en ON t.IDPALDEST = p_en.IDPAL WHERE d.IDDIC = :p1")
            cursor.execute(consulta, {'p1': idDic})
            resultados = cursor.fetchall()
            columnas = [col[0] for col in cursor.description]
            # Convertir los resultados en una lista de diccionarios
            resultado_dicts = [dict(zip(columnas, fila)) for fila in resultados]
            return resultado_dicts
        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

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
    def altaTests(self, id,fecha):
        cursor = self.connection.cursor()
        try:
            var1 = cursor.var(cx_Oracle.NUMBER)
            args = (id, fecha,var1)
            cursor.callproc('ALTATEST', args)
        except self.connection.Error as error:
            print("Error: ", error)
        return var1.getvalue()

    def insertarResultado(self, idTests, id_trad, resultado):
        cursor = self.connection.cursor()
        try:
            args = (idTests, id_trad, resultado)
            print(args)
            cursor.callproc('INSERTARESULTADO', args)
        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()

    def obtenerTestsYResultados(self, user_id):
        cursor = self.connection.cursor()
        try:
            consulta = """
            SELECT 
               t.IDTEST AS id_test,
                COUNT(CASE WHEN r.RESULTADO = 1 THEN 1 ELSE NULL END) AS count_1,
                COUNT(r.RESULTADO) AS count_total,
                t.FECHA AS fecha
            FROM 
                myeRESULTADOS r
            JOIN 
                myeTESTS t ON r.TESTID = t.IDTEST
            WHERE 
                t.USRID = :user_id
                
            GROUP BY 
                t.IDTEST, t.FECHA
            """
            cursor.execute(consulta, {'user_id': user_id})
            resultados = cursor.fetchall()
            columnas = [col[0].lower() for col in cursor.description]
            resultado_dicts = [dict(zip(columnas, fila)) for fila in resultados]

            # Calcular la nota sobre 10
            for resultado in resultado_dicts:
                if resultado['count_total'] > 0:
                    resultado['nota_sobre_10'] = (resultado['count_1'] / resultado['count_total']) * 10
                else:
                    resultado['nota_sobre_10'] = 0

            return resultado_dicts
        except self.connection.Error as error:
            print("Error: ", error)
            return []
        finally:
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

    def obtenerPalabrasAleatorias(self, cantidad):
        cursor = self.connection.cursor()
        try:
            consulta = f"""
            SELECT * FROM (
                SELECT 
                    t.IDTRAD AS id_trad, 
                    p_es.PALABRA AS palabra_espanol, 
                    p_es.IDIOMA AS id_idioma_espanol, 
                    p_en.PALABRA AS palabra_ingles, 
                    p_en.IDIOMA AS id_idioma_ingles 
                FROM 
                    myePALABRAS p_es 
                JOIN 
                    myeTRADUCCIONES t ON p_es.IDPAL = t.IDPALORIG 
                JOIN 
                    myePALABRAS p_en ON t.IDPALDEST = p_en.IDPAL 
                ORDER BY dbms_random.value
            ) WHERE ROWNUM <= :cantidad
            """
            cursor.execute(consulta, {'cantidad': cantidad})
            resultados = cursor.fetchall()
            columnas = [col[0] for col in cursor.description]
            resultado_dicts = [dict(zip(columnas, fila)) for fila in resultados]
            print(resultado_dicts)
            return resultado_dicts
        except self.connection.Error as error:
            print("Error: ", error)
            return []
        finally:
            cursor.close()


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
