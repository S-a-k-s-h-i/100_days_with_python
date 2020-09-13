def Reverse(sen):
    sen=sen.split()
    rev=' '.join(reversed(sen))
    print(rev)

sentence=input()
Reverse(sentence)