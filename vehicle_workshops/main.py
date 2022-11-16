from workshop_data import data
import basic_functions as bf
import functions as f

bf.print_section_head("AVERAGE MILEAGE")
print("Average mileage of all vehicles:", f.get_avg_miles(data))
print("Average mileage of A-Class vehicles:", f.get_avg_miles(data, "A-Class"))
print("Average mileage of G-Class vehicles:", f.get_avg_miles(data, "G-Class"))
print("Average mileage of S-Class vehicles:", f.get_avg_miles(data, "S-Class"))

bf.print_section_head("AVERAGE COST")
print("Average cost of all repairs:", f.get_avg_cost(data))
print("Average cost of battery repairs:", f.get_avg_cost(data, "battery"))
print("Average cost of engine repairs:", f.get_avg_cost(data, "engine"))
print("Average cost of wheel repairs:", f.get_avg_cost(data, "wheel"))

bf.print_section_head("TYPE COUNT DEDICATED FUNCTIONS")
print("Number of each vehicle type:", f.get_vehicle_type_count(data))
print("Number of each damage type:", f.get_damage_type_count(data))

bf.print_section_head("TYPE COUNT GENERAL FUNCTION")
print("Number of each vehicle type:", f.count_types_in_list([row["vehicle_type"] for row in data]))
print("Number of each damage type:", f.count_types_in_list([row["damage"]["type"] for row in data]))






