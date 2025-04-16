from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
equipment = Blueprint('equipment', __name__)

#------------------------------------------------------------
# Get all the equipment information from the database
# and return them to the manager
@equipment.route('/equipment', methods=['GET'])
def get_all_equipment():
    cursor = db.get_db().cursor()
    query = '''
        SELECT ID, Name, Price, Lifespan
        FROM Equipment;
    '''
    # get a cursor object from the database
    
    # use cursor to query the database for a list of equipment
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
    response.mimetype='application/json'
    return response

# ------------------------------------------------------------
@equipment.route('/equipment', methods=['POST'])
def add_new_equipment():
    # In a POST request, there is a 
    # collecting data from the request object
    data = request.json
    current_app.logger.info(data)

    #extracting data
    name = data["Name"]
    price = data["Price"]
    lifespan = data["Lifespan"]
   
    query = f'''INSERT INTO Equipment(Name, Price, Lifespan) 
     VALUES('{name}',{price},{lifespan});                                                                       
    '''
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Successfully added equipment")
    response.status_code = 200
    return response
# ------------------------------------------------------------
@equipment.route('/equipment', methods = ["PUT"])
def update_equipment():
    data = request.json
    current_app.logger.info(data)

    #extract data
    new_name = data["Name"]
    new_price = data["Price"]
    new_lifespan = data["Lifespan"]
    id = data["ID"]

    query = '''UPDATE Equipment
                SET Name = %s,  
                    Price = %s,
                    Lifespan= %s
                WHERE ID = %s;                                                                    
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (new_name, new_price, new_lifespan, id))
    db.get_db().commit()

    return make_response("Successfully updated equipment", 200)
