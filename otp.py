from random import *

def otp_6_int():
    ''' The Function prints a single 6 digit random otp for general use ''' 
    global otp
    otp=''
    for x in range(6):
        otp=otp+str((randint(0,9)))

def otp_6_alnum():
    ''' The Functon prints a 6 digit alpha numric otp with number and character alternatievly '''
    global otp
    otp=''
    for x in range(1,7):
        if x%2!=0:
            otp=otp+chr(randint(65,65+25))
        else:
            otp=otp+str(randint(0,9))

def choose():
    ch=input("  Enter 'Y' or 'N' to generate again : ").lower()
    if ch=='y':
        return True
    elif ch=='n':
        print('  Thank you for using the application.\n Have a Nice day!!..')
        return False
    else:
        print('  Not a valid choice!!..\n  Thank you for using the application.\n  Have a Nice day!!..')
    
def main():
    print('What kind of OTP you want to generate.')
    while True:
        print("Enter '1' for numeric OTP and '2' for alphanumeric OTP '3' to Cancel : ", end='')
        choice=eval(input())
        if choice==1:
            otp_6_int()
            otp1=otp[::]
            print('Your new 6 digit Numeric otp is      :',otp1)
            if choose()==True:
                continue
            else:
                break

        elif choice==2:
            otp_6_alnum()
            otp2=otp[::]
            print('Your new 6 digit Alphanumric otp is  :',otp2)
            if choose()==True:
                continue
            else:
                break

        elif choice==3:
            print('  Thank you for using the application.\n Have a Nice day!!..')
            break
            
        else:
            print('  Please enter a valid Choice!!..')
otp=''
if __name__ == '__main__':
    main()
