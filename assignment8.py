#to import random and time modules
import random, time

#defining the function randomword
def randomWord():
    #giving the list of words
    listOfWords=['Georgian','college','for','is']
    randomIndex=random.randint(0,3)
    #to give a random word from the list
    givenRandomWord=listOfWords[randomIndex]
    #to print the content
    print(givenRandomWord)
    #to return the random word
    return givenRandomWord

#defining a function to search the file
def searchTextFile(stringArg):
    #opening the text file
    openTextFile=open('c:\\python\\assignment8.txt')
    #reading ther text file
    textFileContent=openTextFile.read()
    #defining the occurances globally
    occurances= textFileContent.count(stringArg)
    #closing the text file
    openTextFile.close()
    #to check the number of occurances
    if occurances == 0:
        #return the value
        return 'total number of occurance of the random word is none that is ' + str(occurances)
    #to check the number of occurances
    elif occurances>0 and occurances<6:
        #return the value
        return 'total number of occurance of the random word is low that is ' + str(occurances)
    #to check the number of occurances
    elif occurances>5 and occurances <11:
        #return the value
        return 'total number of occurance of the random word is medium that is ' + str(occurances)
    #to check the number of occurances
    elif occurances >= 11:
        #return the value
        return 'total number of occurance of the random word is high that is' + str(occurances)
        

#calling the function to generate a random word from the list
randomWordFromList= randomWord()
#starting the time to get time stamp
startTime=time.time()
#callin the function to search the word
numberOfOccurances=searchTextFile(randomWordFromList)
for i in range (1,10000):
    q=6
#ending the time to get time stamp
endTime=time.time()
#to get the elapsed time
elapsedTime=str(endTime-startTime)
#printing the content
print("time elapsed to check the " + str(randomWordFromList) + " in the text file is " + elapsedTime + " and the word occured " + str(numberOfOccurances))



