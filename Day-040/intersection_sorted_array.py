def intersect(A, B):
    l = []
    i_A = 0
    i_B = 0
    while i_A < len(A) and i_B < len(B):
        if A[i_A] == B[i_B]:
            l.append(A[i_A])
            i_A += 1
            i_B += 1
        elif A[i_A] > B[i_B]:
            i_B += 1
        else:
            i_A += 1
    return l

A=[1,2,3,3,4,5,6]
B=[3,3,5]
intersect(A,B)

