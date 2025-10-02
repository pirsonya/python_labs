#min_max
a=[1.5, 2, 2.0, -3.1]
def min_max(a: list[float | int]) -> tuple[float | int, float | int]:
    sp=[]
    if len(a)==0:
        raise ValueError
    sp.append(min(a))
    sp.append(max(a))
    return sp
print(min_max(a))

#unique_sorted
b=[1.0, 1, 2.5, 2.5, 0]
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    s=sorted(list(set(b)))
    return s
print(unique_sorted(b))


#flatten
c=([1, 2], (3, 4, 5))
def flatten(mat: list[list | tuple]) -> list:
    sp=[]
    for el in c:
        if not isinstance(el, (list,tuple)):
            raise TypeError
        for i in el:
            sp.append(i)
    return sp
print(flatten(c))


