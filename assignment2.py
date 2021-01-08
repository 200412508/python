#ask the user to type
print("enter a sentence")
#to take input from user
typeASentence = input()
#to determine the number of characters in the sentence
print(len(typeASentence))
#to ask the user to give a input number between 1 and number of characters
print("enter between 1 and " + str(len(typeASentence)))
lenghtOfSentence = len(typeASentence)
#record the value given by the user
number = input()
#conditon to check the given number
if int(number) == lenghtOfSentence:
    #displays the string)
    print("the number you provided " + number + " was equal to the number of characters in the sentence")
#checks the other condition if the
elif int(number) < lenghtOfSentence:
    #displays the string
    print("the number you provided " + number + " was less than the number of characters in the sentence")
#checks the other condition
elif int(number) > lenghtOfSentence:
    #displays the string
    print("the number you provided " + number + " was greater than the number of characters in the sentence")
#to generate loop till you get the correct value
while int(number) != lenghtOfSentence:
    #to display the string
    print("enter the correct value")
    #to take input from the user
    number = input()
    #checks the condition
    if int(number) == lenghtOfSentence:
        #to display the string
        print("the number you provided " + number + " was equal to the number of characters in the sentence")
    #checks the other condition
    elif int(number) < lenghtOfSentence:
        #to display the string
        print("the number you provided " + number + " was less than the number of characters in the sentence")
    #checks the other condition
    elif int(number) > lenghtOfSentence:
        #to display the string
        print("the number you provided " + number + " was greater than the number of characters in the sentence")
    
