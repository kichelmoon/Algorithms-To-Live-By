import random

print("The Secretary Problem")

secretaries = []
number_of_applicants = random.randint(10, 100)

print ("There are " + str(number_of_applicants) + " applicants.")

skill_range = random.randint(1, 100)
for i in range(number_of_applicants):
    secretaries.append(random.randrange(skill_range))

applicant_hired = False
secretary_skill = 0

while applicant_hired == False:
    applicant = random.choice(secretaries)
    print("Applicant skill level: " + str(applicant))
    
    hire = input("Hire applicant? (Y/N)")
    if hire == "Y" or hire == "y":
        print("Hired!")
        applicant_hired = True
        secretary_skill = applicant
    else:
        secretaries.remove(applicant)
        if not secretaries:
            print ("No more applicants, hired the last one")
            applicant_hired = True
            secretary_skill = applicant

print ("Your secretary has a skill level of " + str(secretary_skill) + " out of a maximum of " + str(skill_range) + ".")
