from workshop_data import data
import functions as f

avg_miles = f.get_avg_miles(data, "A-Class")

print("The A-Class vehicles coming to our workshop are driven", avg_miles, "miles on average.")

avg_miles = f.get_avg_miles(data)

print("The vehicles coming to our workshop are driven", avg_miles, "miles on average.")

avg_cost = f.get_avg_cost(data)
print("The repairs cost", avg_cost, "USD on average.")
avg_cost = f.get_avg_cost(data, "battery")
print("avg cost for battery repairs is", avg_cost, "USD")

print(f.get_vehicle_type_count(data))
damage_count = f.get_damage_type_count(data)
print(max(damage_count, key=damage_count.get), "is the most common damage type.")



