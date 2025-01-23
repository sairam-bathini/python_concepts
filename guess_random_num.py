import random

number_to_guess = random.randint(1, 100)
attempts = 0

print("Namaste Kaka to Guessing Game")
print("Nenu eppudu oka number korukunna adhi entido jara cheppu Kaka?")

while True:
    guess = int(input("Guess cheyara bhai: "))
    attempts= +1

    if guess < number_to_guess:
        print("Chaana thakkuva Malli try chey!")
    elif guess > number_to_guess:
        print("Antha Kadu Bhai Malli try chey!")
    else:
        print(f"Super kaka! Bale guess chesinav {attempts} attempts la.")
