########################################################
# Sample supply orders blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
supplyOrders = Blueprint('supplyOrders', __name__)

#------------------------------------------------------------
# Get all the supply orders from the database, package them up,
# and return them to the client
@supplyOrders.route('/supply-orders', methods=['GET'])
def get_supply_orders():
    query = '''
        SELECT ID, OrderQuantity, OrderTotal, DateOrdered, DeliveryDate, SupplierID, ManagerID
        FROM SupplyOrder;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response

# ------------------------------------------------------------
# get supply order information about a specific supply order
# notice that the route takes <id> and then you see id
# as a parameter to the function.  This is one way to send 
# parameterized information into the route handler.
@supplyOrders.route('/supply-order/<id>', methods=['GET'])
def get_supply_order_detail (id):

    query = f'''
            SELECT ID, OrderQuantity, OrderTotal, 
            DateOrdered, DeliveryDate, SupplierID, ManagerID
        FROM SupplyOrder
        WHERE ID = {str(id)};
    '''
    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /supply-order/<id> query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /supply-order/<id> Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response