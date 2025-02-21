import pymysql
import sys
import random
from BDDCommon.CommonConfigs.configurations import get_config

class DBHelpers:
    def __init__(self):
        """
        Initialize database connection parameters.
        """
        config = get_config()
        self.host = config['mysql']['host']
        self.port = int(config['mysql']['port'])
        self.db_user = config['mysql']['db_user']
        self.db_password = config['mysql']['db_password']
        # self.database = config.get('mysql', {}).get('database', 'your_database_name')

    def create_connection(self):
        """
        Creates a database connection. If it fails, the program exits immediately.
        """
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.db_user,
                password=self.db_password,
                # database=self.database,
                connect_timeout=10  # Added timeout for better failure handling
            )
            # print("✅ Database connection successful!")
            return self.connection
        except pymysql.err.OperationalError as e:
            print(f"❌ ERROR: Failed to connect to MySQL - {str(e)}")
            sys.exit(1)  # Immediately exit the program if the database is unavailable

    def execute_select(self, sql):
        """
        Executes a SELECT SQL query and returns the results as a dictionary.
        """
        try:
            conn = self.create_connection()  # Ensure connection before running query
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
            conn.close()
            return result
        except pymysql.err.OperationalError as e:
            print(f"❌ Database error: {str(e)}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Failed running SQL: {sql}. Error: {str(e)}")
            sys.exit(1)

    def execute_sql(self, sql):
        """
        Executes an INSERT, UPDATE, or DELETE SQL statement.
        """
        try:
            conn = self.create_connection()
            with conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()
            conn.close()
            print("✅ SQL executed successfully!")
        except pymysql.err.OperationalError as e:
            print(f"❌ Database error: {str(e)}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Failed executing SQL: {sql}. Error: {str(e)}")
            sys.exit(1)

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
        sys.exit(1)  # Ensure execution stops if connection fails

    try:
        # Test SELECT query
        sql = "SELECT * FROM local.wp_posts WHERE post_type = 'product' ORDER BY id DESC LIMIT 5000"
        results = db_helper.execute_select(sql)
        print("\n✅ SELECT query successful!")
        sample_result = random.sample(results, 1)
        print(f"Sample product Id: {sample_result[0]['ID']}, title: {sample_result[0]['post_title']}")

    except Exception as e:
        print(f"❌ SELECT query failed: {e}")
        sys.exit(1)  # Ensure execution stops if query fails
