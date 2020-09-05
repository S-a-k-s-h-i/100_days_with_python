def Sum_of_List(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum

lst=[int(x) for x in input().split()]
print(Sum_of_List(lst))