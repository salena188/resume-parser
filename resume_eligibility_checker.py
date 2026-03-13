#check the eligibility 

def resume_eligibilie():
    name = input("Enter your name: ")
    experience = int(input("Enter your years of experience: "))

    if experience >= 5:
        print(name, "is eligible for Senior Developer role")
    elif experience >=2 :
        print(name, "is eligible for Mid Developer role")
    else:
        print(name, "is eligible for Junior Developer role")

# calling the function
resume_eligibilie()