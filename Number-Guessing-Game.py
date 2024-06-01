import random
name = input("May I ask for ur name?\n")
number = random.randint(1,200)
print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
print("Go ahead. Guess!")
def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def game():
    guessesTaken=6
    while guessesTaken !=0:
        guess = get_valid_number("Enter your guess: ")
        if guess<=0 or guess>200:
            print("Silly Goose! That number isn't in the range!\nPlease enter a number between 1 and 200")
            continue
        if guess < number:
            print("The guess of the number that you have entered is too low\nTry Again!")
            guessesTaken-=1
        elif guess > number:
              print("The guess of the number that you have entered is too high\nTry Again!")
              guessesTaken-=1
        elif guess==number:
              print("You Won")
              exit()
        else:
            return
        while guessesTaken==0 and guess!=number:
            print("Nope. The number I was thinking of was", + number)
            break
        while guess!=number and guessesTaken==0:
            play_again = input("Do you want to play again?")
            if play_again.lower() == "no":
                break
            if play_again.lower() == "yes" or "y":
                name = input("May I ask for ur name?\n")
                print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
                print("Go ahead. Guess!")
                game()
        

game()
