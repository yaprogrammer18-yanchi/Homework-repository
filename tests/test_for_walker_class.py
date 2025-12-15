from src.Walker.Walker_class import Walker
import pytest


def test_1_prob_occasion():
    walker_scheme = Walker([["A", 1], ["D", 0]])
    assert(walker_scheme.get_random() == "A")

def test_error():
    with pytest.raises(ValueError, match="Вероятности в сумме не дают 1!"):
        walker_scheme = Walker([["A", 0], ["D", 0]])

def test_usual_occasion():
    a = Walker([["A", 0.24], ["D", 0.11], ["E", 0.34], ["C", 0.28], ["B", 0.03]])
    print(a.events_and_prob)

def test_empty_list():
    with pytest.raises(ValueError, match="Переданный список пустой"):
        walker_scheme = Walker([])

