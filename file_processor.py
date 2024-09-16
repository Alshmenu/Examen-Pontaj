import os
import shutil
import csv
from db_manager import DatabaseManager

def process_csv_files(db_manager, intrari_folder='intrari', backup_folder='backup_intrari'):
    
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

   
    for file_name in os.listdir(intrari_folder):
        if file_name.endswith('.csv'): 
            file_path = os.path.join(intrari_folder, file_name)
            try:
                with open(file_path, mode='r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header row
                    for row in reader:
                        user_id, access_time, direction, gate_id = row
                        db_manager.insert_access_data(user_id, access_time, direction, gate_id)
                print(f"Processed file: {file_name}")

                
                shutil.move(file_path, os.path.join(backup_folder, file_name))

            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

if __name__ == "__main__":
    # Initialize the DatabaseManager object
    db_manager = DatabaseManager(
        host="localhost",
        user="root",
        password="19iul2005",  
        database="sistem_monitorizare"  
    )

    
    process_csv_files(db_manager)

    
    db_manager.close()
