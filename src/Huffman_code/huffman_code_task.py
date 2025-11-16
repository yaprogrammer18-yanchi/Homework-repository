class Node:
    def __init__(self, symbol=None, freq=0):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        self.path = ''


def encode(msg: str) -> tuple[str, dict[str, str]]:
    lst_of_nodes = []

    def make_table_symbol_and_freq(msg):
        msg = list(msg)
        while msg != []:
            node = Node(msg[0], msg.count(msg[0]))
            msg = (''.join(msg)).replace(msg[0], '')
            msg = list(msg)
            lst_of_nodes.append(node)

    def heapify(lst_of_nodes):
        while len(lst_of_nodes) > 1:
            lst_of_nodes.sort(key=lambda x: x.freq)
            left = lst_of_nodes.pop(0)
            right = lst_of_nodes.pop(0)

            # создаем новый элемент с частотой равной сумме двух выбранных
            node = Node(freq=left.freq + right.freq)
            node.left = left
            node.right = right
            lst_of_nodes.append(node)

    make_table_symbol_and_freq(msg)
    heapify(lst_of_nodes)
    table = {}
    def code_and_collect_every_path(node, prefix):
        if node.symbol is not None:
            node.path = prefix
            table[node.symbol] = node.path
        else:
            if node.left:
                code_and_collect_every_path(node.left, prefix + "0")
            if node.right:
                code_and_collect_every_path(node.right, prefix + "1")



    if lst_of_nodes:
        code_and_collect_every_path(lst_of_nodes[0], '')

    encoded_msg = ''
    for el in msg:
        encoded_msg += table[el]

    return (encoded_msg, table)


















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