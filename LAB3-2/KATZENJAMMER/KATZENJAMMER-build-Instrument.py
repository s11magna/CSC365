import string

if __name__=="__main__":
    CampusFile=open("Instruments.csv")
    outfile=open("KATZENJAMMER-build-Instruments.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Instruments(SONGID, BANDMATEID, INSTRUMENT) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))
