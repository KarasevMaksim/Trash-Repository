# Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
# Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
# Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).

# Пример:
# Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
# Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
# Различных сочетаний три, поэтому C(3, 2) = 3.

# Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать.
# Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать пять.

# Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
# C(n, k) = C(n - 1, k) + C(n - 1, k - 1).

# Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

# Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
# Ваша программа должна вывести единственное число: C(n, k).


def c(n, k):
    if n < k:
        return 0
    elif k == 0:
        return 1
    return c(n-1, k) + c(n-1, k-1)

# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     print(c(n, k))

# Обход вложенного массива ====================================================


mass = [1, [2, [3, 4], 5, [6, 7], 8], 9, [
    10, [11, ['Senko', 'Holo'], 12], 13, [14, 15], 16], 17]


def rec_search1(mass) -> None:
    for i in mass:
        if not isinstance(i, list):
            print(i)
        else:
            rec_search1(i)


def rec_search2(mass) -> None:
    if mass:
        if not isinstance(mass[0], list):
            print(mass[0])
        else:
            rec_search2(mass[0])
        rec_search2(mass[1:])


def rec_search3(mass) -> str:
    if mass:
        if isinstance(mass[0], list):
            return rec_search3(mass[0]) + ', ' + rec_search3(mass[1:])
        else:
            return str(mass[0]) + ', ' + rec_search3(mass[1:])
    else:
        return ''
    
string = 'SenkoSun'

def reverse_name(name: str) -> str:
    if name:
        return name[-1] + reverse_name(name[:len(name) -1])
    return ''

def my_pow(num, n):
    if not n == 0:
        return num * my_pow(num, n-1)
    return 1


if __name__ == '__main__':
    print(my_pow(5, 3))
