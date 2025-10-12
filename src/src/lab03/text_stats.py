import sys
import os
# from lib.text import count_freq, top_n, normalize, tokenize
def reading():
    return sys.stdin.read()
def table(top_n_words):
    if not top_n_words:
        return
    mx_len=max(len(word) for word, count in top_n_words)
    mn_width=max(mx_len, len('слово'))
    print(f"{'слово':<{mn_width}} | частота")
    print('-' * (mn_width + 3 + len('частота')))
    for word, count in top_n_words:
        print(f"{word:<{mn_width}} | {count}")
def first_ver(top_n_words):
    for word, count in top_n_words:
        print(f'{word}:{count}')
def main():
    text=reading()
    if not text.strip():
        sys.exit(1)
    norm_text=normalize(text, casefold=True, yo2e=True)
    tokens=tokenize(norm_text)
    word_text=count_freq(tokens)
    top5_words=top_n(word_text, 5)
    total_w, unique_w=len(tokens), len(word_text)
    print(f'Всего слов: {total_w}')
    print(f'Уникальных слов: {unique_w}')
    print('Топ-5:')
    table_mode = os.getenv('TEXT_STATS_TABLE', 'false').lower() == 'true'
    if table_mode:
        table(top5_words)
    else:
        first_ver(top5_words)
if __name__=='__main__':
    main()



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