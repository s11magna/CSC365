import string

if __name__=="__main__":
    CampusFile=open("airlines.csv")
    outfile=open("AIRLINES-build-airlines.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Airlines(ID, AIRLINE, ABBREVIATION, COUNTRY) VALUES (%s, %s, %s,%s);\n" % (campuses[0],campuses[1],campuses[2],campuses[3].strip()))
