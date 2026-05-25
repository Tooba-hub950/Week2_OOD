"""
04 — Interface Segregation Principle (ISP)
===========================================
"No client should be forced to depend on methods it does not use."

Domain: Ride-Hailing App
"""

from abc import ABC, abstractmethod

# ❌ BAD: The Fat Interface
# This interface forces ALL vehicles to implement methods they might not need.

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def charge_battery(self):
        pass
    
    @abstractmethod
    def refuel(self):
        pass
  
# A standaard petrol; car is forced to implement a dummy ' charge_battery' method.
class BadPetrolCar(IVehicle):
    def start_engine(self):
        print("Vroom!")
    
    def charge_battery(self):
        raise NotImplementedError("I don't have a battert to charge!")
    
    def refuel(self):
        print("Filling up with unleaded petrol.")
        
         
# ✅ GOOD: Segregated Interfaces
# We split the fat interface into lean, focused interfaces.      
class IEngineVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class IElectricVehicle(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def charge_battery(self):
        pass
            
# Now a petrol car only implements what it needs.
class GoodPetrolCar(IEngineVehicle):
    def start_engine(self):
        print("Vroom!")

    def refuel(self):
        print("Filling up with unleaded petrol.")

# And an electric car only implements what it needs.
class GoodElectricCar(IElectricVehicle):
    def turn_on(self):
        print("Silent hum...")

    def charge_battery(self):
        print("Plugging into supercharger.")


if __name__ == "__main__":
    print("--- BAD DESIGN ---")
    bad = BadPetrolCar()
    bad.start_engine()
    try:
        bad.charge_battery()
    except NotImplementedError as e:
        print(f"ISP Violation: {e}")

    print("\n--- GOOD DESIGN ---")
    petrol = GoodPetrolCar()
    petrol.start_engine()
    petrol.refuel()

    ev = GoodElectricCar()
    ev.turn_on()
    ev.charge_battery()
