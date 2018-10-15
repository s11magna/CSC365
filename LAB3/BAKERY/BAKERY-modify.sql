-- Samuel Magana (smagan01@calpoly.edu)

-- Remove  from table containing listing of pasteries about everything execpt cakes
DELETE FROM Goods 
    WHERE (FOOD != 'Cake');

-- Increase the prices of the Choclate and Opera Cake by %20
UPDATE Goods SET PRICE =  PRICE + (.20 * PRICE) WHERE (FLAVOR = 'Chocolate' OR FLAVOR = 'Opera');

-- Reduce the prices of Lemon Cake and Napoleon Cake
UPDATE Goods SET PRICE =  PRICE - 2 WHERE (FLAVOR = 'Lemon'AND FOOD = 'Cake') OR (FLAVOR = 'Napoleon' AND FOOD = 'Cake');

-- Reduce the Price of all other cakes by %10
UPDATE Goods SET PRICE =  PRICE - (PRICE *.10) WHERE (FLAVOR != 'Lemon' OR FLAVOR != 'Napoleon' OR FLAVOR != 'Chocolate' OR FLAVOR != 'Opera');
-- contents of the table
SELECT *
FROM Goods
ORDER BY ID;

