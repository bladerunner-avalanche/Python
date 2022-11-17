class Vehicle:
    def __init__(self, color_in: str, brand_in: str, engine_in: str, max_speed_in: int,
                 number_of_seats_in: int, fuel_type_in: str, fuel_consumption_in: float):
        # initialize the attributes
        self.color = color_in
        self.brand = brand_in
        self.engine = engine_in
        self.max_speed = max_speed_in
        self.number_of_seats = number_of_seats_in
        self.fuel_type = fuel_type_in
        self.fuel_consumption = fuel_consumption_in

    def display_vehicle_characteristics(self):
        # display the attributes
        print("-----------------")
        print("Brand: ", self.brand)
        print("Color: ", self.color)
        print("Engine: ", self.engine)
        print("Max Speed: ", self.max_speed)
        print("Number of Seats: ", self.number_of_seats)
        print("Fuel Type: ", self.fuel_type)
        print("Fuel Consumption: ", self.fuel_consumption)
        return None

    """Getter and setter methods for the attributes"""
    def update_color(self, color_in):
        self.color = color_in
        return None

    def update_brand(self, brand_in):
        self.brand = brand_in
        return None

    def update_engine(self, engine_in):
        self.engine = engine_in
        return None

    def update_max_speed(self, max_speed_in):
        self.max_speed = max_speed_in
        return None

    def update_number_of_seats(self, number_of_seats_in):
        self.number_of_seats = number_of_seats_in
        return None

    def update_fuel_type(self, fuel_type_in):
        self.fuel_type = fuel_type_in
        return None

    def update_fuel_consumption(self, fuel_consumption_in):
        self.fuel_consumption = fuel_consumption_in
        return None


class Garage:
    def __init__(self, capacity_in: int, alarm_in: bool, location_in: str, fleet_in: list[Vehicle]):
        self.capacity = capacity_in
        self.alarm = alarm_in
        self.location = location_in
        self.fleet = fleet_in

    def display_garage_characteristics(self):
        print("-----------------")
        print(f"Displaying characteristics of {self.location} garage")
        print("")
        print("Capacity: ", self.capacity)
        print("Alarm: ", self.alarm)
        print("Location: ", self.location)
        print("Fleet: ", self.fleet)
        return None


    def display_fleet_characteristics(self):
        print(f"Displaying vehicles in the fleet of {self.location} garage")
        for vehicle in self.fleet:
            vehicle.display_vehicle_characteristics()
        return None


mercedes_benz = Vehicle("black", "Mercedes Benz", "4-Cylinder", 250, 5, "Diesel", 6.5)
ford = Vehicle("red", "Ford", "6-Cylinder", 200, 5, "Gasoline", 8.5)
honda = Vehicle("blue", "Honda", "8-Cylinder", 300, 5, "Gasoline", 10.5)

garage = Garage(3, True, "Berlin", [mercedes_benz, ford, honda])
garage.display_garage_characteristics()
garage.display_fleet_characteristics()