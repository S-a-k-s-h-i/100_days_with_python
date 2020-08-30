def Array_Rotation(A,d,n):
    arr=[0]*n
    for i in range(n):
        if i<d:
            arr[n-(d-i)]=A[i]
        else:
            arr[i-d]=A[i]
    print(*arr)

array=[int(x) for x in input().split()]
N=int(input())
Array_Rotation(array,N,len(array))