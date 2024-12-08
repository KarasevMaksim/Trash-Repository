mass = [3, 0, 1, 5, 2, 9, 2, -2, 2, 1, 6]

# mass2 = list()
# while mass:
#     min_val = 0, mass[0]

#     for index, elem in enumerate(mass[1:], start=1):
#         if min_val[1] > elem:
#             min_val = index, elem
#     mass2.append(mass.pop(min_val[0]))


array = [-3, 2, 4]


def quick_merge_sort(array):
    if not array:
        return array
    elif len(array) == 1:
        return [array[0]]
    elif len(array) == 2:
        item1 = array[0]
        item2 = array[1]
        return [item1, item2] if item1 <= item2 else [item2, item1]
    else:
        array_midle = len(array) // 2
        arr1 = quick_merge_sort(array[:array_midle])
        arr2 = quick_merge_sort(array[array_midle:])
        count1 = 0
        count2 = 0
        res_mass = list()
        while count1 < len(arr1) and count2 < len(arr2):
            val1 = arr1[count1]
            val2 = arr2[count2]
            if val1 == val2:
                res_mass.append(val1)
                res_mass.append(val2)
                count1 += 1
                count2 += 1
            elif val1 < val2:
                res_mass.append(val1)
                count1 += 1
            else:
                res_mass.append(val2)
                count2 += 1
        res_mass += arr1[count1:] + arr2[count2:]
        return res_mass


def quick_sort_not_inplace(array):
    if not array or len(array) == 1:
        return array
    elif len(array) == 2:
        elem1 = array[0]
        elem2 = array[1]
        return array if elem1 <= elem2 else [elem2, elem1]
    else:
        L = len(array) // 2
        mid_elem = array[L]
        mid_array = list()
        left_array = list()
        right_array = list()
        for e in array:
            if e == mid_elem:
                mid_array.append(e)
            elif e < mid_elem:
                left_array.append(e)
            else:
                right_array.append(e)
        return quick_merge_sort(left_array) + mid_array + \
            quick_merge_sort(right_array)


def two_sum():
    has = set()
    array = [4, 1, 5, 4, 2, 7, 7, 8, 3]
    k = 8
    for v in array:
        x = k - v
        if x in has:
            print(v)
            print(x)
            break
        else:
            has.add(v)





# Алгоритмы с указателями =====================================================
string = 'lol'


def polindrom(string):
    c1 = 0
    c2 = len(string) - 1
    while c1 < c2:
        if not string[c1].isalnum():
            c1 += 1
            continue
        elif not string[c2].isalnum():
            c2 -= 1
            continue
        if string[c1] != string[c2]:
            return False
        c1 += 1
        c2 -= 1
    return True


def mul_and_sort():
    '''Сортировка убывюще возростающего списка за O(n) черз 2 указателя'''
    x = [49, 30, 9, 4, 0, 7, 12, 16, 50]
    y = list()
    while x:
        value = None
        if x[0] > x[-1]:
            value = x.pop(0)
        else:
            value = x.pop()
        y.insert(0, value)

    print(y)

# =============================================================================


def merge_sort():
    ''' O(n)
    Сортировка слиянием через указатели для двух отсортированных списков.
    указатели куазывают на два перых элемета, после чего они сравниваются
    и в результатирующий список отправляется меньший элемент, далее указатель
    с меньшего элемента сдвигается, а указатель большего элемената остается
    на месте, далее повторяется сравнение, пока не переберутся все элементы.
    После того как один из списков закончится, результатирующий список
    расширяется оставшимися элементами одного из списков'''
    array1 = [1, 3, 6, 10, 12, 25]
    array2 = [-3, 4, 8, 10]
    result_array = list()

    count1 = 0
    count2 = 0

    while count1 < len(array1) and count2 < len(array2):
        value1 = array1[count1]
        value2 = array2[count2]
        if value1 < value2:
            result_array.append(value1)
            count1 += 1
        elif value1 > value2:
            result_array.append(value2)
            count2 += 1
        elif value1 == value2:
            result_array.append(value1)
            result_array.append(value2)
            count1 += 1
            count2 += 1
    else:
        lust_merge_value = array1[count1:]
        if lust_merge_value:
            result_array.extend(lust_merge_value)
        else:
            result_array.extend(array2[count2:])
        # or
        # result_array += array1[count1:] + array2[count2:]

    print(result_array)


# =============================================================================

def num():
    mums = [-4, -1, -1, 0, 3, 10]
    res = list()
    count1 = 0
    count2 = len(mums) - 1
    while count1 <= count2:
        val1 = mums[count1] ** 2
        val2 = mums[count2] ** 2
        if val1 > val2:
            res.append(val1)
            count1 += 1
        else:
            res.append(val2)
            count2 -= 1
    print(mums)
    print(*reversed(res))


def puzir_sort():
    array = [4, 1, 5, 4, 2, 7, 7, 8, 3]
    for run in range(len(array) - 1):
        for i in range(len(array) - 1 - run):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    print(array)


def true_scob():
    open_scob = {'{': '}', '[': ']', '(': ')'}
    scob = '(())'
    stack = list()
    flag = True
    for i in scob:
        if i in open_scob:
            stack.append(i)
        else:
            try:
                q = stack.pop()
                if i != open_scob[q]:
                    flag = False
                    break
            except IndexError:
                flag = False
                break
    print(flag)

def count_sort_method():
    mass = [0, 1, 0, 2, 4, 5, 3, 0, 1, 1, 1, 2, 5, 3]
    count = [0] * len(set(mass))
    for i in mass:
        count[i] += 1
        
    res_sort = [i for i, v in enumerate(count) for _ in range(v)]
    print(res_sort)
    
def qqq():
    arr1 = [2,2,5,8,14,19,29,30]
    arr2 = [-3,0,1,2,2,2,8,19]
    index1 = 0
    index2 = 0
    res_arr = list()
    while index1 < len(arr1) and index2 < len(arr2):
        val1 = arr1[index1]
        val2 = arr2[index2]
        if val1 == val2:
            res_arr.append(val1)
            index1 += 1
            index2 += 1
        elif val1 < val2:
            index1 += 1
        else:
            index2 += 1
    print(res_arr)



def qqq2():
    '''переместить нули'''
    arr = [2, 0, 0, 9, 3, 0, 1, 5, 5, 5, 0, 5, 5]
    index1 = 0
    index2 = 0
    while index2 < len(arr):
        if arr[index1] != 0:
            index1 += 1
        elif arr[index1] == 0 and arr[index2] != 0:
            arr[index1] = arr[index2]
            arr[index2] = 0
            index1 += 1
        index2 += 1



    print(arr)

        
        
        
'''
Паттерны для указателе:
1) С двух сторон - для одного массива
2) Каждому по указателю - для двух массиво
3) быстрый и медленный - для одного массива
'''



def bin_search():
    array = [1, 4, 6, 8, 10, 33, 54, 66, 67, 666]
    search = 1
    left = 0
    right = len(array) - 1

    while left <= right:  # Условие выхода из цикла
        index = (left + right) // 2  # Находим средний индекс
        value = array[index]
        
        if value == search:
            return True  # Элемент найден
        elif search < value:
            right = index - 1  # Искать в левой части
        else:
            left = index + 1  # Искать в правой части

    return False  # Элемент не найден

# Тестирование функции
result = bin_search()
print(result)  # Ожидаемый вывод: True

