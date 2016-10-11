# Ryan Ge
# October 5, 2016
# Play a guessing game

def game():
    import random
    number = random.randint(1,100)

    tries = 0

    while True:
        while True:
            guess = int(input("Give a guess between 1 and 100:"))
            if guess <= 100 and guess >= 1:
                break

        if guess < number:
            print("The number is too low.")
            tries += 1
        elif guess > number:
            print("The number is too high.")
            tries += 1

        else:
            tries += 1
            print("Congratulations! You got the right answer!")
            print("You tried", tries, "time(s).")
            break


def main():
    while True:
        answer = input("Do you want to play? (Y/N)")
        if answer == "Y":
            play = True

        elif answer == "N":
            play = False


        if play:
            game()
            main()
        else:
            print("Thanks for playing. Goodbye!")
            break

main()


