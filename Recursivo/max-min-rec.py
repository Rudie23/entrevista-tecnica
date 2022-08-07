def max_min(lst):
    """
    Calculate the maximum and minimum of a list
    :param lst: list
    :return: tuple:(max,min)
    """
    n = len(lst)
    if n == 0:
        raise ValueError('Empty List')
    max_value = min_value = lst[-1]  # Acessa o último valor da lista

    def max_min_rec(cursor):
        """
        t(n) = 1 + t(n-1)
        t(n) = 1 + 1 + t(n-2)
        t(n) = 1 + 1 + 1 + t(n-3)
        t(n) = n + 1 => O(n)

        m(m) = 1 + m(n-1) => O(n)
        :param cursor:
        :return:
        """

        nonlocal max_value, min_value
        # Primeira condição de parada
        if cursor < 0:
            return max_value, min_value
        # Segunda condição de parada
        current = lst[cursor]
        if current > max_value:
            max_value = current
        if current < min_value:
            min_value = current
        return max_min_rec(cursor - 1)

    return max_min_rec(n - 1)


print(max_min([1, 2, 3, 6, 7]))
print(max_min(list(range(50))))
print(max_min([]))
