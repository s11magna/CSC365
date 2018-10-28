-- Samuel Magana


-- Keep the table documenting campus enrollment by discipline for the
-- The following enrollements
-- Engineering Majors (9) Cal Poly SLO(20) and Cal Poly P(14)
-- LB(9) with enrollments > 200 
-- All enrollments in CIS(7) for schools > 500

DELETE FROM disEnroll 
    WHERE !((DISCIPLINE = 9) AND ((CAMPUS = 20) OR (CAMPUS = 14))) AND
            !((CAMPUS = 9) AND (GRADUATE > 200)) AND
            !((DISCIPLINE = 7) AND (UNDERGRADUATE > 500));

-- Display the remaining contents of the discipline enrollments table

SELECT *
FROM disEnroll
ORDER BY CAMPUS,DISCIPLINE;

-- Keeping in the documenting CSU fees only rh info that matches all the conoditons
-- Fee is greater then 2500
-- The Year is either 2002 or one of 2004 to 2006
-- Campus is either Cal Poly SLO or Cal Poly Pomona, SJSU

DELETE FROM CSUFees
    WHERE !(CAMPUSFEE > 2500 AND 
            ((YEAR = 2002) OR (YEAR BETWEEN 2004 AND 2006)) AND 
            ((CAMPUS = 19) OR (CAMPUS = 20) OR (CAMPUS = 14)));

-- Show Remaining Contents
SELECT *
FROM CSUFees
ORDER BY CAMPUS, YEAR;