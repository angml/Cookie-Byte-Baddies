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
# Get all menu items from the system
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

### Get all menu-items categories
@menuItems.route('/categories', methods = ['GET'])
def get_all_menu_categories():
    query = '''
        SELECT DISTINCT Category AS label, Category as value
        FROM MenuItem
        WHERE Category IS NOT NULL
        ORDER BY Category
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Get all menu-items BY category 
@menuItems.route('/menu-items/category/<category>', methods=['GET'])
def get_menuItems_by_category(category):
    cursor = db.get_db().cursor()
    query = '''
        SELECT ItemID, Name, Status, Price, Category, Stock, ShelfLife
        FROM MenuItem
        WHERE Category = %s;
    '''
    cursor.execute(query, (category,))
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get all menu items and their stock amount from the system
@menuItems.route('/menu-items/stocks', methods=['GET'])
def get_menuItems_stocks():
    cursor = db.get_db().cursor()
    the_query = ''' 
        SELECT ItemID, Name, Stock
        FROM MenuItem;
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype='application/json'
    return the_response

# Update stock of a menu item
@menuItems.route('/menu-items/update-stock/<int:item_id>', methods=['PUT'])
def update_menu_item_stock(item_id):
    try:
        data = request.get_json()
        new_stock = data.get('Stock')

        if new_stock is None:
            return jsonify({"error": "Missing 'Stock' in request body"}), 400

        # Determine new status
        new_status = "Unavailable" if new_stock == 0 else "Available"

        cursor = db.get_db().cursor()
        update_query = '''
            UPDATE MenuItem
            SET Stock = %s, Status = %s
            WHERE ItemID = %s;
        '''
        cursor.execute(update_query, (new_stock, new_status, item_id))
        db.get_db().commit()

        return jsonify({"message": "Stock and status updated successfully!"}), 200

    except Exception as e:
        current_app.logger.error(f"Error updating stock: {e}")
        return jsonify({"error": "An error occurred while updating stock."}), 500
    
# Delete menu item 
@menuItems.route('/menu-items/delete/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    cursor = db.get_db().cursor()

    # Check if the item exists
    cursor.execute('SELECT * FROM MenuItem WHERE ItemID = %s', (item_id,))
    if not cursor.fetchone():
        return jsonify({"error": "Item not found"}), 404

    # Delete the item
    cursor.execute('DELETE FROM MenuItem WHERE ItemID = %s', (item_id,))
    db.get_db().commit()

    return jsonify({"message": "Item deleted successfully"}), 200

# Create a NEW menu item
@menuItems.route('/menu-items/create', methods=['POST'])
def create_menu_item():
    data = request.get_json()

    # Get data from the request body
    name = data.get('Name')
    status = data.get('Status')
    price = data.get('Price')
    category = data.get('Category')
    stock = data.get('Stock')
    shelf_life = data.get('ShelfLife')

    # SQL query to insert a new menu item (no need for ItemID since it's auto-incremented)
    query = '''
    INSERT INTO MenuItem (Name, Status, Price, Category, Stock, ShelfLife)
    VALUES (%s, %s, %s, %s, %s, %s);
    '''

    # Insert data into the database
    cursor = db.get_db().cursor()
    cursor.execute(query, (name, status, price, category, stock, shelf_life))
    db.get_db().commit()

    return jsonify({"message": "Menu item created successfully"}), 201



