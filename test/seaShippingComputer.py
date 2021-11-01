from shippingCalculator import ShippingCalculator 
from countryCharges import CountryCharges

class SeaShippingCalculator (ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self,custNm, custContact)
    def computeCharges(self):
        baseCharge = super().computeBaseCharge()
        
        customCharges = super().computeCustomCharges()

        packagingCharge = self.computeSeaPackagingCharge()

        seaFreightCharges = self.computeSeaFreightCharges()

        return baseCharge + packagingCharge + customCharges + seaFreightCharges

    def computeSeaPackagingCharge(self):
        return super().getSize()*super().getWeight()

    def computeSeaFreightCharges(self):
        return (super().getSize()*0.75) + (super().getWeight()*0.75) + 100
