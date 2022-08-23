from random import shuffle


def max_min(lst):
    """
    Calculate the maximum and minimum of a list
    :param lst: list
    :return: tuple:(max,min)
    """
    n = len(lst)
    if n == 0:
        raise ValueError('Empty List')
    # Acessa o último valor da lista, o cursor está na última posição
    max_value = min_value = lst[-1]

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
        # Primeira condição de parada, significa que ja percorri todos os valores no meu vetor
        if cursor < 0:
            return max_value, min_value
        # Segunda condição de parada
        current = lst[cursor]
        if current > max_value:
            max_value = current
        if current < min_value:
            min_value = current
        # Estou chamando a função sempre diminuindo o valor em -1, para chamar o valor à esquerda, isto é uma
        # característica de uma função recursiva cuja chama a si mesma. A condição de parada foi estabelecida em
        # cima, if cursor < 0
        return max_min_rec(cursor - 1)

    return max_min_rec(n - 1)


print(max_min([1]))
print(max_min([1, 2]))
random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_min(random_list))
print(max_min([]))
