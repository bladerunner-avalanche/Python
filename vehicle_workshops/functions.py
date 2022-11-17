import basic_functions as bf
import re


"""
    SECTION 1: Calculate the averages of the data set
"""


def avg_miles_with_kwargs(**kwargs) -> float:
    """Returns the average mileage of all vehicles inside a dataset"""
    if "data_set" not in kwargs:
        #   raise ValueError("No data set provided")
        return str("No data set provided")
    elif "vehicle_type" in kwargs and re.match(r"all", kwargs["vehicle_type"], re.IGNORECASE) or "vehicle_type" not in kwargs:
        return bf.average_of_list([row["mileage"] for row in kwargs["data_set"]])
    else:
        return bf.average_of_list([row["mileage"] for row in kwargs["data_set"] if row["vehicle_type"] == kwargs["vehicle_type"]])


def get_avg_miles(data_set: list, vehicle_type: str = "") -> float:
    """Returns the average mileage of all vehicles inside a dataset"""
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


def get_avg_cost_per_damage_type(data_set: list) -> dict:
    """Returns the average cost per damage type"""
    avg_cost_per_damage_type = {}
    for damage_type in count_damage_types(data_set):
        avg_cost_per_damage_type[damage_type] = get_avg_cost(data_set, damage_type)
    return avg_cost_per_damage_type


"""
    SECTION 2: Count the number of values inside a dataset
"""


def count_vehicle_types(data_set: list) -> dict:
    """Returns the number of each vehicle type"""
    vehicle_type_count = {}
    for element in data_set:
        if element["vehicle_type"] in vehicle_type_count:
            vehicle_type_count[element["vehicle_type"]] += 1
        else:
            vehicle_type_count[element["vehicle_type"]] = 1
    return vehicle_type_count


def count_damage_types(data_set: list) -> dict:
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
    SECTION 3: Get the maximum and minimum values of a dataset
"""


def select_most_frequent_damage_type(data_set: list) -> str:
    """Returns the most frequent damage type"""
    damage_type_count = count_damage_types(data_set)
    most_freq_damage_type = ""
    for damage_type in damage_type_count:
        if most_freq_damage_type == "" or damage_type_count[damage_type] > damage_type_count[most_freq_damage_type]:
            most_freq_damage_type = damage_type
    return most_freq_damage_type
