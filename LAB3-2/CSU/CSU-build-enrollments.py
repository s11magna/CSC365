import string

if __name__=="__main__":
    CampusFile=open("enrollments.csv")
    outfile=open("CSU-build-enrollments.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Enrollment(CAMPUS, YEAR, TOTALENROLLMENT_AY, FTE_AY) VALUES (%d, %d, %d, %d);\n" % (int(campuses[0]),int(campuses[1]),int(campuses[2]),int(campuses[3].strip())))

