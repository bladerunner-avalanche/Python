import basic_functions as bf


def add_key_to_dictionary(dictionary: dict, key, value) -> dict:
    x = dict(dictionary)
    x.update({key: value})
    return x


def check_key_presence(dictionary: dict, key) -> bool:
    """Function takes a dictionary and a key and checks if it already exists."""
    if key in dictionary:
        print(f"The key {key} already exists in the dictionary!")
        return True
    else:
        print(f"The key {key} is not in use!")
        return False

