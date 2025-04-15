# `modules` Folder

Currently, we are using this folder to hold functionality that needs to be accessible to the entire application. `nav.py` is a module that supports our custom navigation bar on the left of the app along with some basic Role-Based Access Control (RBAC). 

Our `nav.py` file holds navigation links for 

GENERAL: 
- `HomeNav()`
- `AboutPageNav()`

MANAGER ROLE
- `ManagerPageNav()`
    -Has links to the manager home page, management costs page, and management sales page

CUSTOMER ROLE
- `CustomerHomeNav()`
- `MenuAPINav()`
    -Links to both the customer home page and the up-to-date menu

BAKER ROLE
- `BakerHomeNav()`
- `BakerStockNav()`
    -Links to both the baker home page and the stock tracker page 

CASHIER ROLE
- `CashierHomeNav()`
- `CashierStockNav()`
    -Links to both the cashier home page and the stock tracker page for cashiers

LINKS FUNCTIONS
- There are definitions//UI for the side bar which includes the CookieByte logo, and how the side bar should look depending on the role of the user on the current page