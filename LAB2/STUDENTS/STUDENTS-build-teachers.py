import string

if __name__=="__main__":
    CampusFile=open("teachers.csv")
    outfile=open("STUDENTS-build-teachers.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO teachers(LASTNAME, FIRSTNAME, CLASSROOM) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))
