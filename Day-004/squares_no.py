def Sum_of_Squares(number):
    sum=0
    for n in range(1,number+1):
        sum+=pow(n,2)
    return sum
print(Sum_of_Squares(int(input())))
