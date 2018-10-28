import string

if __name__=="__main__":
	CampusFile=open("Campuses.csv") 
	outfile=open("CSU-build-Campuses.sql","w")  
	CampusFile.readline() 
	for campuses in CampusFile:
		campuses = campuses.split(",")
		outfile.write("INSERT INTO Campuses(ID, CAMPUS, LOCATION, COUNTY, YEAR) VALUES (%d, %s, %s, %s, %d);\n" % (int(campuses[0]),campuses[1],campuses[2],campuses[3],int(campuses[4].strip())))
