from db_manager import DatabaseManager


db_manager = DatabaseManager(
    host="localhost",
    user="root",
    password="19iul2005",
    database="sistem_monitorizare"
)

# Register users
db_manager.register_user("Popica", "Popescu", "firma cu proiectu", 1)
# db_manager.register_user("Vlad", "Oncica", "firma cu proiectu", 1)