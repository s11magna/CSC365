import string

if __name__=="__main__":
    CampusFile=open("receipts.csv")
    outfile=open("BAKERY-build-receipts.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO " + "Receipts" + " (" +"RECIEPTNUMBER" + "," + "DATES" + "," + "CUSTOMERID" + ") VALUES (" + campuses[0] + "," + "STR_TO_DATE(" + campuses[1] + ", \"%d-%M-%Y\" )" + "," + campuses[2] + ");" + '\n')
