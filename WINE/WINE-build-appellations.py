import string

if __name__=="__main__":
    CampusFile=open("appellations.csv")
    outfile=open("WINE-build-appellations.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Appelations(NO, APPELATION, COUNTY, STATE,AREA,ISAVA) VALUES (%s, %s, %s,%s,%s,%s);\n" % (campuses[0],campuses[1],campuses[2],campuses[3],campuses[4],campuses[5].strip()))
