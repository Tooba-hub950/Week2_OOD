"""
03 — Liskov Substitution Principle (LSP)
=========================================
"Subtypes must be substitutable for their base type without breaking the program."

Domain: Ride-Hailing App
"""

# ❌ BAD: Breaking the contract
class Driver:
    def accept_ride(self, distance: float) -> bool:
        print(f"Driver accepted a {distance}km ride")

class BadPremiumDriver(Driver):
    def accept_ride(self, distance: float) -> bool:
            #A premium Driver refuses short trips.
            #This reak the LSP because the parent class never refused trips based on distance.
            if distance < 5.0:
                raise NotImplementedError("Premium drivers don't take short trips!")
            print(f"Premium driver accepted a { distance}km ride")
            return True
        
# If a system iterates through a list of generic Drivers, the BadPremiumDriver wiill crash it.
def dispatch_ride(drivers: list[Driver], distance: float):
    for d in drivers:
        try:
            if d.accept_ride(distance):
                print("Ride dipatched successfully!")
                return
        except NotImplementedError as e:
            print(f" CRASH! {e}")
            
 # ✅ GOOD: Honouring the contract
class GoodPremiumDriver(Driver):
    def accept_ride(self, distance: float) -> bool:
     # We can add behaviour (like charging a premium fee), but we MUST NOT 
     # break the expected input/output contract or raise unexpected errors.                      
     if distance < 5.0:
         print("Premium driver accepted a short trip, but added a 5$ surcharge.")
     else:
         print(f"Premium driver accpeted a {distance}km ride")
     return True 
  
def dispatch_good_ride(drivers: list[Driver], distance:float):
    for d in drivers:
        if d.accept_ride(distance):
            print("Ride dispatched successfully!")
            return


if __name__ == "__main__":
    print("-----Bad DESIGN-----")
    bad_fleet = [Driver(), BadPremiumDriver()]  
    # A short 3km trip crashes the system when it hits the BadPremiumDriver
    dispatch_ride(bad_fleet, 3.0)
    
    
    print("\n----GOOD DESIGN----")
    good_fleet = [Driver(), GoodPremiumDriver()]
    # A short 3km trip works perfectly, even with the GoodPremiumDriver
    dispatch_good_ride(good_fleet, 3.0)       
