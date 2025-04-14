########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

# post example in products page

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
ingredients = Blueprint('ingredients', __name__)


#------------------------------------------------------------
# Get all ingredients from the system

@ingredients.route('/ingredients', methods=['GET'])
def get_ingredients():
    query = '''SELECT IngredientID, IngredientName, Inventory,
                    Expiry, Price, BurnRate FROM Ingredients
    '''
    
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of ingredients
    cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
    theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response

# Get ingredients by burn rate 
# might need to be a get by id? /id
@ingredients.route('/ingredients/burnrate', methods=['GET'])
def get_burn_rate_by_ing():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = '''
        SELECT IngredientName, BurnRate
        FROM Ingredients;
    '''

    # use cursor to query the database for a list of ingredients
    cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
    theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response    

# Adds a new ingredient
@ingredients.route('/ingredients', methods=['POST'])
def add_new_ing():
    # Collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting the variable
    ing_name = the_data['IngredientName']

    query = f'''
        INSERT INTO Ingredients (IngredientName)
        VALUES ({'ing_name'})    
    '''

    current_app.logger.info(query)

    # Execute the insert statment and commit the changes
    cursor = db.get.db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Successfully added ingredient")
    response.status_code = 200
    return response

# Updates the inventory of a specific ingredient, that Sally has delivered
@ingredients.route('/ingredients', methods=['PUT'])
def update_ing_by_id():
    new_data = request.json
    current_app.logger.info(new_data)

    ingredient_id = new_data['IngredientID']
    new_inventory = new_data['Inventory']

    query = '''
        UPDATE Ingredients
        SET Inventory = %s
        WHERE IngredientID = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (new_inventory, ingredient_id))
    db.get_db().commit()

    return make_response("Succesfully updated inventory", 200)