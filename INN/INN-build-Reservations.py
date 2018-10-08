import string

if __name__=="__main__":
    CampusFile=open("Reservations.csv")
    outfile=open("INN-build-Reservations.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO " + "Reservations" + " (" +"CODE" + "," + "ROOM" + "," + "CHECKIN" + " ," + "CHECKOUT" + " ," + "RATE" +
        " ," + "LASTNAME" +" ," + "FIRSTNAME" + " ," + "ADULTS" + " ," + "KIDS" + 
        ") VALUES (" + campuses[0] + "," + campuses[1] + " ," + "STR_TO_DATE(" + campuses[2] + ", \"%d-%M-%Y\" )" +"," + "STR_TO_DATE(" + campuses[3] + ", \"%d-%M-%Y\" )" + " ," + campuses[4] + " ,"
        + campuses[5] + " ," + campuses[6] + " ,"+ campuses[7] + " ," + campuses[8] + ");" + '\n')
