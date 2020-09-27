def remove_i(str,i):
    result=''
    for n in range(len(str)):
        if i!=n:
            result+=str[n]
    return result

str=input()
i=int(input())
print(remove_i(str,i))
