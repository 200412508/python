# import random is used to select any random number
import random

#randint() function selects the random number from range 1 to 500
valcom = random.randint(1,500)
print(valcom)

#range is used to specify the range of between 1 to 4 rounds
for rounds in range(1,5):

    #print() is used to display the arguments that inside of parenthesis 
    print("Guess a number")

    #for with range used to iterate the loop over a section of code for specific time of numbers
    for guessNum in range(1,4):

        
        #innput is used to captures informations from keyboard in the string format.
        guess = int(input())

        #if used to start the section of code
        if guess < valcom:

            #print() is used to display the arguments that inside of parenthesis 
            print("Value is too low")
            #print() is used to display the arguments that inside of parenthesis 
            print("Guesses are reamining: " , int(3 - guessNum))
            #print() is used to display the arguments that inside of parenthesis 
            print("Rounds are remaining: ", int(4 - rounds))
            
        #elif used to compare one or more conditions
        elif guess > valcom:
            #print() is used to display the arguments that inside of parenthesis 
            print("Value is too high")
            #print() is used to display the arguments that inside of parenthesis
            print("Guesses are reamining: " , int(3 - guessNum))
            #print() is used to display the arguments that inside of parenthesis 
            print("Rounds are remaining: ", int(4 - rounds))
            
        #elif used to compare one or more conditions
        elif guess == valcom:

           #print() is used to display the arguments that inside of parenthesis 
            print("Congoratulations, You guess correctly")

else:
    #print() is used to display the arguments that inside of parenthesis 
    print(" The Selected num is : ", valcom)
    #print() is used to display the arguments that inside of parenthesis 
    print(" The Successful rounda are 12")
    #print() is used to display the arguments that inside of parenthesis s
    print(" You have successful tries are 4")
