import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="19iul2005",  # Replace with your MySQL password
    database="sistem_monitorizare"  # Replace with the name of your schema
)

cursor = conn.cursor()

# Test if connection works by retrieving users
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()

for user in users:
    print(user)

conn.close()
