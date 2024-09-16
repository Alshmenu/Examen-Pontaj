from flask import Flask, request, jsonify
from db_manager import DatabaseManager

app = Flask(__name__)

# Initialize the database manager
db_manager = DatabaseManager(
    host="localhost",
    user="root",
    password="19iul2005",  
    database="sistem_monitorizare"  
)

@app.route('/api/access', methods=['POST'])
def add_access():
    try:
        data = request.json  # Get JSON data from the request
        print(f"Received JSON: {data}")  # Debug: print received JSON data

        # Insert data into the database
        db_manager.insert_access_data(
            user_id=data['idPersoana'],
            access_time=data['data'],
            direction=data['sens'],
            gate_id=data['idPoarta']
        )
        print("Data successfully inserted into the database.")  # Debug

        return jsonify({"status": "success"}), 201
    except Exception as e:
        print(f"Error occurred: {e}")  # Debug
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
