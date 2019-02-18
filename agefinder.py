 
birth_yr=input("Please Enter your year of birth: ")
def current_age(birth_yr):
    current_age = 2019-int(birth_yr)
   

    if current_age<18:
        print("You are a minor")
    elif current_age<36:
        print("You are a youth")
    else:
        print ("you are an elder")

current_age(birth_yr)