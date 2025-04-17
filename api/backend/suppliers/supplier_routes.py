from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db


suppliers = Blueprint('suppliers', __name__)

@suppliers.route('/suppliers', methods=['GET'])
def get_all_suppliers():
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT ID, CompanyName, ContactPerson, Phone, Email FROM Supplier
        '''
        cursor.execute(query)
        data = cursor.fetchall()
        response = make_response(jsonify(data))
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({"error": str(e), "data": []}), 500
    

@suppliers.route('/s/suppliers', methods=['POST'])
def add_supplier():
    data = request.get_json(force = True)
    query = '''
        INSERT INTO Supplier (ID, CompanyName, ContactPerson, Phone, Email) VALUES (%s, %s, %s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, (
            data['ID'], data['CompanyName'], data['ContactPerson'], data['Phone'], data['Email']
        ))
        db.get_db().commit()
        return jsonify({"message": "Supplier addded!"}), 201
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": str(e)})



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
        person = data.get('ContactPerson')
        phone = data.get('Phone')
        email = data.get('Email')

        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE Supplier SET Name = %s, ContactPerson = %s, Phone = %s, Email = %s WHERE ID = %s",
            (name, person, phone, email, supplier_id)
        )
        mysql.connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Supplier not found'}), 404
        return jsonify({'message': 'Supplier updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})
