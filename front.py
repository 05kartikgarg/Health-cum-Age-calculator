from age import timed
from BMI import health
from difference import diff
from BMI import out
from age import body
from bloodP import Info

#print("                     WELCOME!! TO THE AGE CUM HEALTH CALCULATOR                     ")
#print("choose from the following services \n")
print("1. Age calculator\n"+"2.health predictor \n"+"3.compare age of two \n")
c=int(input(" "))
if c==1:
    timed()
elif c==2:
    health()
    body()
    Info()
    out()
elif c==3:
    diff()
else:
    print("invalid option................")

