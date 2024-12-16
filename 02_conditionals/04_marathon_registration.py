# Problem: Determine if someone is eligible to register for a marathon. Criteria: Must be 18 or older **and** either a resident of the city **or** have a medical clearance.

athlete_age=int(input("How old are You?  "))
is_resident= input("Are you a resident? (yes/no):").strip().lower()=="yes"
is_medically_clear= input("Are you medically clear? (yes/no): ").strip().lower()=="yes"

if athlete_age >=18 and (is_resident or is_medically_clear):
    print("Congratulations..!! you are eligible to register for the Marathon.")
else:
    print("Ooops you are not eligible to participate in the Marathon")