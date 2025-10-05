from itertools import permutations


# Так как всего N ферзей, то каждый ферзь обязательно будет располагаться на одной из строк.
# И в каждой строке будет стоять свой ферзь, если их вообще возможно всех разместить.
# Идея просто пересмотреть всевозможные перестановки с помощью permutations, проверяя все ли ферзи безопасно стоят.


def all_possible_positions(n):  # возвращает все позиции ферзя на одной строке
    all_possible_positions = [[0] * n for _ in range(n)]
    column = 0  # чтоб не делать вложенный список
    for i in range(n):
        all_possible_positions[i][column] = 1
        column += 1
    return all_possible_positions


def queen(n):
    all_possib_posit = all_possible_positions(n)
    count_of_combinations = 0
    for board in permutations(
        all_possib_posit
    ):  # будем рассматривать всевозможные расположения ферзей
        # board - это уже полноценная шахматная доска с расставленными ферзями
        list_of_unsafe_places = []

        # поиск небезопасных мест по диагоналям
        for line in range(n):
            row_of_qeen, col_of_queen = line, board[line].index(1)
            # Мы проверяем только диагонали
            row, col = row_of_qeen, col_of_queen

            while col - 1 >= 0 and row + 1 < n:  # выполняется меньше n раз
                row += 1
                col -= 1
                if [row, col] not in list_of_unsafe_places:
                    list_of_unsafe_places.append([row, col])

            row, col = row_of_qeen, col_of_queen

            while col + 1 < n and row + 1 < n:  # выполняется меньше n раз
                row += 1
                col += 1
                if [row, col] not in list_of_unsafe_places:
                    list_of_unsafe_places.append([row, col])

        every_queen_is_safe = True
        for i in range(len(board)):
            if [i, board[i].index(1)] in list_of_unsafe_places:
                every_queen_is_safe = False
                break
                # сразу завершаем цикл, если хотя бы один ферзь не там стоит
        if every_queen_is_safe:
            count_of_combinations += 1
    return count_of_combinations