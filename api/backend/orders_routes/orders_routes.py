from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
orders = Blueprint('Orders', __name__)

#------------------------------------------------------------
# Get all the orders
@orders.route('/orders', methods=['GET'])
def get_all_orders():
    query = '''
        SELECT os.ID, s.Name, os.OrderQuantity, os.OrderTotal, os.DateOrdered, os.DeliveryDate
        FROM SupplyOrder os JOIN Supplier s ON s.ID = os.SupplierID;
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()
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
    return response
# ------------------------------------------------------------
@orders.route('/orders/full', methods=['POST'])
def add_full_order():
    data = request.json
    
    supplier_name = data["SupplierName"]
    manager_fname = data["ManagerFirstName"]
    manager_lname = data["ManagerLastName"]
    total = data["OrderTotal"]
    quantity = data["OrderQuantity"]
    date_ordered = data["DateOrdered"]
    date_delivered = data["DeliveryDate"]

    cursor = db.get_db().cursor()

    # get manager ID
    cursor.execute("SELECT ID FROM Manager WHERE FirstName = %s AND LastName = %s", (manager_fname, manager_lname))
    manager_row = cursor.fetchone()
    if not manager_row:
        return jsonify({"error": "Manager not found"}), 400
    manager_id = manager_row['ID']

    # get supplier ID
    cursor.execute("SELECT ID FROM Supplier WHERE Name = %s", (supplier_name,))
    supplier_row = cursor.fetchone()
    if not supplier_row:
        return jsonify({"error": "Supplier not found"}), 400
    supplier_id = supplier_row['ID']

    # insert order
    insert_order_query = '''
        INSERT INTO SupplyOrder(SupplierID, ManagerID, OrderTotal, OrderQuantity, DateOrdered, DeliveryDate)
        VALUES(%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_order_query, (supplier_id, manager_id, total, quantity, date_ordered, date_delivered))
    db.get_db().commit()

    # get the new order ID
    cursor.execute("SELECT LAST_INSERT_ID()")
    row = cursor.fetchone()
    order_id = row.get('LAST_INSERT_ID()')

    # === Order details ===
    ingredient_name = data["IngredientName"]
    material_name = data["MaterialName"]
    equipment_name = data["EquipmentName"]
    ingredient_qty = data["IngredientQuantity"]
    material_qty = data["MaterialQuantity"]
    equipment_qty = data["EquipmentQuantity"]

    # get ingredient ID
    cursor.execute("SELECT IngredientID FROM Ingredients WHERE IngredientName = %s", (ingredient_name,))
    ingredient_row = cursor.fetchone()
    if not ingredient_row:
        return jsonify({"error": f"Ingredient '{ingredient_name}' not found"}), 404
    ingredient_id = ingredient_row['IngredientID']

    # get material ID
    cursor.execute("SELECT ID FROM Materials WHERE Name = %s", (material_name,))
    material_row = cursor.fetchone()
    if not material_row:
        return jsonify({"error": f"Material '{material_name}' not found"}), 404
    material_id = material_row['ID']

    # get equipment ID
    cursor.execute("SELECT ID FROM Equipment WHERE Name = %s", (equipment_name,))
    equipment_row = cursor.fetchone()
    if not equipment_row:
        return jsonify({"error": f"Equipment '{equipment_name}' not found"}), 404
    equipment_id = equipment_row['ID']

    # insert details
    insert_details_query = '''
        INSERT INTO OrderQuantity (OrderID, IngredientID, MaterialsID, EquipmentID,
                                   IngredientQuantity, MaterialQuantity, EquipmentQuantity)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_details_query, (order_id, ingredient_id, material_id, equipment_id,
                                          ingredient_qty, material_qty, equipment_qty))
    db.get_db().commit()

    response = make_response(f"Successfully added order id: {order_id} with details", 200)
    return response

#------------------------------------------------------------
# Update the delivery date and status for an order
@orders.route('/orders', methods = ["PUT"])
def update_deliverystatus():
    data = request.json
    
    #extracting data
    supplier_name = data["SupplierName"]
    new_date = data["DeliveryDate"]
    new_status = data["DeliveryStatus"]
    id = data["OrderID"]

    cursor = db.get_db().cursor()

     # look up supplier id based on name
    cursor.execute("SELECT ID FROM Supplier WHERE Name = %s", (supplier_name,))
    supplier_row = cursor.fetchone()
    if not supplier_row:
        return jsonify({"error": "Supplier not found"}), 400
    supplier_id = supplier_row['ID']

    query = '''UPDATE SupplyOrder
                SET DeliveryDate = %s,  
                    Delivered = %s
                WHERE ID = %s AND SupplierID = %s;                                                                    
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (new_date, new_status, id, supplier_id))
    db.get_db().commit()

    return make_response("Successfully updated delivery status", 200)
# ------------------------------------------------------------
# get information about a specific order
@orders.route('/order/<order_id>', methods=['GET'])
def get_order_detail(order_id):
    try:
        id = int(order_id) 
    except ValueError:
        return make_response(jsonify({"error": "Invalid ID"}), 400)

    query = '''
            SELECT so.OrderQuantity, so.DeliveryDate, so.Delivered, 
                so.ID, oq.IngredientQuantity, oq.MaterialQuantity, 
                oq.EquipmentQuantity, e.Name AS EquipmentName, 
                i.IngredientName, m.Name AS MaterialName
            FROM SupplyOrder so 
            JOIN OrderQuantity oq ON so.ID = oq.OrderID 
            JOIN Equipment e ON e.ID = oq.EquipmentID 
            JOIN Materials m ON m.ID = oq.MaterialsID 
            JOIN Ingredients i ON i.IngredientID = oq.IngredientID 
            JOIN Supplier s ON so.SupplierID = s.ID
            WHERE s.Name = %s AND so.ID = %s
            '''
    cursor = db.get_db().cursor()
    cursor.execute(query,("Sanchez & Sons Sweet Deliveries", order_id))
    theData = cursor.fetchall()
 
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response



 

