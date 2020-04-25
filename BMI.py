import sys
from bloodP import Info
#from age import body
def health():
    height1=float(input("enter your height in feet : "))
    weight=float(input("enter your weight in kg:  "))
    height=0.3048*height1
    bmi=weight / (height * height)
    print("your Body Mass Index(BMI) is: ",round(bmi,2))
    if bmi<=18.5:
        print("your weight very low!! you must increase your weight to be healthy ")
    elif bmi>18.5 and bmi<24.9:
        print("you have a good weight. maintain it to be healthy")
    elif bmi>25 and bmi<29.9:
        print("you are over-weighted. need to control the further increase in weight")
    else:
        print("DANGER!! you are highly obesed. need to immediately reduce your weight")
#health()
def out():
    ch=int(input("press 1 to calculate another health statistics \n"+ "press 2. to calculate the age difference.\n" + "press 3. to exit \n"))
    if ch==1:
        health()
        #body()
        Info()
    elif ch==2:
        from difference import diff
        diff()
    else:
        sys.exit()
   
