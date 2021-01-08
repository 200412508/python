#to import random and sys class
import random, sys


#defining my own function with two parameters
def randomNumberGenerator(giveAString, giveAInt):
    #assigning the length of string
    lengthOfString = len(giveAString)
    #assigning multiplied number
    multipliedNumber = lengthOfString*giveAInt
    #assigning random value with rand function
    randomValue = random.randint(1,multipliedNumber)
    #returing the random value

    return randomValue
#print the statement
print("firstName", "lastName", "randomString", "randomInteger") 
#input from user
firstName = input()
#input from user
lastName = input()
#input from user
randomString = input()
#input from user
randomInteger = input()
#to check for 0
while(int(randomInteger)==0):
    #print the statement
    print("give other number than 0")
    #input from user
    randomInteger = input()
    #loop when not equal to 0
    while(int(randomInteger) != 0):
        #print both the strings
        print(firstName + lastName)
        #print multiplies value 
        print(firstName * int(randomInteger))
        #using for to get range of number
        for count in range (20,-2,-2):
            #print the range of numbers
            print(count)
        #to print the statement    
        print(firstName,lastName,sep='---')
        #assigning random number function 
        randomNumber=randomNumberGenerator(randomString,int(randomInteger))
        #print random number
        print(randomNumber)
        #to end the code
        sys.exit()
