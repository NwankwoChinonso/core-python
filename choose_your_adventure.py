name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
        "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across.: ")
    
    if answer == "swim":
        answer = input("You swam aross and got eaten by a crocodile. Do you want the crocodile to spit out your carccass or swallow everything? (spit out/swallow) ")
        if answer == "spit out":
            print("The Croc spat you out, and the fishes did the rest")
        else:
            print("The Croc still spat you out because you taste bitter!! haha")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option, You lose.")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back to the main road. Now you can decide to drive to the left or right.")
    elif answer == "cross":
        answer =input("You crossed the bridge, but your phone fell in the water, you dived in to retrieve it, and three sharks come round, what do you do? (play dead or swim away?) ")

        if answer == "swim away":
            print("You are lucky, you got away, but you did not get the phone. YOU WIN")
        elif answer == "play dead":
            print("Your dumb ass got eaten by them sharks, because they can sense your body heat.")
        else:
            print("Not a valid option, You lose.")

    else:
        print("Not a valid option, You lose.")

else:
    print("Not a valid option. You lose.") 

print(f'Thank you for trying {name}')