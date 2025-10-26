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

#функция-вывод текста таблицей
def table(top_n_words):
    if not top_n_words:
        return
    mx_len=max(len(word) for word, count in top_n_words)
    mn_width=max(mx_len, len('слово'))
    print(f"│ {'слово':<{mn_width}} │ {'частота'} │")
    print(f"├{'─' * (mn_width + 2)}┼{'────────-┤'}")
    for word, count in top_n_words:
        print(f"│ {word:<{mn_width}} │ {count:>6}  │")
    print(f"└{'─' * (mn_width + 2)}┴{'────────-┘'}")
    
def files_in():
    files=['data/a.txt', 'data/b.txt']
    res=[]
    total={}

    for files_name in files:
        with open(files_name, 'r', encoding='utf-8') as f:
            text=f.read()
        
        words=tokenize(normalize(text))
        freq=count_freq(words)

        for word, count in freq.items():
            total[word]=total.get(word,0)+count
            res.append((files_name, word, count))
    res.sort(key=lambda x: (x[0], -x[2], x[1]))

    with open('data/files_report.csv','w') as f:
        f.write('file,word,count\n')
        for file, word, count in res:
            f.write(f'{file},{word},{count}\n')
    
    total_sort=top_n(total,len(total))
    with open('data/total_report.csv','w') as f:
        f.write('word,count\n')
        for word, count in total_sort:
            f.write(f'{word},{count}\n')
    for files_name in files:
        print(f'\n{files_name}:')
        file_words=[(w,c) for f,w,c in res if f == files_name]
        table(file_words[:5])
    table(total_sort[:10])

if __name__=='__main__':
    files_in()  




