import string

if __name__=="__main__":
    CampusFile=open("airports100.csv")
    outfile=open("AIRLINES-build-airports100.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Airports100(CITY, AIRPORTCODE, AIRPORTNAME, COUNTRY, COUNTRYABBREV) VALUES (%s, %s, %s,%s,%s);\n" % (campuses[0],campuses[1],campuses[2],campuses[3],campuses[4].strip()))
