
name=str(input("emter your name: "))
foi= input("enter your field of interest :")
grad= input(str("are you graduated ?"))
age=int(input("enter your age: "))
gpa=float(input("enter your GPA: "))

if age > 25 and gpa >= 3.5 and grad==True :
    print("you are eligible for scholarship")
elif age < 30 and gpa > 2.5 :
    print ("you are eligeble for internship .")
else : 
    print("you are not eligible, try to apply later")








#   >  <  ≥