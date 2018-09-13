from random import *

def otp_6_int():
    ''' The Function prints a single 6 digit random otp for general use ''' 
    global otp
    otp=''
    for x in range(6):
        otp=otp+str((randint(0,9)))
    disp()

def otp_6_alnum():
    ''' The Functon prints a 6 digit alpha numric otp with number and character alternatievly '''
    global otp
    otp=''
    for x in range(1,7):
        if x%2!=0:
            otp=otp+chr(randint(65,65+25))
        else:
            otp=otp+str(randint(0,9))
    disp()

def disp():
    ''' To display the otp to the Console '''
    global otp
    print(otp)

otp=''
otp_6_int()
otp_6_int=otp[::]
otp_6_alnum()
otp_6_alnum=otp[::]
print('Your new 6 digit integer otp is : ',otp_6_int)
print('Your new 6 digit Alphanumric otp is : ',otp_6_alnum)