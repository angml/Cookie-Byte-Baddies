from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

suppliers = Blueprint('suppliers', __name__)

@suppliers.route('/suppliers', methods = ['GET'])
def get_suppliers():
    query = '''
        SELECT ID, Name, Phone, Email
        FROM Supplier
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

@suppliers.route('/suppliers', methods = ['POST'])
def add_supplier():
    data = request.json
    query = '''
        INSERT INTO Supplier (Name, Phone, Email)
        VALUES (%s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['Name'], data['Phone'], data['Email']))
    db.get_db().commit()
    return make_response("Supplier added!", 201)

@suppliers.route('/suppliers/<int:id>', methods = ['PUT'])
def update_supplier_contact(id):
    data = request.json
    query = '''
        UPDATE Supplier
        SET Phone = %s, Email = %s
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['Phone'], data['Email'], id))
    db.get_db().commit()
    return make_response("Supplier contact information updated successfully", 200)

@suppliers.route('/suppliers/<int:id>', methods = ['DELETE'])
def delete_supplier(id):
    query = '''
        DELETE FROM Supplier
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (id,))
    db.get_db().commit()
    return make_response("Supplier contract terminated successfully", 200)
