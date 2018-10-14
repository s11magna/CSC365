import string

if __name__=="__main__":
    CampusFile=open("flights.csv")
    outfile=open("AIRLINES-build-flights.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Flights(AIRLINE,FLIGHTNO, SOURCEAIRPORT, DESAIRPORT) VALUES (%s, %s, %s,%s);\n" % (campuses[0],campuses[1],campuses[2],campuses[3].strip()))
