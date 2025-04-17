use CookieByte;

INSERT INTO MenuItem(ItemID, Status, Category, Name, ShelfLife, Price, Stock)
    VALUES
        (1, 'Available', 'Pastry', 'Croissant', 2, 3.49, 20),
        (2, 'Available', 'Pastry', 'Blueberry Muffin', 2, 3.99, 15),
        (3, 'Available', 'Sandwich', 'Turkey & Swiss Sandwich', 2, 7.99, 10),
        (4, 'Unavailable', 'Sandwich', 'Caprese Panini', 2, 8.49, 0),
        (8, 'Unavailable', 'Dessert', 'Tiramisu', 2, 6.99, 0),
        (9, 'Available', 'Dessert', 'Cherry Pie', 3, 2.99, 30),
        (10, 'Available', 'Sandwich', 'Avocado Toast', 1, 5.99, 8),
        (11, 'Available', 'Pastry', 'Almond Croissant', 2, 3.99, 12),
        (12, 'Available', 'Pastry', 'Chocolate Chip Muffin', 2, 3.89, 18),
        (13, 'Unavailable', 'Pastry', 'Cinnamon Roll', 2, 4.25, 0),
        (14, 'Available', 'Sandwich', 'Ham & Cheese Croissant', 1, 6.49, 7),
        (15, 'Available', 'Sandwich', 'Chicken Caesar Wrap', 2, 7.49, 9),
        (16, 'Available', 'Dessert', 'Brownie', 3, 2.49, 25),
        (17, 'Unavailable', 'Dessert', 'Cheesecake', 3, 5.99, 0),
        (18, 'Available', 'Pastry', 'Banana Bread', 3, 3.25, 14),
        (19, 'Available', 'Pastry', 'Lemon Poppyseed Muffin', 2, 3.75, 11),
        (20, 'Available', 'Sandwich', 'Grilled Cheese', 1, 5.49, 6),
        (21, 'Available', 'Sandwich', 'BLT Sandwich', 1, 6.99, 5),
        (22, 'Available', 'Sandwich', 'Egg Salad Sandwich', 1, 6.49, 7),
        (23, 'Unavailable', 'Dessert', 'Chocolate Cake', 3, 6.49, 0),
        (24, 'Unavailable', 'Dessert', 'Apple Pie', 3, 3.49, 0),
        (25, 'Unavailable', 'Pastry', 'Pumpkin Muffin', 2, 3.99, 0),
        (26, 'Unavailable', 'Pastry', 'Scone', 2, 3.29, 0),
        (27, 'Available', 'Pastry', 'Butter Croissant', 2, 3.59, 16),
        (28, 'Available', 'Sandwich', 'Veggie Wrap', 2, 6.99, 8),
        (29, 'Unavailable', 'Sandwich', 'Roast Beef Sandwich', 2, 7.99, 0),
        (30, 'Available', 'Dessert', 'Peach Tart', 3, 4.99, 10),
        (31, 'Unavailable', 'Dessert', 'Oreo Cheesecake', 3, 5.49, 0),
        (32, 'Available', 'Pastry', 'Chocolate Danish', 2, 3.75, 17),
        (33, 'Unavailable', 'Pastry', 'Strawberry Danish', 2, 3.75, 0),
        (34, 'Unavailable', 'Dessert', 'Lemon Tart', 2, 4.49, 0),
        (35, 'Available', 'Dessert', 'Vanilla Cupcake', 2, 3.25, 21);
;

INSERT INTO Manager(ID, FirstName,LastName,Phone, Email, Revenue)
    VALUES
        (1, 'Mandy', 'Manager','508-555-2345', 'mandymanager@siphappens.com', 120000.00),
        (2, 'Ethan', 'Brown','978-555-3456', 'ethan.brown@siphappens.com', 105000.00),
        (3, 'Clara', 'Nguyen', '617-555-1003', 'clara.nguyen@example.com', 134500.00),
        (4, 'Daniel', 'Garcia', '617-555-1004', 'daniel.garcia@example.com', 88000.00),
        (5, 'Elena', 'Martinez', '617-555-1005', 'elena.martinez@example.com', 112300.25),
        (6, 'Frank', 'White', '617-555-1006', 'frank.white@example.com', 102000.00),
        (7, 'Grace', 'Kim', '617-555-1007', 'grace.kim@example.com', 97000.50),
        (8, 'Hannah', 'Smith', '617-555-1008', 'hannah.smith@example.com', 89000.00),
        (9, 'Ivan', 'Petrov', '617-555-1009', 'ivan.petrov@example.com', 115400.75),
        (10, 'Julia', 'Chen', '617-555-1010', 'julia.chen@example.com', 122000.10),
        (11, 'Kevin', 'Turner', '617-555-1011', 'kevin.turner@example.com', 108800.00),
        (12, 'Linda', 'Reed', '617-555-1012', 'linda.reed@example.com', 93000.00),
        (13, 'Mark', 'Bennett', '617-555-1013', 'mark.bennett@example.com', 123500.00),
        (14, 'Nina', 'Owens', '617-555-1014', 'nina.owens@example.com', 110750.00),
        (15, 'Oscar', 'Lopez', '617-555-1015', 'oscar.lopez@example.com', 117000.00),
        (16, 'Paula', 'Diaz', '617-555-1016', 'paula.diaz@example.com', 99000.00),
        (17, 'Quincy', 'Brown', '617-555-1017', 'quincy.brown@example.com', 98000.00),
        (18, 'Rachel', 'Green', '617-555-1018', 'rachel.green@example.com', 103500.00),
        (19, 'Sam', 'Harris', '617-555-1019', 'sam.harris@example.com', 127500.00),
        (20, 'Tina', 'Morgan', '617-555-1020', 'tina.morgan@example.com', 95000.00),
        (21, 'Umar', 'Ali', '617-555-1021', 'umar.ali@example.com', 109000.00),
        (22, 'Vera', 'Foster', '617-555-1022', 'vera.foster@example.com', 101250.00),
        (23, 'Will', 'Clark', '617-555-1023', 'will.clark@example.com', 113000.00),
        (24, 'Xena', 'Knight', '617-555-1024', 'xena.knight@example.com', 87000.00),
        (25, 'Yusuf', 'Taylor', '617-555-1025', 'yusuf.taylor@example.com', 99000.00),
        (26, 'Zara', 'Evans', '617-555-1026', 'zara.evans@example.com', 104500.00),
        (27, 'Amy', 'Bell', '617-555-1027', 'amy.bell@example.com', 91000.00),
        (28, 'Ben', 'Adams', '617-555-1028', 'ben.adams@example.com', 89000.00),
        (29, 'Cleo', 'Stone', '617-555-1029', 'cleo.stone@example.com', 123000.00),
        (30, 'Derek', 'Hill', '617-555-1030', 'derek.hill@example.com', 93500.00),
        (31, 'Emily', 'Watts', '617-555-1031', 'emily.watts@example.com', 108000.00),
        (32, 'Fred', 'Sharp', '617-555-1032', 'fred.sharp@example.com', 97000.00),
        (33, 'Gina', 'Palmer', '617-555-1033', 'gina.palmer@example.com', 114000.00),
        (34, 'Harvey', 'Walsh', '617-555-1034', 'harvey.walsh@example.com', 101000.00),
        (35, 'Isla', 'Bishop', '617-555-1035', 'isla.bishop@example.com', 119000.00);

INSERT INTO Supplier(ID, CompanyName, ContactPerson, Phone, Email)
    VALUES
        (1, 'Sanchez & Sons Sweet Deliveries', 'Sally Supplier','617-555-1234', 'deliveries@sancheznsons.com'),
        (2, 'Baker’s Best', 'Bernie Other','413-555-4567', 'orders@bakersbest.com'),
        (3, 'Daily Dough Distributors', 'Daisy Dough','617-555-2001', 'daisy@dailydough.com'),
        (4, 'Gourmet Goods Co.', 'Gordon Goods','508-555-2002', 'gordon@gourmetgoods.com'),
        (5, 'Whisk & Whittle', 'Wanda Whittle','781-555-2003', 'wanda@whiskwhittle.com'),
        (6, 'Fresh Picks Produce', 'Felix Farmer','978-555-2004', 'felix@freshpicks.com'),
        (7, 'North Shore Dairies', 'Nina North','978-555-2005', 'nina@northshoredairy.com'),
        (8, 'Golden Grain Suppliers', 'Greg Grain','508-555-2006', 'greg@goldengrain.com'),
        (9, 'Rise & Shine Bakers', 'Rita Rise','781-555-2007', 'rita@riseandshine.com'),
        (10, 'Coastal Coffee Co.', 'Carl Coffee','617-555-2008', 'carl@coastalcoffee.com'),
        (11, 'Berry Bros. Farms', 'Ben Berry','413-555-2009', 'ben@berrybros.com'),
        (12, 'SweetLeaf Honey', 'Sara Sweet','617-555-2010', 'sara@sweetleaf.com'),
        (13, 'Bun Run Delivery', 'Bobby Bun','617-555-2011', 'bobby@bunrun.com'),
        (14, 'PastryPro Suppliers', 'Paula Pastry','508-555-2012', 'paula@pastrypro.com'),
        (15, 'East End Eggs', 'Eddie Egg','413-555-2013', 'eddie@eastendeggs.com'),
        (16, 'Rolling Pin Supply Co.', 'Rachel Roller','781-555-2014', 'rachel@rollingpin.com'),
        (17, 'The Flour Collective', 'Frankie Flour','978-555-2015', 'frankie@flourcollective.com'),
        (18, 'Milky Way Creamery', 'Mila Milk','617-555-2016', 'mila@milkyway.com'),
        (19, 'Crumbs & Co.', 'Chloe Crumb','508-555-2017', 'chloe@crumbsandco.com'),
        (20, 'Tasty Trends', 'Trevor Trend','413-555-2018', 'trevor@tastytrends.com'),
        (21, 'Yeast Feast', 'Yara Yeast','781-555-2019', 'yara@yeastfeast.com'),
        (22, 'Nature’s Harvest', 'Nathan Nature','978-555-2020', 'nathan@naturesharvest.com'),
        (23, 'Ovenly Origins', 'Olivia Oven','617-555-2021', 'olivia@ovenlyorigins.com'),
        (24, 'Local Bounty Co.', 'Leo Local','508-555-2022', 'leo@localbounty.com'),
        (25, 'Maple & Co.', 'Mason Maple','413-555-2023', 'mason@mapleco.com'),
        (26, 'Sunrise Farms', 'Sophie Sunrise','781-555-2024', 'sophie@sunrisefarms.com'),
        (27, 'Harvest Hill Foods', 'Hector Hill','978-555-2025', 'hector@harvesthill.com'),
        (28, 'Pecan Partners', 'Penny Pecan','617-555-2026', 'penny@pecanpartners.com'),
        (29, 'The Spice Trail', 'Spencer Spice','508-555-2027', 'spencer@spicetrail.com'),
        (30, 'Cocoa Creations', 'Carmen Cocoa','413-555-2028', 'carmen@cocoacreations.com'),
        (31, 'Urban Oven Supply', 'Uriel Urban','781-555-2029', 'uriel@urbanoven.com'),
        (32, 'Lush Layers Ltd.', 'Lana Layers','978-555-2030', 'lana@lushlayers.com');

INSERT INTO SupplyOrder(ID, SupplierID, ManagerID, OrderTotal, OrderQuantity, DateOrdered, DeliveryDate)
    VALUES
        (1, 1, 1, 750.50, 20, '2025-03-15', '2025-03-20'),
        (2, 2, 2, 1250.00, 30, '2025-03-03', '2025-03-09'),
        (3, 3, 5, 890.75, 25, '2025-03-10', '2025-03-15'),
        (4, 4, 3, 1100.00, 28, '2025-02-27', '2025-03-03'),
        (5, 5, 4, 645.30, 18, '2025-03-05', '2025-03-10'),
        (6, 6, 6, 1375.00, 35, '2025-03-01', '2025-03-07'),
        (7, 7, 7, 495.90, 12, '2025-03-08', '2025-03-12'),
        (8, 8, 8, 720.00, 20, '2025-03-10', '2025-03-15'),
        (9, 9, 9, 999.99, 24, '2025-03-14', '2025-03-18'),
        (10, 10, 10, 850.00, 22, '2025-03-06', '2025-03-11'),
        (11, 11, 11, 1125.45, 29, '2025-03-12', '2025-03-17'),
        (12, 12, 12, 600.00, 15, '2025-03-04', '2025-03-08'),
        (13, 13, 13, 1320.10, 33, '2025-03-07', '2025-03-13'),
        (14, 14, 14, 780.00, 20, '2025-03-09', '2025-03-14'),
        (15, 15, 15, 1055.00, 27, '2025-03-11', '2025-03-16'),
        (16, 16, 16, 925.75, 23, '2025-03-02', '2025-03-06'),
        (17, 17, 17, 1349.50, 31, '2025-03-15', '2025-03-20'),
        (18, 18, 18, 570.25, 14, '2025-03-03', '2025-03-07'),
        (19, 19, 19, 875.00, 21, '2025-03-13', '2025-03-18'),
        (20, 20, 20, 1199.99, 30, '2025-03-05', '2025-03-10'),
        (21, 21, 21, 665.00, 17, '2025-03-06', '2025-03-11'),
        (22, 22, 22, 1400.00, 34, '2025-03-10', '2025-03-15'),
        (23, 23, 23, 999.95, 25, '2025-03-07', '2025-03-12'),
        (24, 24, 24, 1230.60, 29, '2025-03-08', '2025-03-13'),
        (25, 25, 25, 835.75, 19, '2025-03-04', '2025-03-09'),
        (26, 26, 26, 1075.25, 26, '2025-03-12', '2025-03-17'),
        (27, 27, 27, 950.00, 22, '2025-03-13', '2025-03-18'),
        (28, 28, 28, 715.15, 18, '2025-03-14', '2025-03-19'),
        (29, 29, 29, 1190.90, 30, '2025-03-11', '2025-03-16'),
        (30, 30, 30, 680.00, 16, '2025-03-10', '2025-03-14'),
        (31, 31, 31, 945.65, 24, '2025-03-09', '2025-03-13'),
        (32, 32, 32, 1033.33, 27, '2025-03-06', '2025-03-11'),
        (33, 2, 33, 1205.00, 32, '2025-03-15', '2025-03-20'),
        (34, 5, 34, 999.45, 28, '2025-03-08', '2025-03-13'),
        (35, 8, 35, 885.75, 21, '2025-03-04', '2025-03-09');


INSERT INTO Ingredients(IngredientID, IngredientName, Inventory, Expiry, BurnRate, Price)
    VALUES
        (1, 'Espresso Beans', 5, 14, 1, 15.99),
        (2, 'Whole Milk', 10, 7, 5, 3.49),
        (3, 'Butter', 5, 14, 2, 2.99),
        (4, 'Flour', 10, 171, 4, 1.99),
        (5, 'Sugar', 10, 182, 3, 1.49),
        (6, 'Vanilla Syrup', 13, 30, 6, 4.99),
        (7, 'Chocolate Syrup', 18, 220, 8, 9.53),
        (8, 'Almond Milk', 8, 247, 7, 4.19),
        (9, 'Oat Milk', 9, 216, 2, 5.45),
        (10, 'Cinnamon Powder', 17, 128, 1, 6.99),
        (11, 'Honey', 11, 36, 8, 1.36),
        (12, 'Whipped Cream', 19, 41, 7, 15.45),
        (13, 'Caramel Syrup', 13, 152, 8, 15.44),
        (14, 'Cocoa Powder', 6, 160, 9, 2.96),
        (15, 'Nutmeg', 16, 144, 2, 6.24),
        (16, 'Ice Cream', 11, 196, 10, 3.99),
        (17, 'Matcha Powder', 19, 252, 10, 14.26),
        (18, 'Iced Coffee', 12, 96, 6, 3.88),
        (19, 'Coconut Milk', 16, 200, 4, 10.5),
        (20, 'Oats', 15, 365, 6, 3.99),
        (21, 'Coconut Flakes', 7, 180, 5, 4.79),
        (22, 'Peanut Butter', 6, 180, 4, 5.99),
        (23, 'Pecans', 4, 180, 3, 8.99),
        (24, 'Raisins', 18, 365, 5, 2.99),
        (25, 'Orange Zest', 10, 180, 4, 3.49),
        (26, 'Lemon Zest', 8, 180, 5, 3.79),
        (27, 'Cornstarch', 20, 720, 6, 1.49),
        (28, 'Maple Syrup', 5, 180, 7, 7.99),
        (29, 'Walnuts', 12, 180, 8, 6.99),
        (30, 'Fresh Strawberries', 10, 7, 4, 5.49),
        (31, 'Fresh Blueberries', 14, 7, 4, 6.29),
        (32, 'Fresh Raspberries', 8, 7, 4, 7.49),
        (33, 'Fresh Blackberries', 7, 7, 5, 7.99),
        (34, 'Cream Cheese', 12, 30, 6, 3.69),
        (35, 'Mascarpone', 10, 30, 6, 5.99);


INSERT INTO Materials(ID, Name, Price, BurnRate, Inventory)
     VALUES
        (1, 'Coffee Cups', 0.15, 50, 500),
        (2, 'Plastic Lids', 0.05, 50, 500),
        (3, 'Paper Napkins', 0.02, 100, 1000),
        (4, 'Plastic Forks', 0.10, 30, 300),
        (5, 'Straws', 0.03, 40, 400),
        (6, 'Takeout Bags', 0.20, 60, 650),
        (7, 'Paper Coffee Filters', 0.08, 25, 750),
        (8, 'Sugar Packets', 0.01, 150, 1200),
        (9, 'Stirrers', 0.02, 45, 500),
        (10, 'Baking Paper', 0.12, 80, 600),
        (11, 'Paper Cups (Cold)', 0.18, 55, 750),
        (12, 'Cinnamon Sticks', 0.22, 90, 350),
        (13, 'To-Go Containers', 0.25, 60, 500),
        (14, 'Plastic Wrap', 0.05, 70, 650),
        (15, 'Cling Film', 0.10, 85, 400),
        (16, 'Wax Paper', 0.14, 45, 300),
        (17, 'Cups with Handles', 0.20, 60, 450),
        (18, 'Foil Sheets', 0.07, 50, 500),
        (19, 'Cake Boxes', 0.50, 25, 100),
        (20, 'Napkin Holders', 0.15, 30, 200),
        (21, 'Baking Molds', 0.30, 40, 100),
        (22, 'Candy Cups', 0.08, 60, 750),
        (23, 'Pizza Boxes', 0.35, 35, 550),
        (24, 'Takeout Containers (Soup)', 0.30, 55, 600),
        (25, 'Ice Cream Cones', 0.07, 80, 500),
        (26, 'Tea Bags', 0.05, 120, 1000),
        (27, 'Salt Packets', 0.02, 50, 600),
        (28, 'Honey Jars', 0.15, 40, 500),
        (29, 'Pastry Boxes', 0.40, 35, 350),
        (30, 'Butter Paper', 0.10, 60, 450),
        (31, 'Strawberry Jam Packets', 0.12, 55, 300),
        (32, 'Caramel Cups', 0.18, 50, 200),
        (33, 'Lemon Slices', 0.09, 70, 400),
        (34, 'Parchment Paper', 0.05, 40, 700),
        (35, 'Cupcake Wrappers', 0.08, 75, 650);

INSERT INTO Equipment(ID, Name, Price, Lifespan)
     VALUES
        (1, 'Baking Tray', 30.99, 7),
        (2, 'Wire Whisk', 3.99, 4),
        (3, 'Mixing Bowl', 11.99, 6),
        (4, 'Electric Mixer', 399.99, 10),
        (5, 'Baking Tray', 30.99, 7),
        (6, 'Wire Whisk', 3.99, 4),
        (7, 'Mixing Bowl', 11.99, 6),
        (8, 'Electric Mixer', 399.99, 10),
        (9, 'Toaster', 89.99, 5),
        (10, 'Microwave', 99.99, 8),
        (11, 'Coffee Maker', 79.99, 6),
        (12, 'Griddle', 250.00, 5),
        (13, 'Dishwasher', 599.99, 10),
        (14, 'Ice Cream Machine', 450.00, 7),
        (15, 'Fridge', 899.99, 15),
        (16, 'Freezer', 599.99, 15),
        (17, 'Juicer', 169.99, 5),
        (18, 'Hot Water Dispenser', 150.00, 5),
        (19, 'Oven', 800.00, 12),
        (20, 'Steamer', 120.00, 7),
        (21, 'Panini Press', 129.99, 6),
        (22, 'Refrigerated Display Case', 550.00, 10),
        (23, 'Soda Fountain', 600.00, 8),
        (24, 'Popcorn Machine', 120.00, 4),
        (25, 'Waffle Iron', 100.00, 4),
        (26, 'Microwave Oven', 199.99, 6),
        (27, 'Cappuccino Maker', 299.99, 7),
        (28, 'Hot Plate', 69.99, 4),
        (29, 'Sous Vide Machine', 499.99, 8),
        (30, 'Charbroiler', 350.00, 10),
        (31, 'Pizza Oven', 750.00, 12),
        (32, 'Topping Dispenser', 150.00, 5),
        (33, 'Bread Slicer', 199.99, 7),
        (34, 'Popcorn Machine', 125.00, 6),
        (35, 'Salad Spinner', 40.00, 5);

INSERT INTO OrderQuantity(OrderID, IngredientID, MaterialsID, EquipmentID, IngredientQuantity, MaterialQuantity, EquipmentQuantity)
     VALUES
        (1, 1, NULL, NULL, 10, NULL, NULL),  -- 10 units of Espresso Beans for OrderID 1
        (1, 3, NULL, NULL, 8, NULL, NULL),   -- 8 units of Butter for OrderID 1
        ( 2, 2, NULL, NULL, 15, NULL, NULL),  -- 15 units of Whole Milk for OrderID 2
        (2, 4, NULL, NULL, 20, NULL, NULL),  -- 20 units of Flour for OrderID 2
        (1, NULL, 1, NULL, NULL, 200, NULL), -- 200 units of Coffee Cups for OrderID 1
        (1, NULL, 2, NULL, NULL, 150, NULL), -- 150 units of Plastic Lids for OrderID 1
        (2, NULL, 3, NULL, NULL, 300, NULL), -- 300 units of Paper Napkins for OrderID 2
        (2, NULL, 4, NULL, NULL, 100, NULL), -- 100 units of Plastic Forks for OrderID 2
        (1, NULL, NULL, 1, NULL, NULL, 5),   -- 5 units of Baking Tray for OrderID 1
        (1, NULL, NULL, 2, NULL, NULL, 3),  -- 3 units of Wire Whisk for OrderID 1
        (2, NULL, NULL, 3, NULL, NULL, 2),  -- 2 units of Mixing Bowl for OrderID 2
        (2, NULL, NULL, 4, NULL, NULL, 1), -- 1 unit of Electric Mixer for OrderID 2
        (3, 5, NULL, NULL, 30, NULL, NULL),  -- 30 units of Yeast for OrderID 3
        (3, 6, NULL, NULL, 10, NULL, NULL),  -- 10 units of Salt for OrderID 3
        (4, 7, NULL, NULL, 20, NULL, NULL),  -- 20 units of Vanilla Extract for OrderID 4
        (4, 8, NULL, NULL, 12, NULL, NULL),  -- 12 units of Eggs for OrderID 4
        (5, 9, NULL, NULL, 18, NULL, NULL),  -- 18 units of Milk for OrderID 5
        (5, 10, NULL, NULL, 8, NULL, NULL),  -- 8 units of Heavy Cream for OrderID 5
        (6, 11, NULL, NULL, 25, NULL, NULL), -- 25 units of Cocoa Powder for OrderID 6
        (6, 12, NULL, NULL, 15, NULL, NULL), -- 15 units of Honey for OrderID 6
        (7, 13, NULL, NULL, 30, NULL, NULL), -- 30 units of Chocolate Chips for OrderID 7
        (7, 14, NULL, NULL, 40, NULL, NULL), -- 40 units of Brown Sugar for OrderID 7
        (8, 15, NULL, NULL, 10, NULL, NULL), -- 10 units of Baking Soda for OrderID 8
        (8, 16, NULL, NULL, 5, NULL, NULL),  -- 5 units of Cinnamon for OrderID 8
        (9, 17, NULL, NULL, 12, NULL, NULL), -- 12 units of Nutmeg for OrderID 9
        (9, 18, NULL, NULL, 3, NULL, NULL),  -- 3 units of Almond Extract for OrderID 9
        (10, 19, NULL, NULL, 25, NULL, NULL),-- 25 units of Pumpkin Puree for OrderID 10
        (10, 20, NULL, NULL, 35, NULL, NULL),-- 35 units of Oats for OrderID 10
        (11, 21, NULL, NULL, 18, NULL, NULL),-- 18 units of Coconut Flakes for OrderID 11
        (11, 22, NULL, NULL, 20, NULL, NULL),-- 20 units of Peanut Butter for OrderID 11
        (12, 23, NULL, NULL, 12, NULL, NULL),-- 12 units of Pecans for OrderID 12
        (12, 24, NULL, NULL, 22, NULL, NULL),-- 22 units of Raisins for OrderID 12
        (13, 25, NULL, NULL, 15, NULL, NULL),-- 15 units of Orange Zest for OrderID 13
        (13, 26, NULL, NULL, 10, NULL, NULL),-- 10 units of Lemon Zest for OrderID 13
        (14, 27, NULL, NULL, 20, NULL, NULL),-- 20 units of Cornstarch for OrderID 14
        (14, 28, NULL, NULL, 30, NULL, NULL),-- 30 units of Maple Syrup for OrderID 14
        (15, 29, NULL, NULL, 25, NULL, NULL),-- 25 units of Walnuts for OrderID 15
        (15, 30, NULL, NULL, 40, NULL, NULL),-- 40 units of Fresh Strawberries for OrderID 15
        (16, 31, NULL, NULL, 28, NULL, NULL),-- 28 units of Fresh Blueberries for OrderID 16
        (16, 32, NULL, NULL, 35, NULL, NULL),-- 35 units of Fresh Raspberries for OrderID 16
        (17, 33, NULL, NULL, 45, NULL, NULL),-- 45 units of Fresh Blackberries for OrderID 17
        (17, 34, NULL, NULL, 20, NULL, NULL),-- 20 units of Cream Cheese for OrderID 17
        (18, 35, NULL, NULL, 12, NULL, NULL),-- 12 units of Mascarpone for OrderID 18
        (19, NULL, 5, NULL, NULL, 150, NULL), -- 150 units of Yeast for OrderID 19
        (19, NULL, 6, NULL, NULL, 100, NULL), -- 100 units of Salt for OrderID 19
        (20, NULL, 7, NULL, NULL, 200, NULL), -- 200 units of Vanilla Extract for OrderID 20
        (20, NULL, 8, NULL, NULL, 80, NULL),  -- 80 units of Eggs for OrderID 20
        (21, NULL, 9, NULL, NULL, 120, NULL), -- 120 units of Milk for OrderID 21
        (21, NULL, 10, NULL, NULL, 60, NULL), -- 60 units of Heavy Cream for OrderID 21
        (22, NULL, 11, NULL, NULL, 250, NULL),-- 250 units of Cocoa Powder for OrderID 22
        (22, NULL, 12, NULL, NULL, 130, NULL),-- 130 units of Honey for OrderID 22
        (23, NULL, 13, NULL, NULL, 220, NULL),-- 220 units of Chocolate Chips for OrderID 23
        (23, NULL, 14, NULL, NULL, 260, NULL),-- 260 units of Brown Sugar for OrderID 23
        (24, NULL, 15, NULL, NULL, 180, NULL),-- 180 units of Baking Soda for OrderID 24
        (24, NULL, 16, NULL, NULL, 150, NULL),-- 150 units of Cinnamon for OrderID 24
        (25, NULL, 17, NULL, NULL, 190, NULL),-- 190 units of Nutmeg for OrderID 25
        (25, NULL, 18, NULL, NULL, 180, NULL),-- 180 units of Almond Extract for OrderID 25
        (26, NULL, 19, NULL, NULL, 220, NULL),-- 220 units of Pumpkin Puree for OrderID 26
        (26, NULL, 20, NULL, NULL, 250, NULL),-- 250 units of Oats for OrderID 26
        (27, NULL, 21, NULL, NULL, 180, NULL),-- 180 units of Coconut Flakes for OrderID 27
        (27, NULL, 22, NULL, NULL, 240, NULL),-- 240 units of Peanut Butter for OrderID 27
        (28, NULL, 23, NULL, NULL, 190, NULL),-- 190 units of Pecans for OrderID 28
        (28, NULL, 24, NULL, NULL, 220, NULL),-- 220 units of Raisins for OrderID 28
        (29, NULL, 25, NULL, NULL, 260, NULL),-- 260 units of Orange Zest for OrderID 29
        (29, NULL, 26, NULL, NULL, 230, NULL),-- 230 units of Lemon Zest for OrderID 29
        (30, NULL, 27, NULL, NULL, 240, NULL),-- 240 units of Cornstarch for OrderID 30
        (30, NULL, 28, NULL, NULL, 250, NULL),-- 250 units of Maple Syrup for OrderID 30
        (31, NULL, 29, NULL, NULL, 300, NULL); -- 300 units of Walnuts for Order

INSERT INTO Employee(ID, FirstName, Position, Wage, HoursWorked, ManagerID, LastName)
     VALUES
            (1, 'Connor', 'Cashier', 15, 20, 1, 'Singh'),
            (2, 'Pearl', 'Baker', 25, 40,1,  'Thepnakorn' ),
            (3, 'James', 'Baker', 26, 42, 1, 'Harris'),
            (4, 'Maya', 'Cashier', 16, 18, 4, 'Nguyen'),
            (5, 'Aiden', 'Waitstaff', 16, 38, 2, 'Smith'),
            (6, 'Sophia', 'Cashier', 30, 45, 6, 'Brown'),
            (7, 'Ella', 'Waitstaff', 12, 30, 2, 'Wilson'),
            (8, 'Liam', 'Cashier', 14, 22, 1, 'Taylor'),
            (9, 'Ethan', 'Baker', 27, 40, 5, 'Moore'),
            (10, 'Isabella', 'Cook', 21, 35, 3, 'Miller'),
            (11, 'Luna', 'Cook', 32, 50, 8, 'Davis'),
            (12, 'Jack', 'Waitstaff', 13, 28, 2, 'Martinez'),
            (13, 'Lucas', 'Cashier', 15, 24, 1, 'Garcia'),
            (14, 'Amelia', 'Baker', 25, 38, 6, 'Rodriguez'),
            (15, 'Mason', 'Cook', 19, 40, 2, 'Lopez'),
            (16, 'Harper', 'Waitstaff', 14, 26, 2, 'Gonzalez'),
            (17, 'Oliver', 'Baker', 28, 42, 6, 'Hernandez'),
            (18, 'Charlotte', 'Cashier', 16, 21, 1, 'Perez'),
            (19, 'Ella', 'Cook', 22, 39, 2, 'Murphy'),
            (20, 'Mia', 'Barista', 13, 23, 2, 'Roberts'),
            (21, 'Benjamin', 'Baker', 26, 41, 1, 'Evans'),
            (22, 'Scarlett', 'Cashier', 14, 19, 1, 'James'),
            (23, 'Henry', 'Cook', 21, 36, 2, 'Jackson'),
            (24, 'Grace', 'Manager', 34, 48, 7, 'White'),
            (25, 'Zoe', 'Barista', 12, 29, 2, 'Clark'),
            (26, 'Samuel', 'Cashier', 15, 20, 1, 'Lewis'),
            (27, 'Harold', 'Baker', 24, 41, 1, 'Young'),
            (28, 'Victoria', 'Cook', 23, 37, 2, 'Allen'),
            (29, 'Lucas', 'Baker', 31, 44, 3, 'King'),
            (30, 'Lily', 'Barista', 13, 22, 2, 'Scott'),
            (31, 'Daniel', 'Barista', 16, 23, 1, 'Adams'),
            (32, 'Emma', 'Baker', 29, 43, 1, 'Baker'),
            (33, 'Noah', 'Cook', 20, 38, 2, 'Nelson'),
            (34, 'Elijah', 'Baker', 33, 47, 4, 'Carter'),
            (35, 'Avery', 'Barista', 14, 25, 2, 'Mitchell');

INSERT INTO Costs(CostID, Type, PaymentDate, PaymentAmount, ManagerID, SupplyOrderID)
     VALUES(1, 'Labor', '2025-03-24', 1500.00, 1, NULL),
            (2, 'Supplies', '2025-03-15', 750.50, 2, 1),
            (3, 'Labor', '2025-03-25', 1600.00, 1, NULL),
            (4, 'Supplies', '2025-03-17', 850.75, 3, 2),
            (5, 'Labor', '2025-03-18', 1200.00, 2, NULL),
            (6, 'Supplies', '2025-03-20', 300.40, 4, 3),
            (7, 'Labor', '2025-03-22', 1300.00, 2, NULL),
            (8, 'Supplies', '2025-03-19', 400.25, 5, 4),
            (9, 'Labor', '2025-03-28', 1400.50, 3, NULL),
            (10, 'Supplies', '2025-03-22', 500.00, 1, 5),
            (11, 'Labor', '2025-03-23', 1100.00, 4, NULL),
            (12, 'Supplies', '2025-03-25', 700.60, 6, 6),
            (13, 'Labor', '2025-03-26', 1150.00, 5, NULL),
            (14, 'Supplies', '2025-03-24', 600.20, 7, 7),
            (15, 'Labor', '2025-03-29', 1350.00, 6, NULL),
            (16, 'Supplies', '2025-03-27', 350.90, 8, 8),
            (17, 'Labor', '2025-03-30', 1250.00, 7, NULL),
            (18, 'Supplies', '2025-03-29', 450.35, 9, 9),
            (19, 'Labor', '2025-03-31', 1500.50, 8, NULL),
            (20, 'Supplies', '2025-03-30', 550.80, 10, 10),
            (21, 'Labor', '2025-04-01', 1255.00, 9, NULL),
            (22, 'Supplies', '2025-04-02', 300.75, 11, 11),
            (23, 'Labor', '2025-04-02', 1155.25, 10, NULL),
            (24, 'Supplies', '2025-04-03', 350.50, 12, 12),
            (25, 'Labor', '2025-04-04', 1400.00, 11, NULL),
            (26, 'Supplies', '2025-04-05', 470.60, 13, 13),
            (27, 'Labor', '2025-04-06', 1300.50, 12, NULL),
            (28, 'Supplies', '2025-04-07', 420.45, 14, 14),
            (29, 'Labor', '2025-04-08', 1200.75, 13, NULL),
            (30, 'Supplies', '2025-04-09', 600.90, 15, 15),
            (31, 'Labor', '2025-04-10', 1300.00, 14, NULL),
            (32, 'Supplies', '2025-04-11', 330.65, 16, 16),
            (33, 'Labor', '2025-04-12', 1350.50, 15, NULL),
            (34, 'Utilities', '2025-04-13', 200.00, 17, NULL), -- Utility cost
            (35, 'Labor', '2025-04-14', 1450.00, 16, NULL);

INSERT INTO Sales(SalesID, Date, TotalSales)
     VALUES
        (1, '2025-04-01', 350.75),
        (2, '2025-03-31', 420.50),
        (3, '2025-03-30', 380.00),
        (4, '2025-03-29', 395.25),
        (5, '2025-03-28', 430.10),
        (6, '2025-03-27', 410.80),
        (7, '2025-03-26', 370.60),
        (8, '2025-03-25', 390.50),
        (9, '2025-03-24', 415.40),
        (10, '2025-03-23', 440.75),
        (11, '2025-03-22', 385.60),
        (12, '2025-03-21', 380.30),
        (13, '2025-03-20', 425.90),
        (14, '2025-03-19', 395.00),
        (15, '2025-03-18', 405.40),
        (16, '2025-03-17', 425.60),
        (17, '2025-03-16', 410.20),
        (18, '2025-03-15', 430.80),
        (19, '2025-03-14', 375.50),
        (20, '2025-03-13', 390.25),
        (21, '2025-03-12', 395.75),
        (22, '2025-03-11', 415.00),
        (23, '2025-03-10', 420.60),
        (24, '2025-03-09', 380.90),
        (25, '2025-03-08', 385.10),
        (26, '2025-03-07', 400.60),
        (27, '2025-03-06', 430.50),
        (28, '2025-03-05', 410.90),
        (29, '2025-03-04', 390.10),
        (30, '2025-03-03', 400.80);

INSERT INTO TransactionDetails(SalesID, MenuItemID, MenuItemQuantity, Date)
VALUES (1, 1, 3, '2025-04-01 10:00:00'),
       (2, 2, 2, '2025-04-01 10:00:00'),
       (3, 3, 4, '2025-03-31 10:00:00'),
       (4, 4, 1, '2025-03-30 10:30:00'),
        (5, 8, 2, '2025-03-29 11:00:00'),
        (6, 9, 3, '2025-03-28 11:30:00'),
        (7, 1, 5, '2025-03-27 12:00:00'),
        (8, 2, 4, '2025-03-26 12:30:00'),
        (9, 3, 6, '2025-03-25 13:00:00'),
        (10, 4, 2, '2025-03-24 13:30:00'),
        (11, 8, 3, '2025-03-23 14:00:00'),
        (12, 9, 1, '2025-03-22 14:30:00'),
        (13, 1, 4, '2025-03-21 15:00:00'),
        (14, 2, 5, '2025-03-20 15:30:00'),
        (15, 3, 2, '2025-03-19 16:00:00'),
        (16, 4, 3, '2025-03-18 16:30:00'),
        (17, 8, 4, '2025-03-17 17:00:00'),
        (18, 9, 2, '2025-03-16 17:30:00'),
        (19, 1, 3, '2025-03-15 18:00:00'),
        (20, 2, 1, '2025-03-14 18:30:00'),
        (21, 3, 5, '2025-03-13 19:00:00'),
        (22, 4, 2, '2025-03-12 19:30:00'),
        (23, 8, 4, '2025-03-11 20:00:00'),
        (24, 9, 3, '2025-03-10 20:30:00'),
        (25, 1, 6, '2025-03-09 21:00:00'),
        (26, 2, 2, '2025-03-08 21:30:00'),
        (27, 3, 4, '2025-03-07 22:00:00'),
        (28, 4, 3, '2025-03-06 22:30:00'),
        (29, 8, 5, '2025-03-05 23:00:00'),
        (30, 9, 2, '2025-03-04 23:30:00'),
        (31, 1, 2, '2025-03-03 10:00:00'),
        (32, 2, 3, '2025-03-02 10:30:00'),
        (33, 3, 1, '2025-03-01 11:00:00'),
        (34, 4, 4, '2025-02-28 11:30:00'),
        (35, 8, 3, '2025-02-27 12:00:00'),
        (36, 9, 5, '2025-02-26 12:30:00'),
        (37, 1, 6, '2025-02-25 13:00:00'),
        (38, 2, 4, '2025-02-24 13:30:00'),
        (39, 3, 5, '2025-02-23 14:00:00'),
        (40, 4, 2, '2025-02-22 14:30:00'),
        (41, 8, 4, '2025-02-21 15:00:00'),
        (42, 9, 2, '2025-02-20 15:30:00'),
        (43, 1, 3, '2025-02-19 16:00:00'),
        (44, 2, 5, '2025-02-18 16:30:00'),
        (45, 3, 2, '2025-02-17 17:00:00'),
        (46, 4, 1, '2025-02-16 17:30:00'),
        (47, 8, 6, '2025-02-15 18:00:00'),
        (48, 9, 4, '2025-02-14 18:30:00'),
        (49, 1, 5, '2025-02-13 19:00:00'),
        (50, 2, 3, '2025-02-12 19:30:00'),
        (51, 3, 1, '2025-02-11 20:00:00'),
        (52, 4, 4, '2025-02-10 20:30:00'),
        (53, 8, 3, '2025-02-09 21:00:00'),
        (54, 9, 5, '2025-02-08 21:30:00'),
        (55, 1, 6, '2025-02-07 22:00:00'),
        (56, 2, 4, '2025-02-06 22:30:00'),
        (57, 3, 2, '2025-02-05 23:00:00'),
        (58, 4, 1, '2025-02-04 23:30:00'),
        (59, 8, 5, '2025-02-03 10:00:00'),
        (60, 9, 3, '2025-02-02 10:30:00'),
        (61, 1, 4, '2025-02-01 11:00:00'),
        (62, 2, 2, '2025-01-31 11:30:00'),
        (63, 3, 5, '2025-01-30 12:00:00'),
        (64, 4, 2, '2025-01-29 12:30:00'),
        (65, 8, 3, '2025-01-28 13:00:00'),
        (66, 9, 4, '2025-01-27 13:30:00'),
        (67, 1, 5, '2025-01-26 14:00:00'),
        (68, 2, 6, '2025-01-25 14:30:00'),
        (69, 3, 4, '2025-01-24 15:00:00'),
        (70, 4, 1, '2025-01-23 15:30:00'),
        (71, 8, 5, '2025-01-22 16:00:00'),
        (72, 9, 3, '2025-01-21 16:30:00'),
        (73, 1, 6, '2025-01-20 17:00:00'),
        (74, 2, 4, '2025-01-19 17:30:00'),
        (75, 3, 2, '2025-01-18 18:00:00'),
        (76, 4, 3, '2025-01-17 18:30:00'),
        (77, 8, 6, '2025-01-16 19:00:00'),
        (78, 9, 5, '2025-01-15 19:30:00'),
        (79, 1, 2, '2025-01-14 20:00:00'),
        (80, 2, 1, '2025-01-13 20:30:00'),
        (81, 3, 4, '2025-01-12 21:00:00'),
        (82, 4, 2, '2025-01-11 21:30:00'),
        (83, 8, 3, '2025-01-10 22:00:00'),
        (84, 9, 1, '2025-01-09 22:30:00'),
        (85, 1, 5, '2025-01-08 23:00:00'),
        (86, 2, 6, '2025-01-07 23:30:00'),
        (87, 3, 3, '2025-01-06 10:00:00'),
        (88, 4, 4, '2025-01-05 10:30:00'),
        (89, 8, 2, '2025-01-04 11:00:00'),
        (90, 9, 5, '2025-01-03 11:30:00'),
        (91, 1, 3, '2025-01-02 12:00:00'),
        (92, 2, 5, '2025-01-01 12:30:00'),
        (93, 3, 2, '2024-12-31 13:00:00'),
        (94, 4, 6, '2024-12-30 13:30:00'),
        (95, 8, 3, '2024-12-29 14:00:00'),
        (96, 9, 4, '2024-12-28 14:30:00'),
        (97, 1, 5, '2024-12-27 15:00:00'),
        (98, 2, 2, '2024-12-26 15:30:00'),
        (99, 3, 3, '2024-12-25 16:00:00'),
        (100, 4, 1, '2024-12-24 16:30:00'),
        (101, 8, 6, '2024-12-23 17:00:00'),
        (102, 9, 5, '2024-12-22 17:30:00'),
        (103, 1, 4, '2024-12-21 18:00:00'),
        (104, 2, 3, '2024-12-20 18:30:00'),
        (105, 3, 2, '2024-12-19 19:00:00'),
        (106, 4, 5, '2024-12-18 19:30:00'),
        (107, 8, 3, '2024-12-17 20:00:00'),
        (108, 9, 4, '2024-12-16 20:30:00'),
        (109, 1, 6, '2024-12-15 21:00:00'),
        (110, 2, 4, '2024-12-14 21:30:00'),
        (111, 3, 2, '2024-12-13 22:00:00'),
        (112, 4, 5, '2024-12-12 22:30:00'),
        (113, 8, 1, '2024-12-11 23:00:00'),
        (114, 9, 4, '2024-12-10 23:30:00'),
        (115, 1, 2, '2024-12-09 10:00:00'),
        (116, 2, 5, '2024-12-08 10:30:00'),
        (117, 3, 3, '2024-12-07 11:00:00'),
        (118, 4, 1, '2024-12-06 11:30:00'),
        (119, 8, 4, '2024-12-05 12:00:00'),
        (120, 9, 2, '2024-12-04 12:30:00'),
        (121, 1, 6, '2024-12-03 13:00:00'),
        (122, 2, 1, '2024-12-02 13:30:00'),
        (123, 3, 5, '2024-12-01 14:00:00'),
        (124, 4, 2, '2024-11-30 14:30:00'),
        (125, 8, 3, '2024-11-29 15:00:00');







