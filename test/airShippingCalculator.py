from shippingCalculator import ShippingCalculator
from countryCharges import CountryCharges


class AirShippingCalculator (ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self, custNm, custContact)

    def computeCharges(self):
        baseCharge = super().computeBaseCharge()

        customCharges = super().computeCustomCharges()

        packagingCharge = self.computeAirPackagingCharge()

        airFreightCharges = self.computeAirFreightCharges()

        return baseCharge + packagingCharge + customCharges + airFreightCharges

    def computeAirPackagingCharge(self):
        return super().getSize()*super().getWeight()

    def computeAirFreightCharges(self):
        return (super().getSize()*3) + (super().getWeight()*4)
