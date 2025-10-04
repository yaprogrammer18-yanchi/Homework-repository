"""Алгоритм реализован по математической формуле"""


def gcd_usual(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_extended(a, b):
    # задаем изначальные значения коэффициентов (как будто они предыдущие)
    remember_r = a
    remember_s = 1
    remember_t = 0
    # задаем "настоящие" в временном контексте значения коэффициентов (r1, s1, t1)
    r = b
    s = 0
    t = 1
    gcd_to_stop = gcd_usual(a, b)  # вычисляем НОД чтобы вовремя остановить алгоритм
    while r != gcd_to_stop:
        # вычисляем новые значение коэфов, при этом записывая пройденные в запомненные
        s, remember_s = remember_s - (remember_r // r) * s, s
        t, remember_t = remember_t - (remember_r // r) * t, t
        r, remember_r = remember_r - (remember_r // r) * r, r
    return (s, t, r)
