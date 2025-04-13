########################################################
# Costs blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
costs = Blueprint('Costs', __name__)

#------------------------------------------------------------


# Get all costs from the system
@costs.route('/costs', methods=['GET'])
def get_all_costs():
    cursor = db.get_db().cursor()
    the_query = ''' 
        SELECT DISTINCT Type
        FROM Costs;
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype='application/json'
    return the_response


# Get costs from system based on specified type
@costs.route('/type/<string:cost_type>', methods=['GET'])
def get_costs_by_type(cost_type):
    cursor = db.get_db().cursor()


    the_query = ''' 
        SELECT CostID, Type, PaymentDate, PaymentAmount, ManagerID
        FROM Costs
        WHERE Type = %s;
    '''
    cursor.execute(the_query, (cost_type,))
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype='application/json'
    return the_response

# Add a new cost
@costs.route('/cost', methods=['POST'])
def add_new_cost():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    cost_type = the_data['Type']              
    payment_date = the_data['PaymentDate']     
    payment_amount = the_data['PaymentAmount']        
    
    query = f'''
        INSERT INTO Costs (Type, PaymentDate, PaymentAmount)
        VALUES ('{cost_type}', '{payment_date}', {str(payment_amount)})
    '''
    current_app.logger.info(query)
    
    # execute the insert statement and commit the changes
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added cost")
    response.status_code = 200
    return response


# Get all cost records filtered by the payment date
@costs.route('/costs/date/<string:cost_date>', methods=['GET'])
def get_costs_by_date(cost_date):
    cursor = db.get_db().cursor()
    # DATE() function to match the date portion of PaymentDate
    the_query = ''' 
        SELECT CostID, Type, PaymentDate, PaymentAmount, ManagerID
        FROM Costs
        WHERE DATE(PaymentDate) = %s;
    '''
    cursor.execute(the_query, (cost_date,))
    theData = cursor.fetchall()
    return make_response(jsonify(theData), 200)


# Update a cost record that occurred on the given payment date
@costs.route('/costs/id/<int:cost_id>', methods=['PUT'])
def update_cost_by_id(cost_id):
    new_data = request.json
    current_app.logger.info(new_data)

    new_type = new_data['Type']
    new_date = new_data['PaymentDate']
    new_amount = new_data['PaymentAmount']
    new_manager_id = new_data['ManagerID']

    query = '''
        UPDATE Costs
        SET Type = %s,
            PaymentDate = %s,
            PaymentAmount = %s,
            ManagerID = %s
        WHERE CostID = %s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (new_type, new_date, new_amount, new_manager_id, cost_id))
    db.get_db().commit()

    return make_response("Successfully updated cost", 200)


