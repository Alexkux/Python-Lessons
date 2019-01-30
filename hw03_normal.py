# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """Функция возвращает ряд Фибоначи от параметра n до параметра m
    """
    a, b = 1, 1
    f_list = [1, ]
    for i in range(m):
        a, b = b, a + b
        f_list.append(a)
    return f_list[n - 1:m]
print('fibonacci(6, 10): ', fibonacci(6, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(income_list):
    """Функция сортировки списка по возрастанию
    """
    if len(income_list) > 1:
        pivot_index = len(income_list) // 2
        min_items = []
        max_items = []
        for i, val in enumerate(income_list):
            if i != pivot_index:
                if val < income_list[pivot_index]:
                    min_items.append(val)
                else:
                    max_items.append(val)
        sort_to_max(min_items)
        sort_to_max(max_items)
        income_list[:] = min_items + [income_list[pivot_index]] + max_items
     return income_list
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_func(function, iterable):
    """ filter elements divisible by three
    """
    return (item for item in iterable if function(item))

print(list(filter_func(lambda x: True if x % 3 == 0 else False,
                  [1, 7, 3, 11, 5, 6, 7, 8, 9, 12])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram_check(a1, a2, a3, a4):
    """Verifying Parallelogram Vertices
    """
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False
print(parallelogram_check([2,3],[-1,4],[1,1],[4,0]))
print(parallelogram_check([2,7],[-1,7],[1,8],[4,7]))
