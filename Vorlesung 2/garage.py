import json
class Vehicle:
    def __init__(self, brand_in: str, color_in: str, number_of_seats_in: int, engine_in: dict, weight_in: float):
        # initialize the attributes
        self.brand = brand_in
        self.color = color_in
        self.number_of_seats = number_of_seats_in
        self.engine = engine_in
        self.weight = weight_in

    def display_vehicle_characteristics(self):
        # display the attributes
        print("-----------------")
        print("Brand: ", self.brand)
        print("Color: ", self.color)
        print("Number of Seats: ", self.number_of_seats)
        print("Cylinders: ", self.engine["cylinder"])
        print("Max Speed: ", self.engine["max_speed"])
        print("Weight: ", self.weight)

    """Getter and setter methods for the attributes"""
    def update_color(self, color_in):
        self.color = color_in
        return None

    def update_brand(self, brand_in):
        self.brand = brand_in
        return None

class Garage:
    def __init__(self, capacity_in: int, alarm_in: bool, location_in: str, fleet_in: list[Vehicle]):
        if capacity_in < len(fleet_in):
            # add vehicles until the capacity is reached
            self.capacity = capacity_in
            self.fleet = fleet_in[:capacity_in]
            print(f"The fleet is larger than the capacity of the garage. The fleet is reduced to the capacity of {self.capacity}")
            print("The vehicles that are not in the garage are:")
            for vehicle in fleet_in[capacity_in:]:
                vehicle.display_vehicle_characteristics()
        else:
            self.fleet = fleet_in
        self.capacity = capacity_in
        self.alarm = alarm_in
        self.location = location_in

    def display_garage_characteristics(self):
        print("-----------------")
        print(f"Displaying characteristics of {self.location} garage")
        print("")
        print("Capacity: ", self.capacity)
        print("Alarm: ", self.alarm)
        print("Location: ", self.location)
        print("Fleet: ", self.fleet)
        print("")

    def display_fleet_characteristics(self):
        print(f"Displaying vehicles in the fleet of {self.location} garage")
        for vehicle in self.fleet:
            vehicle.display_vehicle_characteristics()


# create a list of vehicles

file = open("vehicle_data.json", "r")
vehicle_data = json.load(file)
file.close()

fleet = []
for element in vehicle_data:
    fleet.append(Vehicle(element["vehicle_brand"], element["color"], element["seats"], element["engine"], element["weight"]))

print(fleet)

# create a garage
garage = Garage(12, True, "Berlin", fleet)
garage.display_garage_characteristics()

# display the fleet
garage.display_fleet_characteristics()

