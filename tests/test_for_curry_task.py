import hypothesis.strategies as st
from src.curry_task import curry, uncurry, MyError
from hypothesis import given

@given(a=st.integers(), b=st.integers(), c=st.integers())
def test_sum_three_elements_check(a, b, c):
    def summ(a, b, c):
        return a + b + c

    func = curry(summ, 3)
    uncarried_func = uncurry(func, 3)
    for el in (a, b, c):
        func = func(el)
    assert func == a + b + c
    assert uncarried_func(a, b, c) == a + b + c


@given(a=st.integers(), b=st.integers(), c=st.integers())
def test_mul_three_elements_check(a, b, c):
    def mul(a, b, c):
        return a * b * c

    func = curry(mul, 3)
    uncarried_func = uncurry(func, 3)
    for el in (a, b, c):
        func = func(el)
    assert func == a * b * c
    assert uncarried_func(a, b, c) == a * b * c


@given(a=st.integers(max_value=5), b=st.integers(max_value=5), c=st.integers(max_value=5))
def test_power_element_check(a, b, c):
    def power(a, b, c):
        return a**b**c

    func = curry(power, 3)
    uncarried_func = uncurry(func, 3)
    for el in (a, b, c):
        func = func(el)
    assert func == a**b**c
    assert uncarried_func(a, b, c) == a ** b ** c


def test_wrong_arity_errors1():
    try:
        def summ(a, b, c):
            return a + b + c

        curry(summ, -1)
        assert False
    except MyError as e:
        assert isinstance(e, MyError)
        assert str(e) == "Арность не может быть меньше или равна 0."


def test_wrong_arity_errors2():
    try:
        def summ(a, b, c):
            return a + b + c

        curry(summ, 5)
        assert False
    except MyError as e:
        assert isinstance(e, MyError)
        assert str(e) == "Переданная арность больше действительной."


def test_wrong_arity_errors3():
    try:
        def mul(a, b, c):
            return a * b * c

        curry(mul, 1.0)
        assert False
    except MyError as e:
        assert isinstance(e, MyError)
        assert str(e) == "Переданная арность функции обязана быть целым числом."

@given(args=st.lists(st.integers(), min_size=4))
def test_wrong_quantity_of_arguments(args):
    try:
        def summ(a, b, c):
            return a + b + c

        func = curry(summ, 3)
        uncarried_func = uncurry(func, 3)
        uncarried_func(args)
        assert False
    except MyError as e:
        assert isinstance(e, MyError)
        assert str(e) == "Передано неверное кол-во аргументов."
