from itertools import permutations


def solve(n):
    all_lines = [i for i in
                 range(n)]  # все позиции, на которых могут стоять ферзи
    d = {}
    for el in all_lines:
        d[el] = []  # посмотрим, какие позиции потенциально могут занимать ферзи, стоящие на строку ниже предложенных
    for first_line in d.keys():
        for second_line in range(n):
            if second_line not in [first_line - 1, first_line, first_line + 1]:
                d[first_line].append(second_line)
    count = 0
    for perm in permutations(range(n)):
        flag = True
        for i in range(len(perm)-1):
            if perm[i+1] not in d[perm[i]]:
                flag = False
                break
        if flag:
            print(perm)

solve(16)


# из-за того, что permutations все-таки со сложностью O(n!) то общая сложность этой функции будет O(n! * n)
# Мне очень хотелось решить эту задачу через словарь,
# но я особо дальше n! не ушла, так что просто оставлю это решение здесь:)



