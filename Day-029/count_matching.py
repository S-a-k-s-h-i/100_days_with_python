def Count_Matching(s1,s2):
    lst=[]
    count=0
    for i in s1:
        for j in s2:
            if i==j and i not in lst:
                lst.append(i)
                break
    print(len(lst))
str1=input("str1 = ")
str2=input("str2 = ")
Count_Matching(str1,str2)