import mysql.connector
from datetime import datetime

class DatabaseManager:
    def __init__(self, host, user, password, database):
        # Initialize database connection
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        #add new user
    def register_user(self, first_name, last_name, company, manager_id):
        try:
            query = """
            INSERT INTO users (first_name, last_name, company, manager_id)
            VALUES (%s, %s, %s, %s);
            """
            self.cursor.execute(query, (first_name, last_name, company, manager_id))
            self.conn.commit()
            print(f"User {first_name} {last_name} registered successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        #insert access data in access      
    def insert_access_data(self, user_id, access_time, direction, gate_id):
        try:
            # Convert the ISO 8601 datetime (e.g., "2023-09-12T09:00:00.000Z") to MySQL-compatible format
            access_time = datetime.strptime(access_time, '%Y-%m-%dT%H:%M:%S.%fZ')
            access_time = access_time.strftime('%Y-%m-%d %H:%M:%S')

            query = """
            INSERT INTO access (user_id, access_time, direction, gate_id)
            VALUES (%s, %s, %s, %s);
            """
            self.cursor.execute(query, (user_id, access_time, direction, gate_id))
            self.conn.commit()
            print(f"Access data for user {user_id} inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        except ValueError as ve:
            print(f"Datetime parsing error: {ve}")
    
      
    def __del__(self):
        # Close the connection when the object is deleted
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
