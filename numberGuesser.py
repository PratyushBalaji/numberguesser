from random import randint

#intro questions for users to set parameters instead of opening source code to edit
setMin = int(input("What should the smallest number on the scale be? "))
setMax = int(input("What should the largest number on the scale be? "))
setChances = int(input("How many chances would you like? "))

#variables for the game
number = randint(setMin,setMax)
chances = 0

#pre-game instructions
print("")
print("")
print("In this game, you have to guess the integer from ",setMin, "to ",setMax," picked at random.")
print("You have a maximum of",setChances,"chances to do so.")
print("")
print("P.S. If you type anything other than integers, the game will exit...")
print("")
print("Happy gaming!")
print("")


#actual game code
while chances <= setChances:
    guess = input("Pick a number between the numbers you chose - ")
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

if not chances <= setChances:
    print("You have run out of your 5 chances!! The number was : ",number,"! Press 'enter' to exit")
