#check the eligibility 

"""
Program: check the eligibility
Author: Salina Shrestha
Date: 11 March 2026
Description: This program check the eligibility.
"""
name =input("Enter your name")
experience = int(input("Enter your years of experience"))

if experience >= 5:
   print(name, "is eligible for Senior Developer role")
else:
   print(name, "is eligible for Junior Developer role")
