import string

if __name__=="__main__":
    degreesFile=open("degrees.csv")
    outfile=open("CSU-build-degrees.sql","w")
    degreesFile.readline()
    for degrees in degreesFile:
        degrees = degrees.split(",")
        outfile.write("INSERT INTO Degrees(YEAR, CAMPUS, DEGREES) VALUES (%d, %d, %d);\n" % (int(degrees[0]),int(degrees[1]),int(degrees[2].strip())))
