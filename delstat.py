

# Processes the delstat data from a USPS Adress Information System Products file

# input file
# use a commandline parameter in production version

delstat = r'C:\delstat\delstat.txt'

data = open(delstat, "rb")  # read input file as binary
data.read(309)


def copyrightRecord(inputstring):
    """Takes a 309-byte Copyright Record from a delstat file (first line in the file)
    Returns the month and year of the file version (CD release month) as a string [MM-YY]"""
    
    return inputstring[19:24]


def detailRecord(inputstring):
    """Takes a 309 byte Detail Record from a delstat file
    Returns a list of fields, with the index corresponding to the field number [1 to 63]
    Field [0] contains no information and should be ignored"""
    
    flist = [] # empty list
    
    flist.append(None)                      #0  append a null value for the index at 0
    flist.append(inputstring[0:1])          #1  Copyright Detail Code
    flist.append(inputstring[1:6])          #2  ZIP Code
    flist.append(inputstring[6:16])         #3  Update Key Number
    flist.append(inputstring[16:17])        #4  Action Code
    flist.append(inputstring[17:21])        #5  Carrier Route ID
    
    # Active Statistics Section
    # Business
    flist.append(int(inputstring[21:26]))   #6  Centralized Count
    flist.append(int(inputstring[26:31]))   #7  Curb Count
    flist.append(int(inputstring[31:36]))   #8  CBU Count
    flist.append(int(inputstring[36:41]))   #9  Other Count
    flist.append(int(inputstring[41:46]))   #10 Facility Box Count
    flist.append(int(inputstring[46:51]))   #11 Contract Box Count
    flist.append(int(inputstring[51:56]))   #12 Detached Box Count
    flist.append(int(inputstring[56:61]))   #13 NPU Count
    flist.append(int(inputstring[61:66]))   #14 Caller Service Box Count
    flist.append(int(inputstring[66:71]))   #15 Remittance Box Count
    flist.append(int(inputstring[71:76]))   #16 Contest Box Count
    flist.append(int(inputstring[76:81]))   #17 Other Box Count
    
    #Residential
    flist.append(int(inputstring[81:86]))   #18 Centralized Count
    flist.append(int(inputstring[86:91]))   #19 Curb Count
    flist.append(int(inputstring[91:96]))   #20 CBU Count
    flist.append(int(inputstring[96:101]))  #21 Other Count
    flist.append(int(inputstring[101:106])) #22 Facility Box Count
    flist.append(int(inputstring[106:111])) #23 Contract Box Count
    flist.append(int(inputstring[111:116])) #24 Detached Box Count
    flist.append(int(inputstring[116:121])) #25 NPU Count
    flist.append(int(inputstring[121:126])) #26 Caller Service Box Count
    flist.append(int(inputstring[126:131])) #27 Remittance Box Count
    flist.append(int(inputstring[131:136])) #28 Contest Box Count
    flist.append(int(inputstring[136:141])) #29 Other Box Count
    
    flist.append(int(inputstring[141:146])) #30 General Delivery Count
    
    # Possible Statistics Section
    # Business
    flist.append(int(inputstring[146:151])) #31 Centralized Count
    flist.append(int(inputstring[151:156])) #32 Curb Count
    flist.append(int(inputstring[156:161])) #33 CBU Count
    flist.append(int(inputstring[161:166])) #34 Other Count
    flist.append(int(inputstring[166:171])) #35 Facility Box Count
    flist.append(int(inputstring[171:176])) #36 Contract Box Count
    flist.append(int(inputstring[177:181])) #37 Detached Box Count
    flist.append(int(inputstring[181:186])) #38 NPU Count
    flist.append(int(inputstring[186:191])) #39 Caller Service Box Count
    flist.append(int(inputstring[191:196])) #40 Remittance Box Count
    flist.append(int(inputstring[196:201])) #41 Contest Box Count
    flist.append(int(inputstring[201:206])) #42 Other Box Count
    
    #Residential
    flist.append(int(inputstring[206:211])) #43 Centralized Count
    flist.append(int(inputstring[211:216])) #44 Curb Count
    flist.append(int(inputstring[219:221])) #45 CBU Count
    flist.append(int(inputstring[221:226])) #46 Other Count
    flist.append(int(inputstring[226:231])) #47 Facility Box Count
    flist.append(int(inputstring[231:236])) #48 Contract Box Count
    flist.append(int(inputstring[236:241])) #49 Detached Box Count
    flist.append(int(inputstring[241:246])) #50 NPU Count
    flist.append(int(inputstring[246:251])) #51 Caller Service Box Count
    flist.append(int(inputstring[251:256])) #52 Remittance Box Count
    flist.append(int(inputstring[256:261])) #53 Contest Box Count
    flist.append(int(inputstring[261:266])) #54 Other Box Count
    
    flist.append(int(inputstring[266:271])) #55 General Delivery Count    
    
    # Drop Business    
    flist.append(int(inputstring[271:276])) #56 Families Served Count
    
    # Active Business / Residential Mixed
    flist.append(int(inputstring[276:281])) #57 Count
    
    # Active Residential / Business Mixed
    flist.append(int(inputstring[281:286])) #58 Count
    
    flist.append(inputstring[286:292])      #59 Finance Number
    flist.append(inputstring[292:294])      #60 State Abbreviation
    flist.append(inputstring[294:297])      #61 County Code
    flist.append(inputstring[297:303])      #62 Municipality City State Key
    flist.append(inputstring[303:309])      #63 Preferred Last Line City State Key
    
    return flist
    

class ZipRecord:
    fieldList = [0] * 64  #empty list of 64 items to store the 63 fields
    
    def setfield(self, fieldnumber, value):
        self.fieldList[fieldnumber] = value
    
    def getfield(self, fieldnumber):
        return self.fieldlist[fieldnumber]


    
    
     
