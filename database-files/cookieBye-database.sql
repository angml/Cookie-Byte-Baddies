DROP DATABASE IF EXISTS CookieByte;

# Creating a new database called CookieByte
CREATE DATABASE CookieByte;
# Set CookieByte as the current database
USE CookieByte;

-- Table: MenuItem
CREATE TABLE MenuItem (
    ItemID INT PRIMARY KEY,
    Status VARCHAR(20),
    Category VARCHAR(50),
    Name VARCHAR(100),
    ShelfLife INT,
    Price DECIMAL(10,2),
    Stock INT
);

-- Table: Manager
CREATE TABLE Manager (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Revenue DECIMAL
);

-- Table: Supplier
CREATE TABLE Supplier (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100)
);

-- Table: SupplyOrder
CREATE TABLE SupplyOrder (
    ID INT PRIMARY KEY,
    SupplierID INT,                     -- Foreign Key to Supplier
    ManagerID INT,                      -- Foreign Key to Manager (who created the order)
    OrderTotal DECIMAL(10,2),
    OrderQuantity INT,
    DateOrdered DATETIME,
    DeliveryDate DATETIME,
    FOREIGN KEY (SupplierID) REFERENCES Supplier(ID),
    FOREIGN KEY (ManagerID) REFERENCES Manager(ID)
);

-- Table: Ingredients
CREATE TABLE Ingredients (
    IngredientID INT PRIMARY KEY,
    IngredientName VARCHAR(100),
    Inventory INT,
    Expiry INT,
    BurnRate DECIMAL(10,2),
    Price DECIMAL(10,2)
);

-- Table: Materials
CREATE TABLE Materials (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Price DECIMAL(10,2),
    BurnRate DECIMAL(10,2),
    Inventory INT
);

-- Table: Equipment
CREATE TABLE Equipment (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Price DECIMAL(10,2),
    Lifespan INT
);

-- Table: OrderQuantity
-- This table represents the breakdown of a supply order into quantities for ingredients,
-- materials, and equipment.
CREATE TABLE OrderQuantity (
    OrderQuantityID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,                        -- Foreign Key to SupplyOrder
    IngredientID INT,                   -- Foreign Key to Ingredients
    MaterialsID INT NULL,               -- Foreign Key to Materials ??
    EquipmentID INT NULL,               -- Foreign Key to Equipment ??
    IngredientQuantity INT,
    MaterialQuantity INT,
    EquipmentQuantity INT,
    FOREIGN KEY (OrderID) REFERENCES SupplyOrder(ID),
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID),
    FOREIGN KEY (MaterialsID) REFERENCES Materials(ID),
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(ID)
);

-- Table: Employee
CREATE TABLE Employee (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Position VARCHAR(50),
    Wage DECIMAL(10,2),
    HoursWorked DECIMAL(5,2),
    ManagerID INT,                      -- Foreign Key to Manager
    FOREIGN KEY (ManagerID) REFERENCES Manager(ID)
);

-- Table: Costs
CREATE TABLE Costs (
    CostID INT PRIMARY KEY AUTO_INCREMENT,   -- Surrogate Primary Key ??
    Type VARCHAR(50),
    PaymentDate DATETIME,
    PaymentAmount DECIMAL(10,2),
    ManagerID INT,                             -- Foreign Key to Manager (who reviews/receives costs)
    SupplyOrderID INT,                         -- Foreign Key to SupplyOrder (if applicable)
    FOREIGN KEY (ManagerID) REFERENCES Manager(ID),
    FOREIGN KEY (SupplyOrderID) REFERENCES SupplyOrder(ID)
);

-- Table: Sales
CREATE TABLE Sales (
    SalesID INT PRIMARY KEY,
    Date DATETIME,
    TotalSales DECIMAL(10,2)
);

-- Table: TransactionDetails
-- This is a weak entity that details the items in a sale.
CREATE TABLE TransactionDetails (
    SalesID INT,                               -- Foreign Key to Sales
    MenuItemID INT,                            -- Foreign Key to MenuItem
    MenuItemQuantity INT,
    Date DATETIME,
    PRIMARY KEY (SalesID, MenuItemID),
    FOREIGN KEY (SalesID) REFERENCES Sales(SalesID),
    FOREIGN KEY (MenuItemID) REFERENCES MenuItem(ItemID)
);

ALTER TABLE Manager
RENAME COLUMN Name to FirstName,
ADD LastName varchar (100);

ALTER TABLE Employee
RENAME COLUMN Name to FirstName,
ADD LastName varchar (100);

ALTER TABLE TransactionDetails
ADD EmployeeID INT;

ALTER TABLE TransactionDetails
ADD CONSTRAINT FK_Employee
FOREIGN KEY (EmployeeID) REFERENCES Employee(ID);

