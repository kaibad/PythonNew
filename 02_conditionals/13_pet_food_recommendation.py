# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
pets=["dog","cat"]
print("We Recommend food for")
for pet in pets:
    print(pet)

pet_species=input("Mention the type of Pet's Species you have: ")

if pet_species not in pets:
    print("Sorry we donot recommend food for this pet species")
else:
    pets_age = int(input("Also write the age of your pet: "))
    
    if pet_species == "dog":
        if pets_age <= 2:
           food="Puppy food"
        else:
            food="Adult dog food"
    if pet_species=="cat":
        if pets_age<=5:
            food="Kitten food"
        else:
            foof="Senior cat food"

print(f"The food we recommend for to lovely pet is '{food}'" )