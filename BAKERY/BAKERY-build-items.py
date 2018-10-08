import string

if __name__=="__main__":
    CampusFile=open("items.csv")
    outfile=open("BAKERY-build-items.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Items(RECIEPT, ORDINAL, ITEM) VALUES (%s, %s, %s);\n" % (campuses[0],campuses[1],campuses[2].strip()))
