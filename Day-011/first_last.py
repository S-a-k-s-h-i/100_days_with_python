def First_Last(l):
    l[0],l[len(l)-1]=l[len(l)-1],l[0]
    print(l)

l=[int(x) for x in input().split()]
First_Last(l)