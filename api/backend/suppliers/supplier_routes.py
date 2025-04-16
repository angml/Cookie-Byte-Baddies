from flask import Blueprint, request, jsonify, current_app
from backend.db_connection import db

suppliers = Blueprint('suppliers', __name__)

@suppliers.route('/suppliers', methods=['GET'])
def get_suppliers():
    cursor = db.get_db().cursor()
    query = '''
        SELECT ID, Name, Phone, Email
        FROM Supplier
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    data = [dict(zip(column_names, row)) for row in rows]
    return jsonify(data), 200

@suppliers.route('/suppliers', methods=['POST'])
def add_supplier():
    data = request.json
    query = '''
        INSERT INTO Supplier (ID, Name, Phone, Email)
        VALUES (%s, %s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, (data['ID'], data['Name'], data['Phone'], data['Email']))
        db.get_db().commit()
        return jsonify({"message": "Supplier added!"}), 201
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": str(e)}), 400

@suppliers.route('/suppliers/<int:id>', methods=['PUT'])
def update_supplier_contact(id):
    data = request.json
    query = '''
        UPDATE Supplier
        SET Phone = %s, Email = %s
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, (data['Phone'], data['Email'], id))
        db.get_db().commit()
        return jsonify({"message": "Supplier contact information updated successfully"}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": str(e)}), 400

@suppliers.route('/suppliers/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    query = '''
        DELETE FROM Supplier
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, (id,))
        db.get_db().commit()
        return jsonify({"message": "Supplier contract terminated successfully"}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": str(e)}), 400
