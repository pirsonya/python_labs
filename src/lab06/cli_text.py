
import argparse
import os
import sys
from pathlib import Path
import re
def normalize(text: str, *, casefold: bool=True, yo2e: bool=True) -> str:
    if casefold:
        text=text.casefold()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    text=text.replace('\t',' ').replace('\r',' ').replace('\n',' ')
    res=' '.join(text.split())
    return res

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
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]
def top_n(freq: dict[str, int], n: int=5) -> list[tuple[str, int]]:
    """Получение топ-N самых частых слов"""
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]

def get_word_frequencies(text):
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    return count_freq(tokens)
def get_top_words(frequencies, top_n=5):
    return top_n(frequencies, top_n)

def stats_command(input_file, top_count=5):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        print(f"Анализ файла: {input_file}")
        print("=" * 40)
        print(f"Исходный размер: {len(text)} символов")

        normalized_text = normalize(text)
        print(f"После нормализации: {len(normalized_text)} символов")
        
        tokens = tokenize(normalized_text)
        print(f"Найдено токенов: {len(tokens)}")
        
        frequencies = count_freq(tokens)
        print(f"Уникальных слов: {len(frequencies)}")
        
        top_words = top_n(frequencies, top_count)
        print(f"\nТоп-{top_count} самых частых слов:")
        print("-" * 25)
        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i:2}. {word:<15} {count:>5}")
            
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {input_file}")
    except Exception as e:
        raise Exception(f"Ошибка анализа текста: {e}")
    
def cat_command(input_file, number_lines=False):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file, 1):
                if number_lines:
                    print(f"{i:6}  {line}", end='')
                else:
                    print(line, end='')
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {input_file}")
    except Exception as e:
        raise Exception(f"Ошибка чтения файла: {e}")
import argparse
def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")
    # подкоманда cat 
    cat_parser = subparsers.add_parser("cat", help="Print file content")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Number lines")
    # подкоманда stats 
    stats_parser = subparsers.add_parser("stats", help="Word frequency")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()