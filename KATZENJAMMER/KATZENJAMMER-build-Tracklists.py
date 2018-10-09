import string

if __name__=="__main__":
    CampusFile=open("Tracklists.csv")
    outfile=open("KATZENJAMMER-build-Tracklists.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Tracklists(ALBUMID, POSITION, SONGID) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))
