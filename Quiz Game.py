print("Welcome to my quiz game!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")
Score = 0

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Congratulations!, you are correct")
    Score += 1

else:
    print("Oops, you are wrong mate, try again")

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Congratulations!, you are correct")
    Score += 1

else:
    print("Oops, you are wrong mate, try again")

answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Congratulations!, you are correct")
    Score += 1

else:
    print("Oops, you are wrong mate, try again")

answer = input("What does PSU stand for? ").lower()

if answer == "power supply unit":
    print("Congratulations!, you are correct")
    Score += 1

else:
    print("Oops, you are wrong mate, try again")

print(f"You got {Score} questions correct, thank you for playing")
print("You got " + str((Score / 4) * 100) + "%.")