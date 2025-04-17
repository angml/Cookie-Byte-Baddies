from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Create a new Blueprint object, which is a collection of routes
materials = Blueprint('materials', __name__)

# Get all materials from the system
@materials.route('/materials', methods=['GET'])
def get_all_materials():
    cursor = db.get_db().cursor()
    query = ''' 
        SELECT ID, Name, Price, BurnRate, Inventory
        FROM Materials;
    '''
    cursor.execute(query)
    the_data = cursor.fetchall()
    response = make_response(jsonify(the_data))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response


# Add a new material 
@materials.route('/materials/create', methods=['POST'])
def create_material():
    data = request.get_json()

    name = data.get('Name')
    inventory = data.get('Inventory')
    price = data.get('Price')
    burn_rate = data.get('BurnRate')

    query = '''
    INSERT INTO Materials (Name, Inventory, Price, BurnRate)
    VALUES (%s, %s, %s, %s);
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (name, inventory, price, burn_rate))
    db.get_db().commit()

    return jsonify({"message": "Material created successfully"}), 201

# --------------------------------------------------------------------------------------------------

# Update the inventory of a material
@materials.route('/materials/update-inventory/<int:item_id>', methods=['PUT'])
def update_mat_inventory(item_id):
    try:
        data = request.get_json()
        new_inventory = data.get('Inventory')

        if new_inventory is None:
            return jsonify({"error": "Missing 'Inventory' in request body"}), 400
        if not isinstance(new_inventory, (int, float)) or new_inventory < 0:
            return jsonify({"error": "Inventory must be a non-negative number"}), 400

        cursor = db.get_db().cursor()
        update_query = '''
            UPDATE Materials
            SET Inventory = %s
            WHERE ID = %s;
        '''
        cursor.execute(update_query, (new_inventory, item_id))
        db.get_db().commit()

        return jsonify({"message": "Inventory updated successfully!"}), 200

    except Exception as e:
        current_app.logger.error(f"Error Updating Inventory: {e}")
        return jsonify({"error": "An error occurred while updating inventory."}), 500
    

# Gets the top 10 highest burn rates
@materials.route('/materials/burnrate/top', methods=['GET'])
def get_top_mat_burnrates():
    cursor = db.get_db().cursor()

    top_query = '''
        SELECT Name, BurnRate
        FROM Materials
        ORDER BY BurnRate DESC
        LIMIT 10
    '''

    cursor.execute(top_query)
    top_results = cursor.fetchall()

    return jsonify(top_results), 200

# Gets the top 10 lowest burn rates
@materials.route('/materials/burnrate/bottom', methods=['GET'])
def get_bottom_mat_burnrates():
    cursor = db.get_db().cursor()

    bottom_query = '''
        SELECT Name, BurnRate
        FROM Materials
        ORDER BY BurnRate ASC
        LIMIT 10
    '''

    cursor.execute(bottom_query)
    bottom_results = cursor.fetchall()

    return jsonify(bottom_results), 200