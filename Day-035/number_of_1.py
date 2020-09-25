def numSetBits(A):
    l = []
    while A:
        n = A % 2
        print(n)
        l.append(n)
        A=A//2
    return l.count(1)
no=int(input())
print(numSetBits(no))
