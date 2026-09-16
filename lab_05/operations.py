from functools import reduce


def filter_objects(objects, predicate):

    return list(filter(predicate, objects))


def transform_objects(objects, operation):

    return list(map(operation, objects))


def sort_objects(objects, key_function, reverse=False):

    return sorted(objects, key=key_function, reverse=reverse)


def get_computer_names(computers):

    return transform_objects(computers, lambda comp: comp.name)


def filter_by_min_ram(computers, min_ram):

    return filter_objects(computers, lambda comp: comp.ram >= min_ram)


def sort_by_price(computers, reverse=False):

    return sort_objects(computers, lambda comp: comp.price, reverse=reverse)


def find_most_expensive(computers):

    if not computers:
        return None
    return max(computers, key=lambda comp: comp.price)


def check_ram_availability(computers, target_ram):

    return any(comp.ram == target_ram for comp in computers)


def check_all_positive_prices(computers):

    return all(comp.price > 0 for comp in computers)


def get_cheap_computer_models(computers, threshold):

    return [comp.name for comp in computers if comp.price < threshold]


def calculate_total_cost(computers):

    if not computers:
        return 0.0
    return reduce(lambda acc, comp: acc + comp.price, computers, 0.0)