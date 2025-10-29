class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "BMW: 240 km/h"
    def transmission(self):
        return "Automatic Transmission"
class Ferrari:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "Ferrari: 330 km/h"
    def transmission(self):
        return "Dual-clutch Transmission"
def vehicle_details(vehicle):
    print(f"Fuel Type: {vehicle.fuel_type()}")
    print(f"Max Speed: {vehicle.max_speed()}")
    print(f"Transmission: {vehicle.transmission()}")
    print("-" * 30)
bmw_car = BMW()
ferrari_car = Ferrari()
vehicle_details(bmw_car)
vehicle_details(ferrari_car)