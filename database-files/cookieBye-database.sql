DROP DATABASE IF EXISTS CookieByte;
# Creating a new database called CookieByte
CREATE DATABASE CookieByte;
# Set CookieByte as the current database
USE CookieByte;

-- Table: MenuItem
CREATE TABLE MenuItem
(
    ItemID    INT UNIQUE PRIMARY KEY NOT NULL,
    Status    VARCHAR(20)            NOT NULL,
    Category  VARCHAR(50)            NOT NULL,
    Name      VARCHAR(100)           NOT NULL,
    ShelfLife INT                    NOT NULL,
    Price     DECIMAL(10, 2)         NOT NULL,
    Stock     INT                    NOT NULL
);

-- Alter the table to add AUTO_INCREMENT
ALTER TABLE MenuItem MODIFY ItemID INT AUTO_INCREMENT;

-- Table: Manager
CREATE TABLE Manager
(
    ID        INT UNIQUE PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName  VARCHAR(100),
    Phone     VARCHAR(20) UNIQUE,
    Email     VARCHAR(100) UNIQUE,
    Revenue   DECIMAL
);

-- Table: Supplier
CREATE TABLE Supplier
(
    ID    INT UNIQUE PRIMARY KEY,
    CompanyName  VARCHAR(100),
    ContactPerson VARCHAR(100),
    Phone VARCHAR(20) UNIQUE,
    Email VARCHAR(100) UNIQUE
);


-- Table: SupplyOrder
CREATE TABLE SupplyOrder
(
    ID            INT UNIQUE PRIMARY KEY,
    SupplierID    INT, -- Foreign Key to Supplier
    ManagerID     INT, -- Foreign Key to Manager (who created the order)
    OrderTotal    DECIMAL(10, 2),
    OrderQuantity INT,
    DateOrdered   DATETIME,
    DeliveryDate  DATETIME,
    Delivered     BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_1 FOREIGN KEY (`SupplierID`) REFERENCES Supplier (`ID`)
        ON UPDATE RESTRICT ON DELETE CASCADE,
    CONSTRAINT fk_2 FOREIGN KEY (`ManagerID`) REFERENCES Manager (`ID`)
        ON UPDATE RESTRICT ON DELETE CASCADE
);
ALTER TABLE SupplyOrder MODIFY ID INT AUTO_INCREMENT;

-- Table: Ingredients
CREATE TABLE Ingredients
(
    IngredientID   INT UNIQUE PRIMARY KEY NOT NULL,
    IngredientName VARCHAR(100)           NOT NULL,
    Inventory      INT                    NOT NULL,
    Expiry         INT                    NOT NULL,
    BurnRate       DECIMAL(10, 2)         NOT NULL,
    Price          DECIMAL(10, 2)         NOT NULL
);
ALTER TABLE Ingredients MODIFY IngredientID INT AUTO_INCREMENT;

-- Table: Materials
CREATE TABLE Materials
(
    ID        INT UNIQUE PRIMARY KEY,
    Name      VARCHAR(100),
    Price     DECIMAL(10, 2),
    BurnRate  DECIMAL(10, 2),
    Inventory INT
);
ALTER TABLE Materials MODIFY ID INT AUTO_INCREMENT;

-- Table: Equipment
CREATE TABLE Equipment
(
    ID       INT UNIQUE PRIMARY KEY,
    Name     VARCHAR(100),
    Price    DECIMAL(10, 2),
    Lifespan INT
);
-- Alter the table to add AUTO_INCREMENT
ALTER TABLE Equipment MODIFY ID INT AUTO_INCREMENT;

-- Table: OrderQuantity
-- This table represents the breakdown of a supply order into quantities for ingredients,
-- materials, and equipment.
CREATE TABLE OrderQuantity
(
    OrderQuantityID    INT UNIQUE PRIMARY KEY AUTO_INCREMENT,
    OrderID            INT,
    IngredientID       INT UNIQUE DEFAULT NULL,
    MaterialsID        INT UNIQUE DEFAULT NULL,
    EquipmentID        INT UNIQUE DEFAULT NULL,
    IngredientQuantity INT        DEFAULT NULL,
    MaterialQuantity   INT        DEFAULT NULL,
    EquipmentQuantity  INT        DEFAULT NULL,
    CONSTRAINT fk_3 FOREIGN KEY (`OrderID`) REFERENCES SupplyOrder (`ID`)
        ON UPDATE RESTRICT ON DELETE CASCADE,
    CONSTRAINT fk_4 FOREIGN KEY (`IngredientID`) REFERENCES Ingredients (`IngredientID`)
        ON UPDATE RESTRICT ON DELETE CASCADE,
    CONSTRAINT fk_5 FOREIGN KEY (`MaterialsID`) REFERENCES Materials (`ID`)
        ON UPDATE RESTRICT ON DELETE CASCADE,
    CONSTRAINT fk_6 FOREIGN KEY (`EquipmentID`) REFERENCES Equipment (`ID`)
        ON UPDATE RESTRICT ON DELETE CASCADE
);

-- Table: Employee
CREATE TABLE Employee
(
    ID          INT UNIQUE PRIMARY KEY AUTO_INCREMENT,
    FirstName   VARCHAR(100),
    LastName    VARCHAR(100),
    Position    VARCHAR(50),
    Wage        DECIMAL(10, 2),
    HoursWorked DECIMAL(5, 2),
    ManagerID   INT, -- Foreign Key to Manager
    CONSTRAINT fk_7 FOREIGN KEY (`ManagerID`) REFERENCES Manager (`ID`)
        ON UPDATE RESTRICT ON DELETE SET NULL
);

-- Table: Costs
CREATE TABLE Costs
(
    CostID        INT UNIQUE PRIMARY KEY AUTO_INCREMENT, -- Surrogate Primary Key ??
    Type          VARCHAR(50),
    PaymentDate   DATETIME,
    PaymentAmount DECIMAL(10, 2),
<<<<<<< Updated upstream
    ManagerID     INT UNIQUE,                            -- Foreign Key to Manager (who reviews/receives costs)
    SupplyOrderID INT,                         -- Foreign Key to SupplyOrder (if applicable)
=======
    ManagerID     INT UNIQUE, 
    SupplyOrderID INT,                            -- Foreign Key to Manager (who reviews/receives costs)
>>>>>>> Stashed changes
    CONSTRAINT fk_8 FOREIGN KEY (`ManagerID`) REFERENCES Manager (`ID`)
        ON UPDATE RESTRICT ON DELETE SET NULL
);

-- Table: Sales
CREATE TABLE Sales
(
    SalesID    INT UNIQUE PRIMARY KEY NOT NULL,
    Date       DATETIME               NOT NULL,
    TotalSales DECIMAL(10, 2)         NOT NULL
);

-- Table: TransactionDetails
-- This is a weak entity that details the items in a sale.
CREATE TABLE TransactionDetails
(
    SalesID          INT UNIQUE NOT NULL, -- Foreign Key to Sales
    MenuItemID       INT  NOT NULL, -- Foreign Key to MenuItem
    MenuItemQuantity INT        NOT NULL,
    Date             DATETIME   NOT NULL,
    EmployeeID       INT UNIQUE,
    PRIMARY KEY (SalesID, MenuItemID),
    CONSTRAINT fk_9 FOREIGN KEY (`SalesID`)
        REFERENCES Sales (`SalesID`)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
    CONSTRAINT fk_10 FOREIGN KEY (`MenuItemID`)
        REFERENCES MenuItem (`ItemID`)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
    CONSTRAINT fk_11 FOREIGN KEY (`EmployeeID`)
        REFERENCES Employee (`ID`)
        ON UPDATE RESTRICT
        ON DELETE SET NULL
);