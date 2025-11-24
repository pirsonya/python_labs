import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   \t\n\r  ", ""),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("test\t\ttest", "test test"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


def test_normalize_all_combinations():
    text = "ПрИвЕт Ёжик"
    assert normalize(text) == "привет ежик"
    assert normalize(text, casefold=False) == "ПрИвЕт Ежик"
    assert normalize(text, yo2e=False) == "привет ёжик"
    assert normalize(text, casefold=False, yo2e=False) == "ПрИвЕт Ёжик"


@pytest.mark.parametrize(
    "source, expected",
    [
        ("Привет, мир!", ["Привет", "мир"]),
        ("Hello world!", ["Hello", "world"]),
        ("Simple text", ["Simple", "text"]),
        ("", []),
        ("!@#$%^&*()", []),
        ("123 numbers", ["123", "numbers"]),
        ("какой-то текст", ["какой-то", "текст"]),
        ("по-русски по-английски", ["по-русски", "по-английски"]),
        ("word1 word2-word3", ["word1", "word2-word3"]),
        ("test-test test", ["test-test", "test"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([], {}),
        (["hello"], {"hello": 1}),
        (["a", "a", "a"], {"a": 3}),
    ],
)
def test_count_freq_parametrized(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({}, 5, []),
        ({"a": 1}, 0, []),
        ({"a": 1, "b": 2}, 5, [("b", 2), ("a", 1)]),
        (
            {"apple": 3, "banana": 3, "cherry": 3, "date": 2},
            3,
            [("apple", 3), ("banana", 3), ("cherry", 3)],
        ),
        ({"z": 5, "a": 5, "m": 5}, 3, [("a", 5), ("m", 5), ("z", 5)]),
    ],
)
def test_top_n_parametrized(freq, n, expected):
    assert top_n(freq, n) == expected
