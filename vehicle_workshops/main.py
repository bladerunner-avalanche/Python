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
print("Number of each vehicle type:", f.count_vehicle_types(data))
print("Number of each damage type:", f.count_damage_types(data))

bf.print_section_head("TYPE COUNT GENERAL FUNCTION")
print("Number of each vehicle type:", f.count_types_in_list([row["vehicle_type"] for row in data]))
print("Number of each damage type:", f.count_types_in_list([row["damage"]["type"] for row in data]))

bf.print_section_head("AVG COST PER DAMAGE TYPE")
avg_cost = f.get_avg_cost_per_damage_type(data)
for element in avg_cost:
    print("Average cost of", element, "repairs:", avg_cost[element])

bf.print_section_head("MOST FREQUENT DAMAGE TYPE")
print(f.select_most_frequent_damage_type(data))

print(f"Mileage average if user enters 'all': {f.avg_miles_with_kwargs(data_set=data, vehicle_type='all')}")
print(f"Mileage average if user enters 'A-Class': {f.avg_miles_with_kwargs(data_set=data, vehicle_type='A-Class')}")
print(f"Mileage average if user enters 'G-Class': {f.avg_miles_with_kwargs(data_set=data, vehicle_type='G-Class')}")
print(f"Mileage average if user enters 'S-Class': {f.avg_miles_with_kwargs(data_set=data, vehicle_type='S-Class')}")
print(f"Mileage average if user only enters the dataset: {f.avg_miles_with_kwargs(data_set=data)}")
print(f"Mileage average if user enters nothing: {f.avg_miles_with_kwargs()}")
#print(f.get_most_freq_damage_cost(data))