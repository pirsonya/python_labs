import sys
from pathlib import Path
import csv
from typing import Iterable, Sequence
import re


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


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)

    return p.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:

    p = Path(path)
    rows = list(rows)
    if rows:
        first_len_rows = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_len_rows:
                raise ValueError
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def main():
    input_file = "data/input.txt"
    output_file = "data/report.csv"
    encoding = "utf-8"
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        text = normalize(text)
        words = tokenize(text)
        words_count = count_freq(words)
        sort_w = top_n(words_count, len(words_count))
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("word,count\n")
            for word, count in sort_w:
                f.write(f"{word},{count}\n")
        total_words = len(words)
        unique_words = len(words_count)
        top_5 = top_n(words_count, 5)
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_5:
            print(f"{word}:{count}")
    except FileNotFoundError:
        print(f"файл '{input_file}' не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
