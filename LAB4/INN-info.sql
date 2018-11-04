-- Samuel Magana (smagan01@calpoly.edu)
-- LAB4 INN

-- Q1 Room modern decor two beds base price < 160
SELECT rm.RoomName, res.Code
FROM rooms rm INNER JOIN reservations res ON res.Room = rm.RoomId
WHERE rm.decor = 'modern' AND BasePrice < 160 AND Beds = 2
ORDER BY res.Code;

-- Q2 
SELECT res.LastName, res.CheckIn, res.CheckOut, res.Adults + res.Kids AS 'Total People', res.Rate
FROM rooms rm INNER JOIN reservations res ON res.Room = rm.RoomId
WHERE res.CheckIn LIKE '2010-08-%' AND res.Checkout LIKE '2010-08-%' AND rm.RoomName = 'Convoke and sanguine'
ORDER BY res.CheckIn, res.CheckOut;

-- Q3 
SELECT rm.RoomName, res.CheckIn ,res.Checkout
FROM rooms rm INNER JOIN reservations res ON res.Room = rm.RoomId
WHERE '2010-02-06' BETWEEN res.CheckIn AND res.Checkout
ORDER BY rm.RoomName;

-- Q4
SELECT res.Code,res.CheckIn,res.CheckOut, rm.RoomName, DATEDIFF(res.CheckOut,res.CheckIn)* res.Rate  as 'Total'
FROM rooms rm INNER JOIN reservations res ON res.Room = rm.RoomId
WHERE res.LastName = 'KNERIEN' AND res.FirstName = 'GRANT'
ORDER BY rm.RoomName;

-- Q5
SELECT rm.RoomName, res.Rate, rm.RoomName, DATEDIFF(res.CheckOut,res.CheckIn) AS 'Nights',DATEDIFF(res.CheckOut,res.CheckIn)* res.Rate  as 'Total'
FROM rooms rm INNER JOIN reservations res ON res.Room = rm.RoomId
WHERE res.CheckIn = '2010-12-31'
ORDER BY Nights DESC;

-- Q6
SELECT res.Code, res.FirstName, res.LastName, rm.RoomName, rm.RoomId, res.CheckIn, res.CheckOut
FROM rooms rm INNER JOIN reservations res ON res.Room = rm.RoomId
WHERE rm.BedType = 'Double' and res.Adults = 4
ORDER BY rm.RoomId;

