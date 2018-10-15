import string

if __name__=="__main__":
    CampusFile=open("customers.csv")
    outfile=open("BAKERY-build-customers.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Customers(ID, LASTNAME, FIRSTNAME) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))
