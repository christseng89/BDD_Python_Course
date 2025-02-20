import pymysql
from BDDCommon.CommonConfigs.configurations import get_config

class DBHelpers(object):

    def __init__(self):
        self.host = get_config()['mysql']['host']
        self.port = int(get_config()['mysql']['port'])
        self.db_user = get_config()['mysql']['db_user']
        self.db_password = get_config()['mysql']['db_password']

    def create_connection(self):
        """
        Creates a database connection.
        """
        try:
            self.connection = pymysql.connect(
                host=self.host, 
                port=self.port, 
                user=self.db_user, 
                password=self.db_password
            )
            return self.connection
        except Exception as e:
            raise Exception(f"Failed to connect to MySQL: {str(e)}")

    def execute_select(self, sql):
        """
        Executes a SELECT SQL query and returns the results as a dictionary.
        """
        try:
            self.create_connection()
            cur = self.connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running SQL: {sql}. Error: {str(e)}")
        finally:
            self.connection.close()

        return rs_dict

    def execute_sql(self):
        pass

# ✅ Add a test connection when running the script
if __name__ == '__main__':
    db_helper = DBHelpers()

    try:
        # Test connection
        connection = db_helper.create_connection()
        print("✅ MySQL connection successful!")
        connection.close()
    except Exception as e:
        print(f"❌ MySQL connection failed: {e}")
