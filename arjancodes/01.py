import string
import random

class VehicleRegistry:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits,k=2))}-{''.join(random.choices(string.ascii_uppercase,k=2))}"


class Application:
    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()
        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a licence plate for the vehicle
        # using the first two characters of the vehicle id
        licence_plate = registry.generate_vehicle_license(vehicle_id)

        # compute the catalogue price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price. except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute payable tax
        payable_tax = tax_percentage * catalogue_price

        print("Registeration complete, Veheicle information")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"Licence plate: {licence_plate}")
        print(f"Payable Tax: {payable_tax}")


if __name__ == "__main__":
    app = Application()
    app.register_vehicle('BMW 5')