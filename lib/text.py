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
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]