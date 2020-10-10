def sumValuesInDictionary(d):
    sum=0
    for val in d.values():
        sum+=val
    return sum

d=dict()
n=int(input())
for i in range(n):
    data=input().split(' ')
    d[data[0]]=int(data[1])
print(sumValuesInDictionary(d))