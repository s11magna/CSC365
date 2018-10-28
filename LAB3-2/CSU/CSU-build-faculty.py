import string

if __name__=="__main__":
    CampusFile1=open("faculty.csv")
    outfile=open("CSU-build-faculty.sql","w")
    CampusFile1.readline()
    for campuses in CampusFile1:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Faculty(CAMPUS, YEAR, FACULTY) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))