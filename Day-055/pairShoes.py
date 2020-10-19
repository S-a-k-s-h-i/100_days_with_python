color_ar=list(map(int,input().split(' ')))
print(color_ar)
i,pairs=0,0
while i<len(color_ar)-1:
    if color_ar[i]==color_ar[i+1]:
        pairs+=1
        i+=2
    else:
        i+=1
print(pairs)


