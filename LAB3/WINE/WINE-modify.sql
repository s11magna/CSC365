-- Samuel Magana (smagan01@calpoly.edu)

-- drop appellation name and the name of the wine
ALTER TABLE Wine 
    DROP FOREIGN KEY wine_ibfk_2;

ALTER TABLE Wine
    DROP APPELATION
    DROP NAME;

-- Keep in the table only the Syrahs with a score higher then 93
DELETE FROM Wine
	WHERE (GRAPE = 'Syrah' AND Score < 93); 

-- alter length of the atrribute storing
-- the winery name to be 15 char long
UPDATE Wine SET WINERY=SUBSTRING(WINERY, 1, 15);
	ALTER TABLE Wine MODIFY WINERY VARCHAR(15);

-- Add new column to table called Revenue
ALTER TABLE Wine 
    ADD REVENUE INT;

-- REVENUE FROM SELLING ALL CASES OF WINE
UPDATE Wine SET REVENUE = PRICE * (CASES/12);

-- OUTPUT LIST OF WINES
SELECT * FROM Wine
ORDER BY REVENUE;
