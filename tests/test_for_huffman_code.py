from hypothesis import given
import hypothesis.strategies as st
from src.Huffman_code.huffman_code_task import encode, decode


@given(st.text())
def test_that_everything_works_with_any_text(text):
    msg, table = encode(text)
    assert decode(msg, table) == text

@given(st.text())
def test_types(text):
    msg, table = encode(text)
    decoded_msg = decode(msg, table)
    assert type(msg) == str and type(table) == dict and type(decoded_msg) == str

@given(st.text())
def test_table_equality(text):
    msg1, table1 = encode(text)
    msg2, table2 = encode(text)
    assert decode(msg1, table1) == text
    assert decode(msg2, table2) == text

def test_empty_string():
    msg, table = encode("")
    assert decode(msg, table) == ""
    assert table == {}

def test_single_character():
    msg, table = encode("a")
    assert decode(msg, table) == "a"
    assert len(table) == 1

    def test_repeated_character():
        msg, table = encode("aaaaa")
        assert decode(msg, table) == "aaaaa"

def test_special_characters():
    text = "!@#$%^&*()\n\t\r"
    msg, table = encode(text)
    assert decode(msg, table) == text
