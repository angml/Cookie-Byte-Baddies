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
# Get all the orders for mananger
@orders.route('/orders', methods=['GET'])
def get_manager_orders():
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
# Add to the order history for manager
@orders.route('/orders', methods=['POST'])
def add_new_orders():
    # In a POST request, there is a 
    # collecting data from the request object
    data = request.json

    #extracting data
    supplier_name = data["SupplierName"]
    manager_fname = data["ManagerFirstName"]
    manager_lname = data["ManagerLastName"]
    total = data["OrderTotal"]
    quantity = data["OrderQuantity"]
    date_ordered = data["DateOrdered"]
    date_delivered = data["DeliveryDate"]

    cursor = db.get_db().cursor()

    # look up manager id based on name
    cursor.execute("SELECT ID FROM Manager WHERE FirstName = %s AND  LastName = %s", (manager_fname, manager_lname))
    manager_row = cursor.fetchone()
    if not manager_row:
        return jsonify({"error": "Manager not found"}), 400
    manager_id = manager_row['ID']

    # look up supplier id based on name
    cursor.execute("SELECT ID FROM Supplier WHERE Name = %s", (supplier_name,))
    supplier_row = cursor.fetchone()
    if not supplier_row:
        return jsonify({"error": "Supplier not found"}), 400
    supplier_id = supplier_row['ID']

    # insert query with the supplier and manager ids
    query = '''INSERT INTO SupplyOrder(SupplierID, ManagerID, OrderTotal, 
                                    OrderQuantity, DateOrdered, DeliveryDate)
    VALUES(%s, %s, %s, %s, %s, %s);                                                                    
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query,(supplier_id, manager_id, total, quantity, date_ordered, date_delivered))
    db.get_db().commit()

    response = make_response("Successfully added order")
    response.status_code = 200
    return response
#------------------------------------------------------------
# Update the delivery date and status for an order for Supplier
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

    return make_response("Succesfully created order", 200)
# ------------------------------------------------------------
# get information about a specific order for Supplier
@orders.route('/orders/<order_id>', methods=['GET'])
def get_order_detail(order_id):
    print(f"Received order_id: {order_id}")
    query = '''
            SELECT 
                so.ID, oq.IngredientQuantity, oq.MaterialQuantity,
                oq.EquipmentQuantity, e.Name AS EquipmentName,
                i.IngredientName, m.Name AS MaterialName
            FROM SupplyOrder so
            JOIN OrderQuantity oq ON so.ID = oq.OrderID
            LEFT OUTER JOIN Equipment e ON e.ID = oq.EquipmentID
            LEFT OUTER JOIN Materials m ON m.ID = oq.MaterialsID
            LEFT OUTER JOIN Ingredients i ON i.IngredientID = oq.IngredientID
            JOIN Supplier s ON so.SupplierID = s.ID
            WHERE s.Name = %s AND so.ID = %s;
            '''
    cursor = db.get_db().cursor()
    cursor.execute(query,('Sanchez & Sons Sweet Deliveries', order_id))
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
# ------------------------------------------------------------
# get orders information for Supplier
@orders.route('/orders/supplier', methods=['GET'])
def get_supplier_orders():
    query = '''
        SELECT so.ID, so.OrderQuantity, so.DeliveryDate, so.Delivered
        FROM SupplyOrder so JOIN Supplier s 
        ON so.SupplierID = s.ID
        WHERE s.CompanyName = %s;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, ("Sanchez & Sons Sweet Deliveries"))
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    print(response)
    response.status_code = 200
    return response






 

