def Even_List(lst):
    l=[]
    for i in range(len(lst)):
        if lst[i]%2==0:
            l.append(lst[i])
    print(l)

lst=[int(x) for x in input().split()]
Even_List(lst)