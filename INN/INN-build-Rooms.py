import string

if __name__=="__main__":
    CampusFile=open("Rooms.csv")
    outfile=open("INN-build-Rooms.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Rooms(ROOMID,ROOMNAME,BEDS,BEDTYPE,MAXOCCUPANCY,BASEPRICE,DECOR) VALUES (%s, %s, %s, %s, %s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2],campuses[3],campuses[4],campuses[5],campuses[6].strip()))
