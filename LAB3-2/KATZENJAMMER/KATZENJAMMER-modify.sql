-- Samuel Magana
-- smagan01@calpoly.edu
--lab3-2

-- In the instruments table update
-- all occurances of balalika and guitar
UPDATE Instruments 
    SET INSTRUMENT = 'awesome bass balalaika'
    WHERE INSTRUMENT =  'bass balalaika';

UPDATE Instruments 
    SET INSTRUMENT = 'acoustic guitar'
    WHERE INSTRUMENT =  'guitar';


-- Keep in the Instrument Table only info about
-- acoustic guitar players

DELETE FROM Instruments
    WHERE !((INSTRUMENT = 'acoustic guitar') AND
           (BANDMATEID = 4));

-- show contents
SELECT * 
FROM Instruments
ORDER BY SONGID,BANDMATEID;

-- Add a New column to describe the  albums released 
ALTER TABLE Albums
ADD COLUMN TRACKS INT;


-- Update each record in the albums table to show the correct number
-- of tracks
UPDATE Albums 
    SET TRACKS = 13
    WHERE AID = 1;

UPDATE Albums
    SET TRACKS = 12
    WHERE AID = 2;

UPDATE Albums
    SET TRACKS = 19
    WHERE AID = 3;

UPDATE Albums
    SET TRACKS = 11
    WHERE AID = 4;

-- show contents of the table

SELECT *
FROM Albums
ORDER BY YEAR;

