import string

if __name__=="__main__":
    CampusFile=open("grapes.csv")
    outfile=open("WINE-build-grapes.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Grapes(ID, GRAPE, COLOR) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))
