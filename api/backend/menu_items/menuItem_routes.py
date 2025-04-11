########################################################
# Sample menu items blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
menuItems = Blueprint('menuItems', __name__)

#------------------------------------------------------------
# Get all customers from the system
@menuItems.route('/menu-items', methods=['GET'])
def get_all_menuItems():
    cursor = db.get_db().cursor()
    the_query = ''' 
        SELECT ItemID, Name, Status, Price, Category, Stock, ShelfLife
        FROM MenuItem;
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype='application/json'
    return the_response