# ########################################################
# # Sample customers blueprint of endpoints
# # Remove this file if you are not using it in your project
# ########################################################
# from flask import Blueprint
# from flask import request
# from flask import jsonify
# from flask import make_response
# from flask import current_app
# from backend.db_connection import db
# from backend.ml_models.model01 import predict

# # post example in products page

# #------------------------------------------------------------
# # Create a new Blueprint object, which is a collection of 
# # routes.
# ingredients = Blueprint('ingredients', __name__)

# # Get all ingredients from the system
# @ingredients.route('/ingredients', methods=['GET'])
# def get_all_ingredients():
#     cursor = db.get_db().cursor()
#     the_query = ''' 
#         SELECT IngredientID, IngredientName, Inventory, Expiry, Price, BurnRate
#         FROM Ingredients;
#     '''
#     cursor.execute(the_query)
#     theData = cursor.fetchall()
#     the_response = make_response(jsonify(theData))
#     the_response.status_code = 200
#     the_response.mimetype='application/json'
#     return the_response

# # # Get ingredients by burn rate 
# # @ingredients.route('/ingredients/burnrate', methods=['GET'])
# # def get_burn_rate_by_ing():
# #     cursor = db.get_db().cursor()
# #     query = '''
# #         SELECT IngredientName, BurnRate
# #         FROM Ingredients;
# #     '''

# #     cursor.execute(query)
# #     theData = cursor.fetchall()
# #     column_headers = [i[0] for i in cursor.description]
# #     json_data = [dict(zip(column_headers, row)) for row in theData]

# #     the_response = make_response(jsonify(json_data))
# #     the_response.status_code = 200
# #     the_response.mimetype='application/json'
# #     return the_response    

# # Adds a new ingredient
# @ingredients.route('/ingredients', methods=['POST'])
# def add_new_ing():
#     # Collecting data from the request object
#     the_data = request.json
#     current_app.logger.info(the_data)

#     # Extracting the variables
#     ing_name = the_data.get('IngredientName')
#     inventory = the_data.get('Inventory', 0)
#     expiry = the_data.get('Expiry', None)
#     price = the_data.get('Price', 0.0)
#     burn_rate = the_data.get('BurnRate', 0.0)

#     # Get Max IngredientID
#     cursor = db.get_db().cursor()
#     cursor.execute("SELECT MAX(IngredientID) FROM Ingredients")
#     max_id = cursor.fetchone()[0]
#     next_id = 1 if max_id is None else max_id + 1

#     query = '''
#         INSERT INTO Ingredients (IngredientID, IngredientName, Inventory, Expiry, Price, BurnRate)
#         VALUES (%s, %s, %s, %s, %s, %s)    
#     '''
#     current_app.logger.info(query)
#     cursor.execute(query, (next_id, ing_name, inventory, expiry, price, burn_rate))
#     db.get_db().commit()

#     response = make_response("Successfully added ingredient")
#     response.status_code = 200
#     return response

# # CREATE NEW INGREDIENT
# @ingredients.route('/ingredients/create', methods=['POST'])
# def create_ingredient():
#     data = request.get_json()


#     name = data.get('IngredientName')
#     inventory = data.get('Inventory')
#     expiry = data.get("Expiry")
#     price = data.get('Price')
#     burn_rate = data.get('BurnRate')

#     # SQL query to insert a new ingreedient (no need for IngredientID since it's auto-incremented)
#     query = '''
#     INSERT INTO Ingredient (IngredientName, Inventory, Expiry, Price, BurnRate)
#     VALUES (%s, %s, %s, %s, %s);
#     '''

#     # Insert data into the database
#     cursor = db.get_db().cursor()
#     cursor.execute(query, (name, inventory, expiry, price, burn_rate))
#     db.get_db().commit()

#     return jsonify({"message": "Ing created successfully"}), 201



# # Updates the inventory of a specific ingredient, that Sally has delivered
# @ingredients.route('/ingredients', methods=['PUT'])
# def update_ing_by_id():
#     new_data = request.json
#     current_app.logger.info(new_data)

#     ingredient_id = new_data['IngredientID']
#     new_inventory = new_data['Inventory']

#     # Check if ingredient exists
#     cursor = db.get_db().cursor()
#     check_query = '''
#         SELECT COUNT(*) FROM Ingredients WHERE IngredientID = %s    
#     '''

#     cursor.execute(check_query, (ingredient_id,))
#     exists = cursor.fetchone()[0]

#     if exists == 0:
#         return make_response(jsonify({'error': 'Ingredient not found'}), 404)

#     query = '''
#         UPDATE Ingredients
#         SET Inventory = %s
#         WHERE IngredientID = %s
#     '''

#     cursor.execute(query, (new_inventory, ingredient_id))
#     db.get_db().commit()

#     return make_response("Succesfully updated inventory", 200)

# # Get the ingredient by ID NEW Route
# @ingredients.route('/ingredients/<int:id>', methods=['GET'])
# def get_ingredient_by_id(id):
#     cursor = db.get_db().cursor()
#     query = '''
#         SELECT IngredientID, IngredientName, Inventory, Expiry, Price, BurnRate
#         FROM Ingredients
#         WHERE IngredientID = %s
#     '''

#     cursor.execute(query, (id,))
#     theData = cursor.fetchone()

#     if theData:
#         ingredient = {
#             'IngredientID': theData[0],
#             'IngredientName': theData[1],
#             'Inventory': theData[2],
#             'Expiry': theData[3],
#             'Price': theData[4],
#             'BurnRate': theData[5]
#         }
#         response = make_response(jsonify(ingredient))
#         response.status_code = 200

#     else:
#         response = make_response(jsonify({'error': 'Ingredient not found'}), 404)
    
#     return response

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

# Update the inventory of a specific ingredient
@ingredients.route('/ingredients', methods=['PUT'])
def update_ing_by_id():
    new_data = request.json
    ingredient_id = new_data['IngredientID']
    new_inventory = new_data['Inventory']

    cursor = db.get_db().cursor()
    check_query = '''
        SELECT COUNT(*) FROM Ingredients WHERE IngredientID = %s    
    '''
    cursor.execute(check_query, (ingredient_id,))
    exists = cursor.fetchone()[0]

    if exists == 0:
        return make_response(jsonify({'error': 'Ingredient not found'}), 404)

    query = '''
        UPDATE Ingredients
        SET Inventory = %s
        WHERE IngredientID = %s
    '''
    cursor.execute(query, (new_inventory, ingredient_id))
    db.get_db().commit()

    return make_response("Successfully updated inventory", 200)

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
