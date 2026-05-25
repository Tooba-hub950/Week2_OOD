"""
01 — Single Responsibility Principle (SRP)
===========================================
"A class should have only one reason to change."

Domain: Ride-Hailing App
"""
# ❌ BAD: The "God Class"
# This class handles matching, pricing, notifications, and database saving.
class Badrideservice:
    def process_ride(self, rider, driver, distance):
        #1. Matching logic
        print(f"Matching{rider}with {driver}....")
        
        #2. pricing logic
        fare = distance * 1.5 + 2.0
        print(f"calculated fare: ${fare:.2f}")
        
        #3 Notification logic
        print(f"sending SMS to {rider}: your driver{driver} is arriving.")
        
        #4. Database logic
        print(f"saving ride({rider}, {driver}, {fare} to database...)")

# ✅ GOOD: Split into focused classes
class RideMatcher:
    def match(self, rider, driver):
        print(f"[Matcher] Matching {rider} with {driver}..." )
        return{"rider": rider, "driver": driver}

class FareCalculator:
    def calculate(sself, distance):
        fare = distance * 1.5 + 2.0
        print(f"[FareCalc] calculated fare: ${fare:.2f}")
        return fare
    
class NotificationService:
    def send_sms(self, user, message):
        print(f"[SMS] sending to {user}: {message}")
        
class RideRepository:
    def save( self, ride_data):
        print(f"[DB] saving the ride data:{ride_data}")

# The cooridinator (Facade) that glues them togther
class RideCoordinator:
    def __init__(self):
        self.Matcher = RideMatcher()
        self.fare_calc = FareCalculator()
        self.notifier = NotificationService()
        self.repo = RideRepository()
        
    def process_ride(self, rider, driver, distance):
        ride = self.matcher.match(rider, driver)
        ride["fare"] = self.fare_calc.calculate(distance)
        
        self.notifier. send_sms(rider, f"your driver{driver} is arriving.")
        self.repo.save(ride)

if __name__ == "__main__":
    print("--- BAD DESIGN ---")
    bad = Badrideservice()
    bad.process_ride("Alice", "Bob", 10)
    
    print("\n--- GOOD DESIGN---")
    good = RideCoordinator()
    good.process_ride("Alice", "Bob", 10)                            
           
               
        