from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db


suppliers = Blueprint('suppliers', __name__)

@suppliers.route('/suppliers', methods=['GET'])
def get_all_suppliers():
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT ID, Name, Phone, Email FROM Supplier
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        data = []
        for row in rows:
            sup = dict(zip(column_names, row))
            data.append(sup)
        response = make_response(jsonify(data))
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({"error": str(e), "data": []}), 500
    

# Route to add a new supplier
@suppliers.route('/s/suppliers', methods=['POST'])
def add_supplier():
    try:
        data = request.get_json()
        name = data.get('Name')
        phone = data.get('Phone')
        email = data.get('Email')

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Supplier (Name, Phone, Email) VALUES (%s, %s, %s)",
            (name, phone, email)
        )
        mysql.connection.commit()
        return jsonify({'message': 'Supplier added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)})

# Route to delete a supplier by ID
@suppliers.route('/s/suppliers/<int:supplier_id>', methods=['DELETE'])
def delete_supplier(supplier_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "DELETE FROM Supplier WHERE ID = %s", (supplier_id,)
        )
        mysql.connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Supplier not found'}), 404
        return jsonify({'message': 'Supplier deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Route to update a supplier
@suppliers.route('/s/suppliers/<int:supplier_id>', methods=['PUT'])
def update_supplier(supplier_id):
    try:
        data = request.get_json()
        name = data.get('Name')
        phone = data.get('Phone')
        email = data.get('Email')

        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE Supplier SET Name = %s, Phone = %s, Email = %s WHERE ID = %s",
            (name, phone, email, supplier_id)
        )
        mysql.connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Supplier not found'}), 404
        return jsonify({'message': 'Supplier updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})
