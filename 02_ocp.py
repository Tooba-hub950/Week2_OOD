"""
02 — Open/Closed Principle (OCP)
=================================
"Software entities should be open for extension but closed for modification."

Domain: Ride-Hailing App
"""
from abc import ABC, abstractmethod
# ❌ BAD: The if/elif chain
# Every time we add a new ride type (e.g. Electric, Luxury), we must EDIT this class.
class BadFareCalculator:
    def calculate(self, distance: float, ride_type:str) -> float:
        base = 2.0
        if ride_type == "Standard":
            return base + (distance * 1.5)
        elif ride_type == "Premiun":
            return base + (distance * 2.5) + 5.0
        elif ride_type == "Pool":
            return base + (distance * 1.0)
        else:
            raise ValueError(f"UnKnown ride type:{ride_type}")
        
 # ✅ GOOD: Polymorphism
# We create an Abstract Base Class (ABC). 
# Adding a new ride type means adding a NEW file/class, not editing existing code. 

class BaseFare(ABC):
    @abstractmethod
    def calculate(self, distance: float) -> float:
        pass

class StandardFare(BaseFare):  
    def calculate(self, distance: float) -> float:
        return 2.0 + (distance * 1.5)
    
class PremiumFare(BaseFare):
    def calculate(self, distance:float) -> float:
        return 2.0 + (distance * 2.5) + 5.0
    
class PoolFare(BaseFare):
    def calculate(self, distance: float) -> float:
        return 2.0 + (distance * 1.0)
    
 # the new type! we did not touch the original calculator or standard fares.
class ElectricFare(BaseFare):
    def calculate(self, distance:float):
        return 2.0 + (distance * 1.8) # slightly more than standard
    
    
class GodFareCalculator:
    def process_fare(self, distance: float, fare_strategy : BaseFare) -> float:
        # this cide never changess, no matter hoe many fare typeswe invent!
        return fare_strategy.calculate(distance)
    
if __name__ == " __main__":
    print("---BAD DESIGN---")
    bad = BadFareCalculator()
    print(f"Standard 10km: ${bad.calculate(10,'Standard'):.2f}")
    print(f"Premium 10km: ${bad.calculate(10, 'Premium'):.2f}")
    
    print(f"\n----GOOD DESIGN----")
    good = GodFareCalculator()
    print(f"Standard 10km: ${good.process_fare(10, StandardFare()):.2f}")
    print(f"Premium  10km: ${good.process_fare(10, PremiumFare()):.2f}")
    
    # adding the new type is seemless
    print(f"Electric 10km: ${good.process_fare(10, ElectricFare()):.2f}")                          
    