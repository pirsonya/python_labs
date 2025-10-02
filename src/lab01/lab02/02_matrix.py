#transpose
c=[]
def transpose(mat: list[list[float | int]]) -> list[list]:
    sp3=[]
    if len(mat)>0:
        sp3_len = len(mat[0])
        if all(len(sps) == sp3_len for sps in mat):
            for i in range(len(mat[0])):
                nsp=[]
                for j in range(len(mat)):
                    nsp.append(mat[j][i])
                sp3.append(nsp)
        else:
            raise ValueError
    return sp3
print(transpose(c))
      
#row_sums
a = [[1, 2, 3], [4, 5, 6]]
def row_sums(mat: list[list[float | int]]) -> list[float]:
    sp = []
    if len(a)>0:  
        sp_len = len(a[0])
        if all(len(sps) == sp_len for sps in a):
            for i in range(len(a)):
                sm = sum(a[i])
                sp.append(sm)
        else:
            raise ValueError()
    else:
        sp = []
    return sp
print(row_sums(a))
  


#col_sums
b=[[1, 2, 3], [4, 5, 6]]
def col_sums(mat: list[list[float | int]]) -> list[float]:
    sp2=[]
    if len(b)>0:
        sp2_len = len(b[0])
        if all(len(sps2) == sp2_len for sps2 in b):
            for i in range(len(b[0])):
                sm=0
                for j in range (len(b)):
                    sm+=b[j][i]
                sp2.append(sm)
        else:
            raise ValueError
    return sp2
print(col_sums(b))


    