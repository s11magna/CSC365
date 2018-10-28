import string

if __name__=="__main__":
    CampusFile=open("Vocals.csv")
    outfile=open("KATZENJAMMER-build-Vocals.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Vocals(SONGID, BANDMATE, TYPE) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))
