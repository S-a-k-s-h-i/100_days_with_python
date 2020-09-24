def lp(A):
    A.sort()
    ot=list(A[0])
    for i in range(1,len(A)):
        op=list(A[i])
        j=0
        while j<min(len(ot),len(op)):
            if ot[j]!=op[j]:
                ot=ot[:j]
                break
            print(ot)
            j+=1
    return ''.join(ot)
A=input()
print(lp(A))

