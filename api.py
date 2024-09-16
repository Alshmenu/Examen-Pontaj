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

# Define a POST route
@app.route('/api/access', methods=['POST'])
def add_access():
    try:
        data = request.json  
        db_manager.insert_access_data(
            user_id=data['idPersoana'],
            access_time=data['data'],
            direction=data['sens'],
            gate_id=data['idPoarta']
        )
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

