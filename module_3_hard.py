data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    the_sum = 0
    for unit in args:
        if isinstance(unit, list):
            the_sum += calculate_structure_sum(*unit)
        elif isinstance(unit, set):
            the_sum += calculate_structure_sum(*unit)
        elif isinstance(unit, tuple):
            the_sum += calculate_structure_sum(*unit)
        elif isinstance(unit, int):
            the_sum += unit
        elif isinstance(unit, str):
            the_sum += len(unit)
        elif isinstance(unit, dict):
            for key, value in unit.items():
                the_sum += len(key)
                the_sum += calculate_structure_sum(value)
    return the_sum


result = calculate_structure_sum(data_structure)
print(result)
