def Remove_i(str,n):
    new_str=''
    for i in range(len(str)):
        if i!=n:
            new_str+=str[i]
    print(new_str)
str=input()
n=int(input())
Remove_i(str,n)