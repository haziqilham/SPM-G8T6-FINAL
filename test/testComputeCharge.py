import unittest
from airShippingCalculator import AirShippingCalculator
from countryCharges import CountryCharges
from landShippingCalculator import LandShippingCalculator
from seaShippingComputer import SeaShippingCalculator

from unittest import mock

class TestComputeCharge(unittest.TestCase):
    def setUp(self):
        self.air = AirShippingCalculator('AirMarcus', 91144231)
        self.air.setSizeWeight(10,10)
        self.air.setFromToCountry("SG","USA")

        self.air2 = AirShippingCalculator('Air2Marcus', 12345678)
        self.air2.setSizeWeight(10, 10)
        self.air2.setFromToCountry("USA", "CHINA")
        
        self.land = LandShippingCalculator('LandMarcus', 91144232)
        self.land.setSizeWeight(10, 10)
        self.land.setFromToCountry("SG", "INDIA")

        self.land2 = LandShippingCalculator('Land2Marcus', 91144632)
        self.land2.setSizeWeight(10, 10)
        self.land2.setFromToCountry("CHINA", "SG")

        self.sea = SeaShippingCalculator('SeaMarcus', 91144229)
        self.sea.setSizeWeight(10, 10)
        self.sea.setFromToCountry("SG", "CHINA")

        self.sea2 = SeaShippingCalculator('Sea2Marcus', 91144429)
        self.sea2.setSizeWeight(10, 10)
        self.sea2.setFromToCountry("CHINA", "USA")

        self.cc = CountryCharges()

    def tearDown(self):
        self.air = None
        self.air2 = None
        self.land = None
        self.land2 = None
        self.sea = None
        self.sea2 = None
        self.cc = None

    def testBaseCharge(self):
        self.assertEquals(self.cc.getBaseCharge("SG", "USA"),100)

    def testCustomCharges(self):
        self.assertEquals(self.cc.getCustomCharges("USA"), 100)

    def testWeight(self):
        self.assertEquals(self.air.getWeight(), 10)

    def testSize(self):
        self.assertEquals(self.air.getSize(), 10)

    def testAirComputeCharge(self):
        #Formula: Base Shipping Charge + Customs Charges + Package Charges + Air Freight Charges

        #Working: 100 + 100 + 100 + (10*3 + 10*4) = 370
        self.assertEquals(self.air.computeCharges(), 370)
        #Working: 140 + 25 + 100 + (10*3 + 10*4) = 335
        self.assertEquals(self.air2.computeCharges(), 335)

    def testLandComputeCharge(self):
        #Formula: Base Shipping Charge + Customs Charges + Package Charges + Land Freight Charges
        #Note: Land has 10% discount on Package Charges

        #Working: 50 + 20 + 90 + (10*0.25 + 10*0.75 + 10) = 180
        self.assertEquals(self.land.computeCharges(), 180)
        #Working: 40 + 50 + 90 + (10*0.25 + 10*0.75 + 10) = 200
        self.assertEquals(self.land2.computeCharges(), 200)

    def testSeaComputeCharge(self):
        #Formula: Base Shipping Charge + Customs Charges + Package Charges + Sea Freight Charges
        
        #Working: 40 + 25 + 100 + (10*0.75 + 10*0.75 + 100) = 280
        self.assertEquals(self.sea.computeCharges(), 280)
        #Working: 140 + 100 + 100 + (10*0.75 + 10*0.75 + 100) = 455
        self.assertEquals(self.sea2.computeCharges(), 455)





    
