from flask import Flask, Blueprint, request, jsonify, make_response
from backend.db_connection import db

employees = Blueprint('employees', __name__)

@employees.route('/employees', methods=['GET'])
def get_all_employees():
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT ID, FirstName, LastName, Position, Wage, HoursWorked, ManagerID
            FROM Employee
        '''
        cursor.execute(query)
        data = cursor.fetchall()
        response = make_response(jsonify(data))
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({"error": str(e), "data": []}), 500

@employees.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json(force=True)
    query = '''
        INSERT INTO Employee (ID, FirstName, LastName, Position, Wage, HoursWorked, ManagerID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, (
            data['ID'], data['FirstName'], data['LastName'], data['Position'],
            float(data['Wage']), float(data['HoursWorked']), 1
        ))
        db.get_db().commit()
        return jsonify({"message": "Employee added!"}), 201
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": str(e)}), 400
    

@employees.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json(force=True)
    query = '''
        UPDATE Employee
        SET Wage = %s
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, (float(data['Wage']), id))
        db.get_db().commit()
        return jsonify({"message": "Employee wage updated successfully."}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": str(e)}), 400

@employees.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    query = '''
        DELETE FROM Employee
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, (id,))
        db.get_db().commit()
        return jsonify({"message": "Employee terminated"}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": str(e)}), 400


app = Flask(__name__)
app.register_blueprint(employees, url_prefix='/e')

if __name__ == "__main__":
    app.run(debug=True, port=4000)