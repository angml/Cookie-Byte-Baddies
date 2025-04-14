from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Get all employees from the system

employees = Blueprint('employees', __name__)

@employees.route('/employees', methods = ['GET'])
def get_all_employees():
    
    query = '''
        SELECT id, name, position, wage_per_hour
        FROM employees
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    return make_response(jsonify(theData), 200)


@employee.route('/employees', methods = ['POST'])
def add_employee():
    data = request.json
    query = '''
        INSERT INTO Employee (Name, Position, Wage, HoursWorked, ManagerID)
        Values (%s, %s, %s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (
        data['Name'], data['Position'], data['Wage'],
        data.get('HoursWorked', 0), data.get('ManagerID')
    ))
    db.get_db(commit())
    return make_response("Employee added!", 201)

@employee.route('/employees/<int:id>', methods = ['PUT'])
def update_employee(jd):
    data = '''
        UPDATE Employee
        SET Wage = %s
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['Wage'], id))
    db.get_db().commit()
    return make_response("Employee wage updated successfully.", 200)

@employees.route('/employees/<int:id>', methods = ['DELETE'])
def delete_employee(id):
    query = '''
        DELETE FROM Employee
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (id,))
    db.get_db().commit()
    return make_response("Employee terminated", 200)


@employees.route('/employees/position/<position>', methods = ['GET'])
def get_employees_by_position(position):
    query = '''
        SELECT ID, Name, Position, Wage
        FROM Employee
        WHERE Position = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (position,))
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)