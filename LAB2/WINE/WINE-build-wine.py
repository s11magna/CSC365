import string

if __name__=="__main__":
    CampusFile=open("wine.csv")
    outfile=open("WINE-build-wine.sql","w")
    CampusFile.readline()
    for campuses in CampusFile:
        campuses = campuses.split(",")
        outfile.write("INSERT INTO Wine(NO,GRAPE,WINERY,APPELATION,NAME,YEAR,PRICE,SCORE,CASES) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s);\n" % (campuses[0],campuses[1],campuses[2],campuses[3],campuses[5],campuses[6],campuses[7],campuses[8],campuses[9].strip()))
