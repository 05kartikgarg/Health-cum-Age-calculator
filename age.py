from datetime import datetime
from BMI import health
import time
from bloodP import Info
from BMI import out

print("                     WELCOME!! TO THE AGE CUM HEALTH CALCULATOR                     ")
name=str(input("enter your name \n"))
dob = input("Enter DOB, use dd mm yyyy format: ")
dob = datetime.strptime(dob, '%d %m %Y')
age= int((datetime.today()-dob).days/365)
print("Hello, "+ name +" choose from the following services \n")

def body():
    if age<2:
        print("normal body tempreture range is: 94.5-99.1 °F")
    elif age>2 and age<11:
        print("normal body tempreture range is: 96.6-98.0 °F")
    elif age>11 and age<65:
        print("normal body tempreture range is:  95.3-98.4 °F")
    else:
        print("normal body tempreture range is:  96.0-97.4 °F")

def timed():
    print("Here are your age statistics...")
    time.sleep(1)
    print ("Years : %d" % ((datetime.today()- dob).days/365))
    print ("Months : %d" % ((datetime.today() - dob).days/30.4))
    print("Weeks : %d"%((datetime.today()-dob ).days/7))
    print("Days: %d"%((datetime.today()-dob ).days))
    print ("Hours : %d" % ((datetime.today() - dob).days*24))
    print ("Minutes : %d" % ((datetime.today() - dob).days*1440))
    print ("Seconds : %d" % ((datetime.today() - dob).days*86400))
    #health()
    p = int(input("enter 1 for calculating another age statistics \nenter 2 to view health statistics \n"+"enter 3. to calculate age difference \nenter 4 to exit \n"))
    if p==1:
            kr()
    elif p==2:
            body()
            health()
            Info()
            out()
    elif p==3:
            from difference import diff
            diff()

        
    else: ex()

def ex():
        print("thanks for giving your precious time")
       # sys.exit()5
        
def kr():
        timed()
#timed()




















