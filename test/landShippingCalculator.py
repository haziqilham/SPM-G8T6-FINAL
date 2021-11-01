from shippingCalculator import ShippingCalculator
from countryCharges import CountryCharges


class LandShippingCalculator (ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self, custNm, custContact)

    def computeCharges(self):
        baseCharge = super().computeBaseCharge()

        customCharges = super().computeCustomCharges()

        packagingCharge = self.computeLandPackagingCharge()

        landFreightCharges = self.computeLandFreightCharges()

        return baseCharge + packagingCharge + customCharges + landFreightCharges

    def computeLandPackagingCharge(self):
        return (super().getSize()*super().getWeight())*0.9

    def computeLandFreightCharges(self):
        return (super().getSize()*0.25) + (super().getWeight()*0.75) + 10
