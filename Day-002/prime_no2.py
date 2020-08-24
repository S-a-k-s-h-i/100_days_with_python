def Prime_no(number):
    if number>1:
        for n in range(2,number):
            if number%n==0:
              break
        if n+1==number:
             print('True')
        else:
             print('False')
    else:
        print('False')
Prime_no(int(input()))