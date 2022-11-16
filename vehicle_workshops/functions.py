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
