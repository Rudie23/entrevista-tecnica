def max_min(lst):
    """
    Calculate the maximum and minimum of a list
    :param lst: list
    :return: tuple:(max,min)
    """
    n = len(lst)
    if n == 0:
        raise ValueError('Empty List')
    max_value = min_value = lst[0]

    for value in lst:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    return max_value, min_value


print(max_min(list(range(50))))
