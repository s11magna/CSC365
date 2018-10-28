import string

if __name__=="__main__":
    CampusFile=open("disciplines.csv")
    outfile=open("CSU-build-disciplines.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Disciplines(ID, NAME) VALUES (%d, %s);\n" % (int(campuses[0]),campuses[1].strip()))
