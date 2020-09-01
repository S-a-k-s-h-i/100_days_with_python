def ArrayMultiplication(arr,n):
    mul=1
    for i in arr:
        mul*=i
    return mul%n

arr=[int(x) for x in input().split()]
n=int(input())
print(ArrayMultiplication(arr,n))