from flask import Flask

from backend.db_connection import db
from backend.employees.employees_routes import employees
from backend.suppliers.supplier_routes import suppliers
from backend.menu_items.menuItem_routes import menuItems
from backend.cost_routes.cost_routes import costs
from backend.equipment_routes.equipment_routes import equipment
from backend.sales_routes.sales_routes import sales
from backend.orders_routes.orders_routes import orders
from backend.materials.material_routes import materials
from backend.ingredients.ingredient_routes import ingredients

import os 
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Load environment variables
    # This function reads all the values from inside
    # the .env file (in the parent folder) so they
    # are available in this file.  See the MySQL setup 
    # commands below to see how they're being used.
    load_dotenv()

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # # these are for the DB object to be able to connect to MySQL. 
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER').strip()
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD').strip()
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST').strip()
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT').strip())
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME').strip()  # Change this to your DB name

    # Initialize the database object with the settings above. 
    app.logger.info('current_app(): starting the database connection')
    db.init_app(app)


    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.logger.info('current_app(): registering blueprints with Flask app object.')   
    app.register_blueprint(menuItems,   url_prefix='/m')
    app.register_blueprint(employees,   url_prefix='/e')
    app.register_blueprint(suppliers,   url_prefix='/s')
    app.register_blueprint(costs, url_prefix='/costs')
    app.register_blueprint(equipment, url_prefix='/eq')
    app.register_blueprint(sales, url_prefix='/sales')
    app.register_blueprint(orders, url_prefix = '/o' )
    app.register_blueprint(materials, url_prefix = '/m' )
    app.register_blueprint(ingredients, url_prefix = '/i' )
    # Don't forget to return the app object
    return app

