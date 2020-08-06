import random

print("The Secretary Problem")

secretaries = []
number_of_applicants = random.randint(10, 100)

print ("There are " + str(number_of_applicants) + " applicants.")

skill_range = random.randint(1, 100)
for i in range(number_of_applicants):
    secretaries.append(random.randrange(skill_range))

secretaries_copy = secretaries.copy()

applicant_hired = False
secretary_skill = 0

while applicant_hired == False:
    applicant = random.choice(secretaries)
    secretaries.remove(applicant)

    print("Applicant skill level: " + str(applicant))
    
    hire = input("Hire applicant? (Y/N)")
    if hire == "Y" or hire == "y":
        print("Hired!")
        applicant_hired = True
        secretary_skill = applicant
    else:
        if not secretaries:
            print ("No more applicants, hired the last one")
            applicant_hired = True
            secretary_skill = applicant

print ("Your secretary has a skill level of " + str(secretary_skill) + " out of a maximum of " + str(skill_range) + ".")

applicant_hired = False
secretary_skill = 0
skill_baseline = 0

while applicant_hired == False:
    applicant = random.choice(secretaries_copy)
    secretaries_copy.remove(applicant)
    if len(secretaries_copy) / number_of_applicants * 100 > 63:
        if applicant > skill_baseline:
            skill_baseline = applicant
            print("New baseline: " + str(skill_baseline))
    else:
        if applicant > skill_baseline or not secretaries_copy:
            applicant_hired = True
            secretary_skill = applicant
        

print ("The computer's secretary has a skill level of " + str(secretary_skill) + " out of a maximum of " + str(skill_range) + ".")
