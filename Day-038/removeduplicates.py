def removeDuplicates(str):
    result=''
    for i in str:
        if i not in result:
            result+=i
    return result
str=input()
print(removeDuplicates(str))