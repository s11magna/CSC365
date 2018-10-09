import string

if __name__=="__main__":
    CampusFile=open("Performance.csv")
    outfile=open("KATZENJAMMER-build-Performance.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Performance(SONGID, BANDMATE, STAGEPOSITION) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))
