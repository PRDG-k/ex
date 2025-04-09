from abc import ABC, abstractmethod
class Converter:
    __conversion_ratio = 1.60934

    @classmethod
    def convert(cls, miles):
        """Convert miles to kilometers."""
        return miles * cls.__conversion_ratio
    
    @staticmethod
    def miles_to_km(miles):
        """Convert miles to kilometers."""
        return miles * Converter.__conversion_ratio

class MilesToKilometers(Converter):
    def __init__(self, miles):
        self.miles = miles

    def convert(self):
        """Convert miles to kilometers."""
        return super().convert(self.miles)
    
miles_to_km = MilesToKilometers(10)
print(miles_to_km.convert())