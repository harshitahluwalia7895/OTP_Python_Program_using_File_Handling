from random import *
ch = 'y'
while ch == 'y':
    m=int(input('Enter your Number:'))
    n=str(randint(1000,2000))
    f=open('newFile.txt','w')
    f.write(n)
    f.close()
    f=open('newFile.txt','r')
    data=f.read()
    print('YOur OTP has been Sended to newFile.txt')
    OTP=int(input('Enter the OTP:'))
    if(data==n):
        print('Payment Seccessful')
    else:
        print('Try Again')
    ch = input("Do you want to do more conversions?? y//n: ")
print('THankyou!!!')
f.close()