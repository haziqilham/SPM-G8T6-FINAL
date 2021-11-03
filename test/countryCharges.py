class CountryCharges:

    def __init__(self):
        self.__countryMapping = ["SG", "USA", "INDIA", "CHINA"]
        #Row: SG, USA, INDIA, CHINA 
        #COL: SG, USA, INDIA, CHINA 
        self.__baseCharges = [[0,100,50, 40],[100, 0, 150, 140],[50, 150, 0, 30],[40, 140, 30,0]]
        self.__custom = [50, 100, 20, 25]
    
    def getBaseCharge(self,fr,to):
        i = self.__countryMapping.index(fr)
        j = self.__countryMapping.index(to)
        return self.__baseCharges[i][j]
        
    def getCustomCharges(self, toCty):
        return self.__custom[self.__countryMapping.index(toCty)]