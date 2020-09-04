def count_x(lst, x):
    count = 0
    for i in lst:
        if (i == x):
            count = count + 1
    return count


# Driver Code
lst = [int(x) for x in input().split()]
x = int(input())
print(count_x(lst,x))
