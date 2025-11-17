from pathlib import Path
import csv
from pathlib import Path
from typing import Iterable, Sequence
# from lib.text import normalize, tokenize, top_n, count_freq

def normalize(text: str, *, casefold: bool=True, yo2e: bool=True) -> str:
    if casefold:
        text=text.casefold()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    text=text.replace('\t',' ').replace('\r',' ').replace('\n',' ')
    res=' '.join(text.split())
    return res

import re
def tokenize(text: str) -> list[str]:
    pattern=r'\w+(?:-\w+)*'
    return re.findall(pattern, text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict={}
    for token in tokens:
        if token in freq_dict:
            freq_dict[token]+=1
        else:
            freq_dict[token]=1
    return freq_dict

def top_n(freq: dict[str, int], n: int=5) -> list[tuple[str, int]]:
    def sort_key(item):
        word, frequency=item
        return (-frequency, word)
    sorted_items=sorted(freq.items(), key=sort_key)
    return sorted_items[:n]


#октрытие файла->строка
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    
    return p.read_text(encoding=encoding)
def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
#header-заголовок столбцов
    p = Path(path)
    rows = list(rows)
    if rows:
        first_len_rows=len(rows[0])
        for i, row in enumerate(rows):
            if len(row)!=first_len_rows:
                raise ValueError
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
def freq_from_txt(text: str) -> dict[str, int]:
    tokens=tokenize(normalize(text))
    return count_freq(tokens)

def sort_w_counts(freq: dict[str,int]) -> list[tuple[str,int]]:
    return top_n(freq, len(freq))


# Тест-кейс A: Один файл
def test_case_a():
 
    text = read_text("src/lab04/input.txt")
    

    freq = freq_from_txt(text)
    sorted_words = sort_w_counts(freq)

    total_words = sum(freq.values())
    unique_words = len(freq)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    
    for word, count in sorted_words[:5]:
        print(f"{word}:{count}")
    
    write_csv(sorted_words, "report.csv", header=("word", "count"))
    print("\nCохранено в report.csv")


if __name__ == "__main__":
    test_case_a()
    