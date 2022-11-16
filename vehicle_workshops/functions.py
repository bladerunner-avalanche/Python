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
