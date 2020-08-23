def fibonacci(number):
    a=0
    b=1
    if number<0:
        print('Incorrect input')
    elif number==1:
        return a
    elif number==2:
        return b
    else:
        for i in range(2,number):
            c = a + b
            a=b
            b=c
        return b

#Using Recursion
# def fibonacci(number):
#     a=0
#     b=1
#     if number<0:
#         print('Incorrect input')
#     elif number==1:
#         return a
#     elif number==2:
#         return b
#     else:
#         return fibonacci(number-1)+fibonacci(number-2)
n=int(input())
print(fibonacci(n+1))