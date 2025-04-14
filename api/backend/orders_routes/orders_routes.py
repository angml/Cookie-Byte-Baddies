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
# Get all the equipment information from the database
# and return them to the manager
@orders.route('/orders', methods=['GET'])
def get_all_orders():
    query = '''
        SELECT os.OrderTotal, os.OrderQuantity, os.DateOrdered, 
        os.Delivery Date, os.ID, s.Name, m.Firstame, m.LastName
        FROM SupplyOrder os JOIN Manager m 
        ON os.ManagerID = m.ID
        JOIN Supplier s ON s.ID = os.SupplierID;
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
# LEFT OF HERE

@orders.route('/orders', methods=['POST'])
def add_new_equipment():
    # In a POST request, there is a 
    # collecting data from the request object
    data = request.json
    current_app.longer.info(data)

    #extracting the variable
    supplier_name = data["SupplierName"]
    manager_name = data["ManagerName"]
    total = data["OrderTotal"]
    quantity = data["OrderQuantity"]
    date_ordered = data["DateOrdered"]
    date_delivered = data["DeliveryDate"]
    order_id = data["ID"]

    query = f'''INSERT INTO SupplyOrder(SupplierID, ManagerID, OrderTotal, 
                                        OrderQuantity, DateOrdered, DeliveryDate, ID)
     VALUE({supplier_id},{manager_id},{total},{quantity},
     {date_ordered}, {date_delivered}, {order_id})                                                                        
    '''
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()

    cursor.execute("SELECT ID FROM Manager WHERE Name = %s", (manager_name,))
    manager_row = cursor.fetchone()
    if not manager_row:
        return jsonify({"error": "Manager not found"}), 400
    manager_id = manager_row[0]

    cursor.execute("SELECT ID FROM Supplier WHERE Name = %s", (supplier_name,))
    supplier_row = cursor.fetchone()
    if not supplier_row:
        return jsonify({"error": "Supplier not found"}), 400
    supplier_id = supplier_row[0]



    db.get_db().commit()

    response = make_response("Successfully added equipment")
    response.status_code = 200
    return response
# ------------------------------------------------------------
@equipment.route('/equipment', methods = ["PUT"])
def update_equipment():
    data = request.json
    current_app.logger.info(info)

    #variables
    new_name = data["Name"]
    new_price = data["Price"]
    new_lifespan = data["Lifespan"]
    new_id = data["ID"]

    query = '''UPDATE Equipment
                SET Name = %s,  
                    Price = %f,
                    Lifespan= %d, 
                    ID = %d),                                                                       
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (new_name, new_price, new_lifespan, new_id))
    db.get_db().commit()

    return make_response("Successfully updated cost", 200)

# ------------------------------------------------------------
# get product information about a specific product
# notice that the route takes <id> and then you see id
# as a parameter to the function.  This is one way to send 
# parameterized information into the route handler.
    @products.route('/product/<id>', methods=['GET'])
def get_product_detail (id):

    query = f'''SELECT id, 
                       product_name, 
                       description, 
                       list_price, 
                       category 
                FROM products 
                WHERE id = {str(id)}
    '''
    
    current_app.logger.info(f'GET /product/<id> query={query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /product/<id> Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# # ------------------------------------------------------------
# # Get the top 5 most expensive products from the database
# @products.route('/mostExpensive')
# def get_most_pop_products():

#     query = '''
#         SELECT product_code, 
#                product_name, 
#                list_price, 
#                reorder_level
#         FROM products
#         ORDER BY list_price DESC
#         LIMIT 5
#     '''
    
#     # Same process as handler above
#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     theData = cursor.fetchall()
 
#     response = make_response(jsonify(theData))
#     response.status_code = 200
#     return response

# # ------------------------------------------------------------
# # Route to get the 10 most expensive items from the 
# # database.
# @products.route('/tenMostExpensive', methods=['GET'])
# def get_10_most_expensive_products():
    
#     query = '''
#         SELECT product_code, 
#                product_name, 
#                list_price, 
#                reorder_level
#         FROM products
#         ORDER BY list_price DESC
#         LIMIT 10
#     '''
    
#     # Same process as above
#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     theData = cursor.fetchall()
    
#     response = make_response(jsonify(theData))
#     response.status_code = 200
#     return response
    

# # ------------------------------------------------------------
# # This is a POST route to add a new product.
# # Remember, we are using POST routes to create new entries
# # in the database. 
# @products.route('/product', methods=['POST'])
# def add_new_product():
    
#     # In a POST request, there is a 
#     # collecting data from the request object 
#     the_data = request.json
#     current_app.logger.info(the_data)

#     #extracting the variable
#     name = the_data['product_name']
#     description = the_data['product_description']
#     price = the_data['product_price']
#     category = the_data['product_category']
    
#     query = f'''
#         INSERT INTO products (product_name,
#                               description,
#                               category, 
#                               list_price)
#         VALUES ('{name}', '{description}', '{category}', {str(price)})
#     '''
#     # TODO: Make sure the version of the query above works properly
#     # Constructing the query
#     # query = 'insert into products (product_name, description, category, list_price) values ("'
#     # query += name + '", "'
#     # query += description + '", "'
#     # query += category + '", '
#     # query += str(price) + ')'
#     current_app.logger.info(query)

#     # executing and committing the insert statement 
#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     db.get_db().commit()
    
#     response = make_response("Successfully added product")
#     response.status_code = 200
#     return response

# # ------------------------------------------------------------
# ### Get all product categories
# @products.route('/categories', methods = ['GET'])
# def get_all_categories():
#     query = '''
#         SELECT DISTINCT category AS label, category as value
#         FROM products
#         WHERE category IS NOT NULL
#         ORDER BY category
#     '''

#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     theData = cursor.fetchall()
        
#     response = make_response(jsonify(theData))
#     response.status_code = 200
#     return response

