import hypothesis.strategies as st
from src.curry_task import curry, uncurry, MyError
from hypothesis import given

@given(args=st.lists(st.integers(min_value=1), min_size=1))

def test_universal_check(args):
    def summ(*args):
        return sum(args)

    func = curry(summ, len(args))
    for el in args:
        func = func(el)
    assert func == sum(args)
