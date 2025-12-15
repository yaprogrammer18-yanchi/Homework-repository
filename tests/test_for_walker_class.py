from src.Walker.Walker_class import Walker
import pytest


def test_1_prob_occasion():
    walker_scheme = Walker([["A", 1], ["D", 0]])
    assert walker_scheme.get_random() == "A"


def test_error():
    with pytest.raises(ValueError, match="Вероятности в сумме не дают 1!"):
        Walker([["A", 0], ["D", 0]])


def test_empty_list():
    with pytest.raises(ValueError, match="Переданный список пустой"):
        Walker([])


def test_error_sum_under_one():
    with pytest.raises(ValueError, match="Вероятности в сумме не дают 1!"):
        Walker([["A", 0.5], ["D", 0.4]])