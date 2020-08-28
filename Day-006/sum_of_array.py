def Sum_of_Array(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

array=[int(x) for x in input().split()]
print(Sum_of_Array(array))

