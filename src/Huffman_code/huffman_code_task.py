import heapq


class Node:
    def __init__(self, symbol=None, freq=0):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        self.path = None

    def __lt__(self, other):
        return self.freq < other.freq

# разбить на мелкие функции
def encode(msg: str) -> tuple[str, dict[str, str]]:

    msg = list(msg)
    lst_of_nodes = []
    while msg != []:
        node = Node(msg[0], msg.count(msg[0]))
        msg = (''.join(msg)).replace(msg[0], '')
        msg = list(msg)
        lst_of_nodes.append(node)

    while len(lst_of_nodes) > 1:
        lst_of_nodes.sort(key=lambda x: x.freq)
        left = lst_of_nodes.pop(0)
        right = lst_of_nodes.pop(0)
        # создаем новый элемент с частотой равной сумме двух выбранных
        node = Node(freq=left.freq+right.freq)
        node.left = left
        node.right = right
        lst_of_nodes.append(node)















    # отсортировать
    # цикл с сортировкой + объединением + добавлением пути и тп



encode('122333444455555')




























def decode(encoded: str, table: dict[str, str]) -> str:
    # Возвращает раскодированную строку
    pass

def encode_file(input_path: str, output_path: str):
    # Читает текстовый файл, кодирует и записывает в бинарный файл
    pass

def decode_file(input_path: str, output_path: str):
    # Читает бинарный файл, декодирует и записывает текстовый файл
    pass

# + сделать тестов для всего этого