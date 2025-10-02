#min_max
a=[3, -1, 5, 5, 0]
#b=[42]
#c=[-5, -2, -9]
#d=[]
#e=[1.5, 2, 2.0, -3.1]
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    sp=[]
    if len(nums)==0:
        raise ValueError
    sp.append(min(nums))
    sp.append(max(nums))
    return sp
print(min_max(a))
#print(min_max(b))
#print(min_max(c))
#print(min_max(e))
#print(min_max(d))

#unique_sorted
a=[3, 1, 2, 1, 3]
#b=[]
#c=[-1, -1, 0, 2, 2]
#d=[1.0, 1, 2.5, 2.5, 0]
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    s=sorted(list(set(nums)))
    return s
print(unique_sorted(a)) 
#print(unique_sorted(b)) 
#print(unique_sorted(c)) 
#print(unique_sorted(d)) 


#flatten
a=[[1, 2], [3, 4]]
# b=([1, 2], (3, 4, 5))
# c=[[1], [], [2, 3]]
# d=[[1, 2], "ab"]

def flatten(mat: list[list | tuple]) -> list:
    sp=[]
    for el in mat:
        if not isinstance(el, (list,tuple)):
            raise TypeError
        for i in el:
            sp.append(i)
    return sp
print(flatten(a))
# print(flatten(b))
# print(flatten(c))
# print(flatten(d))



### Тест-кейсы (минимум)
# **min_max**
# - `[3, -1, 5, 5, 0]` → `(-1, 5)`
# - `[42]` → `(42, 42)`
# - `[-5, -2, -9]` → `(-9, -2)`
# - `[]` → `ValueError`
# - `[1.5, 2, 2.0, -3.1]` → `(-3.1, 2)`

# **unique_sorted**
# - `[3, 1, 2, 1, 3]` → `[1, 2, 3]`
# - `[]` → `[]`
# - `[-1, -1, 0, 2, 2]` → `[-1, 0, 2]`
# - `[1.0, 1, 2.5, 2.5, 0]` → `[0, 1.0, 2.5]` *(допускаем смешение int/float)*

# **flatten**
# - `[[1, 2], [3, 4]]` → `[1, 2, 3, 4]`
# - `([1, 2], (3, 4, 5))` → `[1, 2, 3, 4, 5]`
# - `[[1], [], [2, 3]]` → `[1, 2, 3]`
# - `[[1, 2], "ab"]` → `TypeError` *(«строка не строка строк матрицы»)*