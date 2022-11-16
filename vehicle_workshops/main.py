from workshop_data import data
import functions as f
print("--------------------")
print("")
print("Mileage statistics:")
print("")
print("Average mileage of all vehicles:", f.get_avg_miles(data))
print("Average mileage of A-Class vehicles:", f.get_avg_miles(data, "A-Class"))
print("Average mileage of G-Class vehicles:", f.get_avg_miles(data, "G-Class"))
print("Average mileage of S-Class vehicles:", f.get_avg_miles(data, "S-Class"))
print("--------------------")
print("")
print("Cost statistics:")
print("")
print("Average cost of all repairs:", f.get_avg_cost(data))
print("Average cost of battery repairs:", f.get_avg_cost(data, "battery"))
print("Average cost of engine repairs:", f.get_avg_cost(data, "engine"))
print("Average cost of wheel repairs:", f.get_avg_cost(data, "wheel"))
print("--------------------")
print("")
print("Vehicle type statistics:")
print("")
print("Number of each vehicle type:", f.get_vehicle_type_count(data))
print("Number of each damage type:", f.get_damage_type_count(data))
print("--------------------")





