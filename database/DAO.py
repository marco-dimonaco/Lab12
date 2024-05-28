from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.retailer import Retailer


class DAO:
    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                        SELECT  *
                        from go_retailers
                    """
        cursor.execute(query)
        for row in cursor:
            result.append(Retailer(**row))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT  DISTINCT(gr.Country)
                    from go_retailers gr
                """
        cursor.execute(query)
        for row in cursor:
            result.append(row["Country"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getRetailersCountry(country):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT  *
                    FROM go_retailers gr
                    WHERE gr.Country = %s
                """
        cursor.execute(query, (country,))
        for row in cursor:
            result.append(Retailer(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(year, idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                    select gds1.Retailer_code as rc1, gds2.Retailer_code as rc2, count(*) as n 
                    from go_daily_sales gds1 join go_daily_sales gds2 on gds1.Product_number = gds2.Product_number 
                    and year(gds1.`Date`) = year(gds2.`Date`)
                    where gds1.Retailer_code < gds2.Retailer_code and year(gds1.`Date`) = %s 
                    group by gds1.Retailer_code, gds2.Retailer_code 
                    order by n desc 
                """
        cursor.execute(query, (year,))
        for row in cursor:
            result.append(Connessione(idMap[row["rc1"]],
                                      idMap[row["rc2"]],
                                      row["n"]))
        cursor.close()
        conn.close()
        return result
