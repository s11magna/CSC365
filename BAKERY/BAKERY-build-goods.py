import string

if __name__=="__main__":
    CampusFile=open("goods.csv")
    outfile=open("BAKERY-build-goods.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Goods(ID, FLAVOR, FOOD, PRICE) VALUES (%s, %s, %s,%s);\n" % (campuses[0],campuses[1],campuses[2],campuses[3].strip()))
