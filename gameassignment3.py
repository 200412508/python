#to import the random class
import random
#to import the sys class
import sys
#to select a random numbers by computer
randomNumber=(random.randint(1,500))
#to display the random number on screen
print(randomNumber)
#assignment of round number
roundNumber=1
#assignment of guess number
guess=1
#assigining total number of guesses to find out the used number
usedGuess=4
#initialte while loop[   
while(roundNumber<=4):
    #initiatiate for loop with range
    for guess in range(3,0,-1):
        #print the statement
        print("guess the random number")
        #print the statement
        print("you are in round " +str(roundNumber) + " and you have " + str(guess) + " guess available")
        #to ask the input from user
        userRandomNumber=input()
        #to assign the new random number
        userRandomNumber=int(userRandomNumber)
        #initiate the if statement
        if(userRandomNumber<randomNumber):
            #print the statement
            print("the number is low")
        #check other condition
        elif(userRandomNumber>randomNumber):
            #print the statement
            print("the number is high")
        #check other condition
        elif(userRandomNumber==randomNumber):
            #print the statement
            print("you have guessed the correct number")
            #print the statement
            print("you have used " + str(roundNumber) + " rounds")
            #print the statement 
            print("you have used " + str(usedGuess - guess) + " guesses")
            #to exit the code
            sys.exit()
        #incrementing guess    
        guess=guess+1
    #to check the guess
    if(guess==3):
        #Break the loop
        break
    #increasing the roundNumber   
    roundNumber=roundNumber+1
    #to check the statement
    if(roundNumber==5):
        #to break the loop
        break
#to print the correct number
print("The correct number is " +str(randomNumber))
#print the statement
print("you have used 4 rounds")
#print the statement 
print("you have used 12 guesses")
            














































#while(guessedNumber != randomNumber):

    #for roundNumber in range(1,5,1):
        #print("you are in round " +char(roundNumber)
        

    #print (roundNumber)
        #for guess in range(1,4):
    #print (guess)
    
    #guess = guess + 1
    #if(guess == 3):
        #roundNumber = roundNumber + 1
        #print("you are in round " + str(roundNumber))
        
    
