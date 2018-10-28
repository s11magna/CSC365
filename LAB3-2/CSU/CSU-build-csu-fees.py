import string

if __name__=="__main__":
    feesFile=open("csu-fees.csv")
    outfile=open("CSU-build-csu-fees.sql","w")
    feesFile.readline()
    for fees in feesFile:
        fees = fees.split(",")
        outfile.write("INSERT INTO CSUFees(CAMPUS, YEAR, CAMPUSFEE) VALUES (%d, %d, %d);\n" % (int(fees[0]),int(fees[1]),int(fees[2].strip())))
