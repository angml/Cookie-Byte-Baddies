from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Get all employees from the system

employees = Blueprint('employees', __name__)

@employees.route('/employees', methods=['GET'])
def get_all_employees():
    query = '''
        SELECT id, name, position, wage_per_hour
        FROM employees
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    return make_response(jsonify(theData), 200)


#------------------------------------------------------------
# Get individual employee information

employee_id = Blueprint('employee_id', __name__)

@employee_id.route('/employees/<id>', methods=['POST'])
def add_employee(id):
    data = request.json
    name = data['name']
    position = data['position']
    wage = data['wage_per_hour']
    query = f'''
        INSERT INTO employees (id, name, position, wage_per_hour)
        VALUES ({id}, '{name}', '{position}', {wage})
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return make_response("Employee added", 200)

@employee_id.route('/employees/<id>', methods=['PUT'])
def update_wage(id):
    data = request.json
    new_wage = data['wage_per_hour']
    query = f'''
        UPDATE employees
        SET wage_per_hour = {new_wage}
        WHERE id = {id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return make_response("Wage updated", 200)

@employee_id.route('/employees/<id>', methods=['DELETE'])
def delete_employee(id):
    query = f'''
        DELETE FROM employees
        WHERE id = {id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return make_response("Employee deleted", 200)

#------------------------------------------------------------
# Get employee position information

employees = Blueprint('employees', __name__)

@employees.route('/employees', methods=['GET'])
def get_all_employees():
    query = '''
        SELECT id, name, position, wage_per_hour
        FROM employees
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    return make_response(jsonify(theData), 200)