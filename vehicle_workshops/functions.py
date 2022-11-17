import basic_functions as bf


def get_avg_miles(data_set: list, vehicle_type: str = "") -> float:
    """Returns the average miles of a data set."""
    if vehicle_type:
        return bf.average_of_list([row["mileage"] for row in data_set if row["vehicle_type"] == vehicle_type])
    else:
        return bf.average_of_list([row["mileage"] for row in data_set])


def get_avg_cost(data_set: list, damage_type: str = "") -> float:
    """Returns the average costs of the repairs"""
    if damage_type:
        return bf.average_of_list([row["damage"]["cost"] for row in data_set if row["damage"]["type"] == damage_type])
    else:
        return bf.average_of_list([row["damage"]["cost"] for row in data_set])


def get_most_freq_damage_type(data_set: list) -> str:
    """Returns the most frequent damage type"""
    damage_type_count = get_damage_type_count(data_set)
    most_freq_damage_type = ""
    for damage_type in damage_type_count:
        if most_freq_damage_type == "" or damage_type_count[damage_type] > damage_type_count[most_freq_damage_type]:
            most_freq_damage_type = damage_type
    return most_freq_damage_type


def get_avg_cost_per_damage_type(data_set: list) -> dict:
    """Returns the average cost per damage type"""
    avg_cost_per_damage_type = {}
    for damage_type in get_damage_type_count(data_set):
        avg_cost_per_damage_type[damage_type] = get_avg_cost(data_set, damage_type)
    return avg_cost_per_damage_type


def get_vehicle_type_count(data_set: list) -> dict:
    """Returns the number of each vehicle type"""
    vehicle_type_count = {}
    for element in data_set:
        if element["vehicle_type"] in vehicle_type_count:
            vehicle_type_count[element["vehicle_type"]] += 1
        else:
            vehicle_type_count[element["vehicle_type"]] = 1
    return vehicle_type_count


def get_damage_type_count(data_set: list) -> dict:
    """Returns the number of each damage type"""
    damage_type_count = {}
    for row in data_set:
        if row["damage"]["type"] in damage_type_count:
            damage_type_count[row["damage"]["type"]] += 1
        else:
            damage_type_count[row["damage"]["type"]] = 1
    return damage_type_count


def count_types_in_list(data_set: list) -> dict:
    """Returns the number of each type in a list"""
    type_count = {}
    for element in data_set:
        if element in type_count:
            type_count[element] += 1
        else:
            type_count[element] = 1
    return type_count


"""
    
"""


def get_damage_cost_count(data_set: list) -> dict:
    """Returns the number of each damage cost"""
    damage_cost_count = {}
    for row in data_set:
        if row["damage"]["cost"] in damage_cost_count:
            damage_cost_count[row["damage"]["cost"]] += 1
        else:
            damage_cost_count[row["damage"]["cost"]] = 1
    return damage_cost_count


def get_most_frequent_damage_cost(data_set: list) -> float:
    """Returns the most frequent damage cost"""
    damage_cost_count = get_damage_cost_count(data_set)
    most_frequent_damage_cost = 0
    for damage_cost in damage_cost_count:
        if damage_cost_count[damage_cost] > damage_cost_count[most_frequent_damage_cost]:
            most_frequent_damage_cost = damage_cost
    return most_frequent_damage_cost

