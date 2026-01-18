from database.DB_connect import DBConnect
from model.oggetto import Oggetto

class DAO:

    @staticmethod
    def read_all_objects():
        conn = DBConnect.get_connection()
        if not conn:
            print("Database connection failed, read_all_objects()")
            return None
        risultati = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM objects"

        try:
            cursor.execute(query)
            for row in cursor:
                ogg = Oggetto(**row)
                risultati.append(ogg)
                print(ogg)

        except Exception as e:
            print(e)
            print('errore nella query, read_all_objects()')
            risultati = None

        finally:
            cursor.close()
            conn.close()

        return risultati

    @staticmethod
    def read_all_relations():
        conn = DBConnect.get_connection()
        if not conn:
            print("Database connection failed, read_all_relations()")
            return None
        risultati = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select eo1.object_id as oggetto1_id, eo2.object_id as oggetto2_id, count(*) as peso
                from exhibition_objects eo1, exhibition_objects eo2
                where eo1.exhibition_id = eo2.exhibition_id and
                    eo1.object_id > eo2.object_id and eo1.object_id != eo2.object_id 
                group by eo1.object_id, eo2.object_id
                """

        try:
            cursor.execute(query)
            for row in cursor:
                risultati.append((row["oggetto1_id"], row["oggetto2_id"], row["peso"]))
                print((row["oggetto1_id"], row["oggetto2_id"]))

        except Exception as e:
            print(e)
            print('errore nella query, read_all_objects()')
            risultati = None

        finally:
            cursor.close()
            conn.close()

        return risultati

