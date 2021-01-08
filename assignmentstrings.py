"""#to print the statement in the paranthesis
print("give input as a 5 word long sentence")
#to take input
inputString=input()
#to know the length of the string
lenghtOfInputString=len(inputString)
#print the length od the sentence
print("the number of characters in your sentence is :",lenghtOfInputString)
#print the 5th character of the sentence
print("the 5th character of the sentence is :",inputString[4])
#3rd to 7th characters of the sentence
print("3rd to 7th characters of the sentence are:",inputString[2:7])
#to check weather sentence contains hello
print('hello' in inputString , " that the input senetence entered contains hello") 
#to print in upper letters
print(inputString.upper())
#to check if the sentence start with hello
print(inputString.startswith('hello') , " that the input sentence starts with hello")
#to print righ justifies
print(inputString.rjust(30))"""


#defining a function
def stringReverse(reverseString):
    #to get the total number of indices
    totalIndices = len(reverseString)-1 
    #defining a null string
    nullString = ""
    #for loop to reverse the string
    for numberOfCharacters in range (1,len(reverseString)+1):
        #to reverse the string
        nullString = nullString + reverseString[totalIndices]
        #to get the count of last character
        totalIndices = totalIndices - 1
    #to return the reversed string
    return nullString

#calling the reversal function
print(stringReverse("hello"))
    
    
