age = 15
def userAge(age):
    if(age<13):
        print("User is child")
    elif(age>13 and age <=19):
        print("user is teenage")
    elif(age>20 and age <=59):
        print("user is adult")
    else:
        print("user is senior")

userAge(age)