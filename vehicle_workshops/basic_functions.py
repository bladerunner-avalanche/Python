def average_of_list(list_of_numbers: list) -> float:
    """Returns the average of a list of numbers.
    :rtype: object
    """
    return sum(list_of_numbers) / len(list_of_numbers)


def print_section_head(section_name: str) -> None:
    """Prints the name of a section."""
    print("--------------------")
    print(section_name.upper())
    print("--------------------")


