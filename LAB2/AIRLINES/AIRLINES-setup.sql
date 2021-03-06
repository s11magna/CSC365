CREATE TABLE Airlines(
    ID INT NOT NULL,
    AIRLINE VARCHAR(100),
    ABBREVIATION VARCHAR(100),
    COUNTRY VARCHAR(100),
    PRIMARY KEY(ID)
);
CREATE TABLE Airports100(
    CITY VARCHAR(100),
    AIRPORTCODE VARCHAR(100) NOT NULL,
    AIRPORTNAME VARCHAR(100),
    COUNTRY VARCHAR(100),
    COUNTRYABBREV VARCHAR(100),
    PRIMARY KEY(AIRPORTCODE)
);
CREATE TABLE Flights(
    AIRLINE INT NOT NULL,
    FLIGHTNO INT,
    SOURCEAIRPORT VARCHAR(100) NOT NULL,
    DESAIRPORT VARCHAR(100) NOT NULL,
    FOREIGN KEY (AIRLINE) REFERENCES Airlines(ID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (SOURCEAIRPORT) REFERENCES Airports100(AIRPORTCODE)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (DESAIRPORT) REFERENCES Airports100(AIRPORTCODE)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);