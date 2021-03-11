'''
Задан массив целых чисел. Верните новый массив, в котором каждый элемент с индексом i нового массива 
является произведением всех элементов первоначального массива кроме самого элемента i. Например для ввода [1, 2, 3, 4, 5], 
возвращенный массив должен быть [120, 60, 40, 30, 24]. Если на входе задан массив [4,3,2], на выходе должен быть [6, 8, 12].

Как бонус: что если нельзя использовать деление?
'''

def get_factors(array):
    cumulative_product = 1
    right_prod_array = list()
    for num in array:
        cumulative_product *= num
        right_prod_array.append(cumulative_product)

    cumulative_product = 1
    left_prod_array = list()
    for num in array[::-1]:
        cumulative_product *= num
        left_prod_array.append(cumulative_product)
    left_prod_array = left_prod_array[::-1]

    output_array = list()
    for i in range(len(array)):
        num = None
        if i == 0:
            num = left_prod_array[i + 1]
        elif i == len(array) - 1:
            num = right_prod_array[i - 1]
        else:
            num = right_prod_array[i - 1] * left_prod_array[i + 1]
        output_array.append(num)
    
    return output_array

assert get_factors([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert get_factors([3, 2, 1]) == [2, 3, 6]