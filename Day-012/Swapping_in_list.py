def Swap(l,pos1,pos2):
    l[pos1],l[pos2]=l[pos2],l[pos1]
    print(l)

l=[int(x) for x in input().split()]
pos1=int(input())
pos2=int(input())
Swap(l,pos1-1,pos2-1)