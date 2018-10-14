import string

if __name__=="__main__":
    CampusFile=open("Band.csv")
    outfile=open("KATZENJAMMER-build-Band.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Band(ID, FIRSTNAME, LASTNAME) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))
