def reverse(A):
    if A==0:
        return 0
    y=bin(A)
    m='0000000000000000000000000000000000'
    n=len(y)
    m=m[n:]
    y=y[::-1]
    return int(y+m,2)
    # l=[]
    # while A:
    #     n=A%2
    #     l.append(n)
    #     A=A//2
    # n=len(l)
    # for i in range(n,32):
    #        l.append(0)
    # sum,i=0,0
    # l=l[::-1]
    # while i<32:
    #     sum+=l[i]*pow(2,i)
    #     i+=1
    # return sum
print(reverse(3))