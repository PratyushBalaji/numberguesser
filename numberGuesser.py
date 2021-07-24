from random import randint
import colorama
from colorama import Fore,Back
colorama.init()

def startGame():

    #intro questions for users to set parameters instead of opening source code to edit
    setMin = int(input("What should the smallest number on the scale be? "))
    setMax = int(input("What should the largest number on the scale be? "))
    setChances = int(input("How many chances would you like? "))
    lives = setChances

    #variables for the game
    number = randint(setMin,setMax)
    chances = 0

    #pre-game instructions
    print(Fore.WHITE+"")
    print("")
    print("In this game, you have to guess the integer from ",setMin, "to ",setMax," picked at random.")
    print("You have a maximum of",setChances,"chances to do so.")
    print("")
    print("P.S. If you type anything other than integers, the game will exit...")
    print("")
    print("Happy gaming!")
    print("")

    playing = True

    while playing:
    #actual game code
        while chances <= lives-1:
            guess = input("Pick a number between the numbers you chose - ")
            guess = int(guess)

            if guess < number:
                print("The number is higher than ",guess,"! Try again")
                chances+=1
            if guess > number:
                print("The number is lower than ",guess,"! Try again")
                chances+=1
            if guess == number:
                print("")
                print(Fore.GREEN+"Yes! The number was",number,Fore.GREEN+"! You Won!")
                print("")
                choice = input("Would you like to play again? y/n : ")
                if choice.lower() == "n":
                    print("Thanks for playing!")
                    input()
                    playing = False
                elif choice.lower() == 'y':
                    print("Lets play again!")
                    startGame()
            if guess == 'quit' or guess == '':
                quit()

        if not chances <= lives-1:
            print("")
            print(Fore.RED+"You have run out of chances!! The number was :",number)
            print(Fore.WHITE+"")
            choice = input("Would you like to play again? y/n : ")
            if choice.lower() == "n":
                print("Thanks for playing!")
                input()
                playing = False
            elif choice.lower() == 'y':
                print("Lets play again!")
                startGame()

startGame()
