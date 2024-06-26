import mysql.connector
db_config = {
    'user': 'admin',
    'password': 'deepak123',
    'host': 'python-connection.cras4m244pf3.us-east-1.rds.amazonaws.com',
    'database': 'pythonsql'
}

class Database:
    @staticmethod
    def execute_query(query, params=None):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def fetch_query(query, params=None):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results