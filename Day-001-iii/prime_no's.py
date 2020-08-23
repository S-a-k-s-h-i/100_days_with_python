def Prime_no(start,end):
    for n in range(start,end):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n,end=' ')
lst=[]
start,end=input().split()
Prime_no(int(start),int(end))