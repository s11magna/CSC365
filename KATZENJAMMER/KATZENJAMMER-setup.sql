CREATE TABLE Songs(
    SONGID INT NOT NULL,
    TITLE VARCHAR(100),
    PRIMARY KEY(SONGID)
);
CREATE TABLE Albums(
    AID INT NOT NULL,
    TITLE VARCHAR(100),
    YEAR INT NOT NULL,
    LABEL VARCHAR(100),
    PRIMARY KEY(AID)
);
CREATE TABLE Tracklists(
    ALBUMID INT NOT NULL,
    POSITION INT NOT NULL,
    SONGID INT NOT NULL,
    FOREIGN KEY (ALBUMID) REFERENCES Albums(AID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (SONGID) REFERENCES Songs(SONGID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE Band(
    ID INT NOT NULL,
    FIRSTNAME VARCHAR(100),
    LASTNAME VARCHAR(100),
    PRIMARY  KEY(ID)
);
CREATE TABLE Vocals(
  SONGID INT NOT NULL,
  BANDMATE INT NOT NULL,
  TYPE VARCHAR(100),
  FOREIGN KEY (SONGID) REFERENCES Songs(SONGID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
  FOREIGN KEY (BANDMATE) REFERENCES Band(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE Instruments(
    SONGID INT NOT NULL,
    BANDMATEID INT NOT NULL,
    INSTRUMENT VARCHAR(100),
    FOREIGN KEY (SONGID) REFERENCES Songs(SONGID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (BANDMATEID) REFERENCES Band(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE Performance(
    SONGID INT NOT NULL,
    BANDMATE INT NOT NULL,
    STAGEPOSITION VARCHAR(100),
    FOREIGN KEY (SONGID) REFERENCES Songs(SONGID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (BANDMATE) REFERENCES Band(ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


