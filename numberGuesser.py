from random import randint

#user changeable parameters to change game difficulty.
#Edit the integer values alone as declaring it witout 'int()' will cause an error (randint parameters HAVE to be integer variables, NOT strings)
minInt = int(1)
maxInt = int(10)
maxChance = 5

#variables for the game
number = randint(minInt,maxInt)
guess = None
chances = 0

#pre-game instructions
print("In this game, you have to guess the integer from ",minInt, "to ",maxInt," picked at random.")
print("You have a maximum of",maxChance,"chances to do so.")
print("To change the number of chances and randint values, check the source code.")
print("")
print("P.S. If you type anything other than integers, the game will exit...")
print("so maybe don't do that")
print("")
print("Happy gaming!")
print("")

#actual game code
while chances <= maxChance:
    guess = input("Pick a number between 1 and 10 : ")
    guess = int(guess)

    if guess < number:
        print("The number is higher than ",guess,"! Try again")
        chances+=1
    if guess > number:
        print("The number is lower than ",guess,"! Try again")
        chances+=1
    if guess == number:
        print("Yes! The number was ",number,"! You won! Press 'enter' to exit")
        guess = input("")
    if guess == '':
        break

if not chances <= maxChance:
    print("You have run out of your 5 chances!! The number was : ",number,"! Press 'enter' to exit")