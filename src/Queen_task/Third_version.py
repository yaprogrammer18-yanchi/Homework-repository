def main(n):
    all_lines = [i for i in range(n)] # все позиции, на которых могут стоять ферзи
    d = {}
    for el in all_lines:
        d[el] = []

    # посмотрим, какие позиции потенциально могут занимать ферзи, стоящие на строку ниже предложенных
    for first_line in d.keys():
        for second_line in range(n):
            if second_line not in [first_line-1, first_line, first_line+1]:
                d[first_line].append(second_line)
    count_combinations = []
    line = [0] * n  # сюда будем собирать комбинации
    elem_working = 0 # индекс последнего элемента, которого добавили
    return solve(line, d, count_combinations, elem_working, n)





def solve(line, d, count_cobinations, elem_working, n):
    if elem_working==n:
        count_cobinations.append(1)
        return # вся строка заполнена

    for el in range(n):
        if elem_working == 0:
            line[elem_working] = el

        elif el in d[line[elem_working-1]] and el not in line:
            line[elem_working] = el
            solve(line, d, count_cobinations, elem_working + 1, n)
            line[elem_working] = 0







main(4)






