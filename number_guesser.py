import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
    
else:
    print("Please enter a number")

random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Please enter a number")
        continue

    if user_guess == random_number:
        print(f"Congratulations!, your guess is in order, you guessed {guesses} times.")
        break

    elif user_guess > random_number:
            print("That's wrong, your guess is above the number, try again.")
    else:
        print("That's wrong, your guess is below the number, try again")
            
        