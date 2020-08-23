number=int(input("Enter the no: "))
test=number
sum=0
while test:
    n=test%10
    sum=sum+pow(n,3)
    test=test//10
if sum==number:
    print("{} is an Armstrong no".format(number))
else:
    print("{} is not an Armstrong no".format(number))