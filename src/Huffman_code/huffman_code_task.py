import json


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
    if len(table) == 1:
        char = list(table.keys())[0]
        table[char] = '0'  # или '1' - любой непустой код
    encoded_msg = ''
    for el in msg:
        encoded_msg += table[el]
    return (encoded_msg, table)


def decode(encoded: str, table: dict[str, str]) -> str:
    decoding_table = {code: char for char, code in table.items()}
    lst_of_decoded_chars = []
    r = 0
    left = 1
    while r != len(encoded):
        tmp = encoded[r:left]
        if tmp not in lst_of_decoded_chars and tmp in decoding_table:
            lst_of_decoded_chars.append(decoding_table[tmp])
            r = left
        left+=1
    return ''.join(lst_of_decoded_chars)


def encode_file(input_path, output_path):
    with open(input_path, 'r', encoding="utf-8") as input_file:
        msg = input_file.read()
        encoded_msg, table = encode(msg)

    table = json.dumps(table, ensure_ascii=False)
    table_bytes = table.encode("utf-8")
    encoded_bytes = encoded_msg.encode("utf-8")

    with open(output_path, 'wb') as output_file:
        # записали в 4 байта размер таблицы
        table_size_in_bytes = len(table_bytes).to_bytes(4, 'big')
        output_file.write(table_size_in_bytes)
        output_file.write(table_bytes)
        output_file.write(encoded_bytes)


def decode_file(input_path, output_path):
    with open(input_path, 'rb') as input_file:
        quantity_of_bytes = input_file.read(4)
        table_size = int.from_bytes(quantity_of_bytes, 'big')
        table_bytes = input_file.read(table_size)
        msg = input_file.read()

    with open(output_path, "w", encoding="utf-8") as output_file:
        table_json = table_bytes.decode("utf-8")
        output_file.write(table_json)
        output_file.write('\n')
        output_file.write(msg.decode("utf-8"))
