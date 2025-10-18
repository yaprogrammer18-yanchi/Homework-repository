# Эта функция сравнивает родителя с его потомками и меняет их местами
# в случае, если потомок больше родителя. Суть этой функции как раз в том, чтобы сделать
# кучу, где каждый родитель больше своих потомков.
def heapify(array, size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if (left < size) and (array[left] > array[largest]):
        largest = left
    if (right < size) and (array[right] > array[largest]):
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, size, largest)


def heap_sort(numbers):
    n = len(numbers)
    # строим первую max-кучу
    # идем от последнего родителя до корневого
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)
    # идем от последних элементов, так как там находятся самые маленькие из всех после формирования кучи
    for i in range(n - 1, -1, -1):
        # перемещаем максимум в конец
        numbers[0], numbers[i] = numbers[i], numbers[0]
        # восстанавливаем кучу, каждый раз уменьшая длину, чтобы не затрагивать отсортированные последние элементы
        heapify(numbers, i, 0)
    return numbers


# P.S. Прошу прощения за большое количество, наверняка очевидных, комментариев, писала их,
# чтобы лучше разбираться в том, что пишу.
