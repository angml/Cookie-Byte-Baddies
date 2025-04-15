use CookieByte;

INSERT INTO MenuItem(ItemID, Status, Category, Name, ShelfLife, Price, Stock)
    VALUES
        (1, 'Available', 'Pastry', 'Croissant', 2, 3.49, 20),
        (2, 'Available', 'Pastry', 'Blueberry Muffin', 2, 3.99, 15),
        (3, 'Available', 'Sandwich', 'Turkey & Swiss Sandwich', 2, 7.99, 10),
        (4, 'Unavailable', 'Sandwich', 'Caprese Panini', 2, 8.49, 0),
        (8, 'Unavailable', 'Dessert', 'Tiramisu', 2, 6.99, 0),
        (9, 'Available', 'Dessert', 'Cherry Pie', 3, 2.99, 30),
        (10, 'Available', 'Sandwich', 'Avocado Toast', 1, 5.99, 8);

INSERT INTO Manager(ID, FirstName, Phone, Email, Revenue, LastName)
    VALUES
        (1, 'Mandy','508-555-2345', 'mandymanager@siphappens.com', 120000.00, 'Manager'),
        (2, 'Ethan', '978-555-3456', 'ethan.brown@siphappens.com', 105000.00, 'Brown');

INSERT INTO Supplier(ID, Name, Phone, Email)
    VALUES
        (1, 'Sanchez & Sons Sweet Deliveries', '617-555-1234', 'deliveries@sancheznsons.com'),
        (2, 'Baker’s Best', '413-555-4567', 'orders@bakersbest.com');

INSERT INTO SupplyOrder(ID, SupplierID, ManagerID, OrderTotal, OrderQuantity, DateOrdered, DeliveryDate)
    VALUES
        (1, 1, 1, 750.50, 20, '2025-03-15', '2025-03-20'),
        (2, 2, 2, 1250.00, 30, '2025-03-03', '2025-03-09');

INSERT INTO Ingredients(IngredientID, IngredientName, Inventory, Expiry, BurnRate, Price)
    VALUES
        (1, 'Espresso Beans', 5, 14, 1, 15.99),
        (2, 'Whole Milk', 10, 7, 5, 3.49),
        (3, 'Butter', 5, 14, 2, 2.99),
        (4, 'Flour', 10, 171, 4, 1.99),
        (5, 'Sugar', 10, 182, 3, 1.49);

INSERT INTO Materials(ID, Name, Price, BurnRate, Inventory)
     VALUES
        (1, 'Coffee Cups', 0.15, 50, 500),
        (2, 'Plastic Lids', 0.05, 50, 500),
        (3, 'Paper Napkins', 0.02, 100, 1000),
        (4, 'Plastic Forks', 0.10, 30, 300),
        (5, 'Straws', 0.03, 40, 400);

INSERT INTO Equipment(ID, Name, Price, Lifespan)
     VALUES
        (1, 'Baking Tray', 30.99, 7),
        (2, 'Wire Whisk', 3.99, 4),
        (3, 'Mixing Bowl', 11.99, 6),
        (4, 'Electric Mixer', 399.99, 10);

INSERT INTO OrderQuantity(OrderQuantityID, OrderID, IngredientID, MaterialsID, EquipmentID, IngredientQuantity, MaterialQuantity, EquipmentQuantity)
     VALUES
        (1, 1, 1, NULL, NULL, 10, NULL, NULL),  -- 10 units of Espresso Beans for OrderID 1
        (2, 1, 3, NULL, NULL, 8, NULL, NULL),   -- 8 units of Butter for OrderID 1
        (3, 2, 2, NULL, NULL, 15, NULL, NULL),  -- 15 units of Whole Milk for OrderID 2
        (4, 2, 4, NULL, NULL, 20, NULL, NULL),  -- 20 units of Flour for OrderID 2
        (5, 1, NULL, 1, NULL, NULL, 200, NULL), -- 200 units of Coffee Cups for OrderID 1
        (6, 1, NULL, 2, NULL, NULL, 150, NULL), -- 150 units of Plastic Lids for OrderID 1
        (7, 2, NULL, 3, NULL, NULL, 300, NULL), -- 300 units of Paper Napkins for OrderID 2
        (8, 2, NULL, 4, NULL, NULL, 100, NULL), -- 100 units of Plastic Forks for OrderID 2
        (9, 1, NULL, NULL, 1, NULL, NULL, 5),   -- 5 units of Baking Tray for OrderID 1
        (10, 1, NULL, NULL, 2, NULL, NULL, 3),  -- 3 units of Wire Whisk for OrderID 1
        (11, 2, NULL, NULL, 3, NULL, NULL, 2),  -- 2 units of Mixing Bowl for OrderID 2
        (12, 2, NULL, NULL, 4, NULL, NULL, 1); -- 1 unit of Electric Mixer for OrderID 2

INSERT INTO Employee(ID, FirstName, Position, Wage, HoursWorked, ManagerID, LastName)
     VALUES
            (1, 'Connor', 'Cashier', 15, 20, 1, 'Singh'),
            (2, 'Pearl', 'Baker', 25, 40,1,  'Thepnakorn' );

INSERT INTO Costs(CostID, Type, PaymentDate, PaymentAmount, ManagerID, SupplyOrderID)
     VALUES
            (1, 'Labor', '2025-03-24', 1500.00, 1, NULL),
            (2, 'Supplies', '2025-03-15', 750.50, 2, 1);

INSERT INTO Sales(SalesID, Date, TotalSales)
     VALUES
        (1, '2025-04-01', 350.75),
        (2, '2025-03-31', 420.50),
        (3, '2025-03-30', 380.00);

INSERT INTO TransactionDetails(SalesID, MenuItemID, MenuItemQuantity, Date)
     VALUES
        (1, 1, 3, '2025-04-01'),
        (1, 2, 2, '2025-04-01'),
        (2, 3, 4, '2025-03-31'),
        (2, 4, 1, '2025-03-31'),
        (3, 1, 2, '2025-03-30'),
        (3, 8, 3, '2025-03-30');





