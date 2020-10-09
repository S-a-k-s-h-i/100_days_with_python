d=dict()
n=int(input())
for i in range(n):
    data=list(input().split())
    d[data[0]]=[int(i) for i in data[1:]]
uniqueValue=list(sorted({j for i in d.values() for j in i}))
print(uniqueValue)