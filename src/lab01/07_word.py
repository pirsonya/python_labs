n=str(input())
s=list(n)
word=''
#находим первую букву слова
for i in range(len(s)-1):
    if str(s[i])==str((s[i]).upper()):
        ind_1=s.index(s[i])
        sym_1=s[i]
        word+=s[i]
        break
#находим вторую букву слова
alph='0123456789'
for i in range(len(s)-1):
    if str(s[i]) in alph:
        ind_2=s.index(s[i+1])
        sym_2=s[i+1]
        word+=s[i+1]
        break

#находим расстояние между первой и второй буквой
distance=int(ind_2)-int(ind_1)
last_ind=s.index(s[-1])
s=s[ind_1:last_ind+1:distance]
string=''
for el in s:
    string+=el
print(string)
        