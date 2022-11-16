from typing import List, Any
import csv

import csv

with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


def get_avg_miles(data_set: list) -> float:
    """Returns the average miles of a data set."""
    total_miles = 0
    for row in data_set:
        total_miles += float(row[2])
    return total_miles / len(data_set)


def get_make_count(make: str, data_set: list) -> int:
    """Returns the number of cars of a specific make."""
    count = 0
    for row in data_set:
        if row[1] == make:
            count += 1
    return count


print(f"The cars in this dataset have been driven for an average of {get_avg_miles(data)} miles.")
print(f"There are {get_make_count('Mazda', data)} Mazdas in the data set.")
print(f"There are {get_make_count('Ford', data)} Fords in the data set.")
print(f"There are {get_make_count('Subaru', data)} Subarus in the data set.")
print(f"There are {get_make_count('Toyota', data)} Toyotas in the data set.")






