from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

employees = Blueprint('employees', __name__)

# ----------------------------------------
# GET all employees
@employees.route('/employees', methods=['GET'])
def get_all_employees():
    query = '''
        SELECT ID, FirstName, LastName, Position, Wage, HoursWorked, ManagerID
        FROM Employee
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]
    data = [dict(zip(column_names, row)) for row in rows]

    return jsonify(data)


# ----------------------------------------
# INSERT a new employee
@employees.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    query = '''
        INSERT INTO Employee (FirstName, LastName, Position, Wage, HoursWorked, ManagerID)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (
        data['FirstName'], data['LastName'], data['Position'],
        data['Wage'], data['HoursWorked'], data['ManagerID']
    ))
    db.get_db().commit()
    return make_response("Employee added!", 201)

# ----------------------------------------
# UPDATE an employee’s wage
@employees.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    query = '''
        UPDATE Employee
        SET Wage = %s
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['Wage'], id))
    db.get_db().commit()
    return make_response("Employee wage updated successfully.", 200)

# ----------------------------------------
# DELETE an employee
@employees.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    query = '''
        DELETE FROM Employee
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (id,))
    db.get_db().commit()
    return make_response("Employee terminated", 200)

# ----------------------------------------
# GET all employees by position
@employees.route('/employees/position/<position>', methods=['GET'])
def get_employees_by_position(position):
    query = '''
        SELECT ID, FirstName, LastName, Position, Wage, HoursWorked, ManagerID
        FROM Employee
        WHERE Position = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (position,))
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)
