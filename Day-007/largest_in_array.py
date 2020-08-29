def Max_in_Array(arr):
    M=arr[0]
    for i in range(1,len(arr)):
        if M<arr[i]:
            M=arr[i]
    return M


array=[int(x) for x in input().split()]
print(Max_in_Array(array))