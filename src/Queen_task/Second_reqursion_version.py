# функция для проверки, безопасное ли место, куда хотят поставить ферзя
def is_safe(board, row, col):
    n = len(board)
    row_to_put, col_to_put = row, col
    for line in range(row):  # перебираем все ряды до желаемого ряда
        row, col = line, board[line].index(1)
        # посмотрим, что по вертикали все в порядке
        if col_to_put == col:
            return False

        # здесь мы смотрим на диагонали
        while col - 1 >= 0 and row + 1 < n:
            row += 1
            col -= 1
            if row == row_to_put and col == col_to_put:
                return False

        row, col = line, board[line].index(1)

        while col + 1 < n and row + 1 < n:
            row += 1
            col += 1
            if row == row_to_put and col == col_to_put:
                return False

    return True


# сама рекурсивная функция
def finding_combinations(board, row, n, count_of_combinations):
    if row == n:  # рекурсия дошла до логического конца
        count_of_combinations.append(1)
        return  # мы посчитали эту комбинацию, следующий шаг будет возврат в ранее вызванную функцию solve
        #  и board[row][col] = 0 станет следующим шагом той функции

    for col in range(n):  # начинаем перебирать столбцы
        if is_safe(board, row, col):  # проверка на то, что сюда можно поставить ферзя
            board[row][col] = 1  # ставим его
            finding_combinations(
                board, row + 1, n, count_of_combinations
            )  # начинаем рассматривать следующий ряд
            # но с измененной уже доской и поставленным ферзем
            # когда рекурсия дойдет до какого-то решения, то мы будем рассматривать все заново, но
            # col уже сдвинется на один => так мы сможем посчитать все решения
            board[row][col] = 0
            # убираем ферзя, так как в следующей итерации мы поставим его на другое место, но в этом же ряду


def main(n):
    board = [[0] * n for _ in range(n)]  # сформировали доску
    count_of_combinations = []  # список удобно передавать, так как он всегда занимает одно место в памяти и тут он
    # сравним с некой глобальной переменной
    finding_combinations(board, 0, n, count_of_combinations)
    return len(count_of_combinations)
