def merge(A, B):
    for i in range(len(B)):
        A.append(B[i])
    print(sorted(A))
A=[-4,3]
B=[-2,-2]
merge(A,B)