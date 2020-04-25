from datetime import datetime
import time

def diff():
    print ("current date and time  ",datetime.today())
    a=str(input("enter your name \n"))
    print("enter your date of birth ")
    dob = input("Enter DOB, use dd mm yyyy format: ")
    dob = datetime.strptime(dob, '%d %m %Y')
    print(dob)
    b=str(input("enter your name \n"))
    print("enter other date of birth ")
    xyz = input("Enter DOB, use dd mm yyyy format: ")
    xyz = datetime.strptime(xyz, '%d %m %Y')
    print(xyz)
   # print(datetime.day(11,04,2000))
    c =xyz-dob
    ''' print("years ",c/365)
    print("month ",c/30.4)
    print("weeks",c/7)
    '''
    if xyz>dob:
        print(" ",a+ " is older by " ,c)
    else:
        print(" ",b+ " is older by " ,c)
    print("age difference is ",c)

#diff()
    
