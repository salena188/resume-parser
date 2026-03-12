#check the eligibility 

# name =input("Enter your name")
# experience = int(input("Enter your years of experience"))

# if experience >= 5:
#    print(name, "is eligible for Senior Developer role")
# else:
#    print(name, "is eligible for Junior Developer role")


def check_role():
    name = input("Enter your name: ")
    experience = int(input("Enter your years of experience: "))

    if experience >= 5:
        print(name, "is eligible for Senior Developer role")
    else:
        print(name, "is eligible for Junior Developer role")

# calling the function
check_role()