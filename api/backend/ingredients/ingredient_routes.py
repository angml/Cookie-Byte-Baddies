from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Create a new Blueprint object, which is a collection of routes
ingredients = Blueprint('ingredients', __name__)

# Get all ingredients from the system
@ingredients.route('/ingredients', methods=['GET'])
def get_all_ingredients():
    cursor = db.get_db().cursor()
    query = ''' 
        SELECT IngredientID, IngredientName, Inventory, Expiry, Price, BurnRate
        FROM Ingredients;
    '''
    cursor.execute(query)
    the_data = cursor.fetchall()
    response = make_response(jsonify(the_data))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

# Add a new ingredient (this is the `/ingredients/create` endpoint)
@ingredients.route('/ingredients/create', methods=['POST'])
def create_ingredient():
    data = request.get_json()

    name = data.get('IngredientName')
    inventory = data.get('Inventory')
    expiry = data.get('Expiry')
    price = data.get('Price')
    burn_rate = data.get('BurnRate')

    # Ensure the ingredients table is named correctly (Ingredients)
    query = '''
    INSERT INTO Ingredients (IngredientName, Inventory, Expiry, Price, BurnRate)
    VALUES (%s, %s, %s, %s, %s);
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (name, inventory, expiry, price, burn_rate))
    db.get_db().commit()

    return jsonify({"message": "Ingredient created successfully"}), 201




# Update the inventory of an ingredient
@ingredients.route('/ingredients/update-inventory/<int:item_id>', methods=['PUT'])
def update_ing_inventory(item_id):
    try:
        data = request.get_json()
        new_inventory = data.get('Inventory')

        if new_inventory is None:
            return jsonify({"error": "Missing 'Inventory' in request body"}), 400
        if not isinstance(new_inventory, (int, float)) or new_inventory < 0:
            return jsonify({"error": "Inventory must be a non-negative number"}), 400

        cursor = db.get_db().cursor()
        update_query = '''
            UPDATE Ingredients
            SET Inventory = %s
            WHERE IngredientID = %s;
        '''
        cursor.execute(update_query, (new_inventory, item_id))
        db.get_db().commit()

        return jsonify({"message": "Inventory updated successfully!"}), 200

    except Exception as e:
        current_app.logger.error(f"Error Updating Inventory: {e}")
        return jsonify({"error": "An error occurred while updating inventory."}), 500


# -------------------------------------------------------------------------------------------------------------

# Get the ingredient by ID
@ingredients.route('/ingredients/<int:id>', methods=['GET'])
def get_ingredient_by_id(id):
    cursor = db.get_db().cursor()
    query = '''
        SELECT IngredientID, IngredientName, Inventory, Expiry, Price, BurnRate
        FROM Ingredients
        WHERE IngredientID = %s
    '''
    cursor.execute(query, (id,))
    the_data = cursor.fetchone()

    if the_data:
        ingredient = {
            'IngredientID': the_data[0],
            'IngredientName': the_data[1],
            'Inventory': the_data[2],
            'Expiry': the_data[3],
            'Price': the_data[4],
            'BurnRate': the_data[5]
        }
        response = make_response(jsonify(ingredient))
        response.status_code = 200
    else:
        response = make_response(jsonify({'error': 'Ingredient not found'}), 404)

    return response

# -------------------------------------------------------------------------------------------------------------

@ingredients.route('/ingredients/burnrate/top', methods=['GET'])
def get_top_burnrates():
    cursor = db.get_db().cursor()

    top_query = '''
        SELECT IngredientName, BurnRate
        FROM Ingredients
        ORDER BY BurnRate DESC
        LIMIT 10
    '''

    cursor.execute(top_query)
    top_results = cursor.fetchall()

    return jsonify(top_results), 200



#----------------------------------------------------------------------------------------------------------------


@ingredients.route('/ingredients/burnrate/bottom', methods=['GET'])
def get_bottom_burnrates():
    cursor = db.get_db().cursor()

    bottom_query = '''
        SELECT IngredientName, BurnRate
        FROM Ingredients
        ORDER BY BurnRate ASC
        LIMIT 10
    '''

    cursor.execute(bottom_query)
    bottom_results = cursor.fetchall()

    return jsonify(bottom_results), 200