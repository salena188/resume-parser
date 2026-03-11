#Resume Skill Level Classifier
#User enters number of skills.
skills = int(input("How many programming skills do you know? "))
if skills >= 5:
   print("Strong Developer Profile")
elif skills >= 3:
   print("Average Developer Profile")
else:
   print("Beginner Developer")