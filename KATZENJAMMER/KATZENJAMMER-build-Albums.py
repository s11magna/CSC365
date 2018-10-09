import string

if __name__=="__main__":
    CampusFile=open("Albums.csv")
    outfile=open("KATZENJAMMER-build-Albums.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Albums(AID, TITLE, YEAR, LABEL) VALUES (%s, %s, %s,%s);\n" % (campuses[0],campuses[1],campuses[2],campuses[3].strip()))
