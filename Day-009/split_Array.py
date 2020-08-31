def Array_Split(arr,N,k):
    A=[0]*N
    for i in range(N):
        if i<k:
            A[N-(k-i)]=arr[i]
        else:
            A[i-k]=arr[i]
    print(*A)

arr=[int(x) for x in input().split()]
position=int(input())
Array_Split(arr,len(arr),position)