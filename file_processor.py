import os
import shutil
import csv
from db_manager import DatabaseManager

def process_csv_files(db_manager, intrari_folder='intrari', backup_folder='backup_intrari'):
    # Ensure the backup folder exists
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Loop through all CSV files in the 'intrari' folder
    for file_name in os.listdir(intrari_folder):
        if file_name.endswith('.csv'):  # Only process CSV files
            file_path = os.path.join(intrari_folder, file_name)
            try:
                with open(file_path, mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        user_id, access_time, direction, gate_id = row
                        db_manager.insert_access_data(user_id, access_time, direction, gate_id)
                print(f"Processed file: {file_name}")

                # Move the processed file to the 'backup_intrari' folder
                shutil.move(file_path, os.path.join(backup_folder, file_name))

            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

if __name__ == "__main__":
    # Initialize the DatabaseManager object
    db_manager = DatabaseManager(
        host="localhost",
        user="root",
        password="19iul2005",  # Replace with your MySQL password
        database="sistem_monitorizare"  # Replace with your schema name
    )

    # Call the function to process CSV files manually
    process_csv_files(db_manager)
