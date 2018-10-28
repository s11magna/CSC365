import string

if __name__=="__main__":
    CampusFile=open("discipline-enrollments.csv")
    outfile=open("CSU-build-discipline-enrollments.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO disEnroll(CAMPUS, DISCIPLINE, YEAR, UNDERGRADUATE, GRADUATE) VALUES (%d, %d, %d, %d, %d);\n" % (int(campuses[0]),int(campuses[1]),int(campuses[2]),int(campuses[3]),int(campuses[4].strip())))
