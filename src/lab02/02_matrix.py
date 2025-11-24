# transpose
a = [[1, 2, 3]]


# b=[[1], [2], [3]]
# c=[[1, 2], [3, 4]]
# d=[]
# e=[[1, 2], [3]]
def transpose(mat: list[list[float | int]]) -> list[list]:
    sp3 = []
    if len(mat) > 0:
        sp3_len = len(mat[0])
        if all(len(sps) == sp3_len for sps in mat):
            for i in range(len(mat[0])):
                nsp = []
                for j in range(len(mat)):
                    nsp.append(mat[j][i])
                sp3.append(nsp)
        else:
            raise ValueError
    return sp3


print(transpose(a))
# print(transpose(b))
# print(transpose(c))
# print(transpose(d))
# print(transpose(e))

# row_sums
a = [[1, 2, 3], [4, 5, 6]]


# b=[[-1, 1], [10, -10]]
# c=[[0, 0], [0, 0]]
# d=[[1, 2], [3]]
def row_sums(mat: list[list[float | int]]) -> list[float]:
    sp = []
    if len(mat) > 0:
        sp_len = len(mat[0])
        if all(len(sps) == sp_len for sps in mat):
            for i in range(len(mat)):
                sm = sum(mat[i])
                sp.append(sm)
        else:
            raise ValueError()
    else:
        sp = []
    return sp


print(row_sums(a))
# print(row_sums(b))
# print(row_sums(c))
# print(row_sums(d))


# col_sums
a = [[1, 2, 3], [4, 5, 6]]


# b=[[-1, 1], [10, -10]]
# c=[[0, 0], [0, 0]]
# d=[[1, 2], [3]]
def col_sums(mat: list[list[float | int]]) -> list[float]:
    sp2 = []
    if len(mat) > 0:
        sp2_len = len(mat[0])
        if all(len(sps2) == sp2_len for sps2 in mat):
            for i in range(len(mat[0])):
                sm = 0
                for j in range(len(mat)):
                    sm += mat[j][i]
                sp2.append(sm)
        else:
            raise ValueError
    return sp2


print(col_sums(a))
# print(col_sums(b))
# print(col_sums(c))
# print(col_sums(d))


### Тест-кейсы (минимум)
# **transpose**
# - `[[1, 2, 3]]` → `[[1], [2], [3]]`
# - `[[1], [2], [3]]` → `[[1, 2, 3]]`
# - `[[1, 2], [3, 4]]` → `[[1, 3], [2, 4]]`
# - `[]` → `[]`
# - `[[1, 2], [3]]` → `ValueError` (рваная матрица)

# **row_sums**
# - `[[1, 2, 3], [4, 5, 6]]` → `[6, 15]`
# - `[[-1, 1], [10, -10]]` → `[0, 0]`
# - `[[0, 0], [0, 0]]` → `[0, 0]`
# - `[[1, 2], [3]]` → `ValueError` (рваная)

# **col_sums**
# - `[[1, 2, 3], [4, 5, 6]]` → `[5, 7, 9]`
# - `[[-1, 1], [10, -10]]` → `[9, -9]`
# - `[[0, 0], [0, 0]]` → `[0, 0]`
# - `[[1, 2], [3]]` → `ValueError` (рваная)
