# функция для проверки, безопасное ли место, куда хотят поставить ферзя
def is_safe(board, row, col):
    current_row, current_column = row, col
    for line in range(row):
        row, col = line, board[line].index(1)
        # проверка по вертикали
        if current_column == col:
            return False
        # проверка по диагонали
        if abs(row - current_row) == abs(col - current_column):
            return False
    return True


def find_combinations(n):
    board = [[0] * n for _ in range(n)]
    count_of_combinations = 0

    def row_enumeration(row):
        nonlocal count_of_combinations
        if row == n:  # рекурсия дошла до логического конца
            count_of_combinations += 1
            return

        for column in range(n):
            if is_safe(board, row, column):  # проверка на то, что сюда можно поставить ферзя
                board[row][column] = 1
                row_enumeration(row+1)
                board[row][column] = 0
                # убираем ферзя, так как в следующей итерации мы поставим его на другое место, но в этом же ряду
    row_enumeration(0)
    return count_of_combinations


def main(n):
    return find_combinations(n)
