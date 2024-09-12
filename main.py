from db_manager import DatabaseManager


db_manager = DatabaseManager(
    host="localhost",
    user="root",
    password="19iul2005",
    database="sistem_monitorizare"
)

# Register users
db_manager.register_user("John", "Doe", "Acme Corp", 1)
db_manager.register_user("Jane", "Smith", "Beta Ltd", 2)