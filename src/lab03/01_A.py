def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    res = " ".join(text.split())
    return res


import re


def tokenize(text: str) -> list[str]:
    pattern = r"\w+(?:-\w+)*"
    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1
    return freq_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    def sort_key(item):
        word, frequency = item
        return (-frequency, word)

    sorted_items = sorted(freq.items(), key=sort_key)
    return sorted_items[:n]


print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
res1 = top_n(freq1, n=2)
print(f"{res1}")

tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freq2 = {"aa": 2, "bb": 2, "cc": 1}
res2 = top_n(freq2, n=2)
print(f"{res2}")
