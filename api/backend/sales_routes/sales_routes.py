########################################################
# Sales blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
sales = Blueprint('Sales', __name__)

#------------------------------------------------------------


# Get all sales from the system
@sales.route('/sales', methods=['GET'])
def get_all_sales():
    cursor = db.get_db().cursor()
    the_query = ''' 
        SELECT SalesID, Date, TotalSales
        FROM Sales;
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype='application/json'
    return the_response


# Get all sales records for a specific year and month
@sales.route('/sales/month/<int:year>/<int:month>', methods=['GET'])
def get_sales_by_month(year, month):
    cursor = db.get_db().cursor()
    the_query = '''
        SELECT SalesID, Date, TotalSales
        FROM Sales
        WHERE YEAR(Date) = %s AND MONTH(Date) = %s;
    '''
    cursor.execute(the_query, (year, month))
    theData = cursor.fetchall()
    return make_response(jsonify(theData), 200)

# Get all sales for a specific menu item
@sales.route('/sales/menuitem/<string:menu_item_name>', methods=['GET'])
def get_total_sales_for_menu_item(menu_item_name):
    cursor = db.get_db().cursor()
    query = '''
        SELECT m.Name, SUM(td.MenuItemQuantity * m.Price) AS TotalRevenue
        FROM TransactionDetails td
        JOIN Sales s ON td.SalesID = s.SalesID
        JOIN MenuItem m ON td.MenuItemID = m.ItemID
        WHERE m.Name = %s
        GROUP BY m.Name;
    '''
    cursor.execute(query, (menu_item_name,))
    row = cursor.fetchone()
    if row is None:
        total_revenue = 0
        item_name = menu_item_name
    else:
        item_name, total_revenue = row

    return make_response(jsonify({"MenuItem": item_name, "TotalRevenue": total_revenue}), 200)
