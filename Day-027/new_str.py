def Even_String(s):
    s=s.split()
    for i in range(len(s)):
        if len(s[i])%2==0:
            print(s[i])
str=input()
Even_String(str)