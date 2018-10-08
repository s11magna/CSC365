import string

if __name__=="__main__":
    CampusFile=open("list.csv")
    outfile=open("STUDENTS-build-list.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO List(LASTNAME, FIRSTNAME, GRADE, CLASSROOM) VALUES (%s, %s, %s,%s);\n" % (campuses[0],campuses[1],campuses[2],campuses[3].strip()))
