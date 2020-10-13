def Merge(d1,d2):
    Md={**d1,**d2}
    print(Md)

dict1=dict()
dict2=dict()
n1=int(input('Length of dictionary1 '))
n2=int(input('length of dictionary2 '))
for i in range(n1):
    data=input().split(' ')
    dict1[data[0]]=int(data[1])
print('dictionary1 = ',dict1)
for i in range(n2):
    data=input().split(' ')
    dict2[data[0]]=int(data[1])
print('dictionary2 = ',dict2)
Merge(dict1,dict2)
