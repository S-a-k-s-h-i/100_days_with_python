def Vowel_Str(st):
    s=set({})
    vowels=set('aeiou')
    for i in st:
        if i in vowels:
            s.add(i)
    if len(s)==len(vowels):
        print('Accepted')
    else:
        print('Not Accepted')
str=input()
Vowel_Str(str)