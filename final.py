import random
import time
import datetime
import sys

def functionOne(stringOne,stringTwo,stringThree):
    stringOneLength=len(stringOne)
    stringTwoLength=len(stringTwo)
    stringThreeLength=len(stringThree)
    if stringTwoLength-stringOneLength==3 and stringThreeLength-stringTwoLength==3:
        return "string 3 > 2 by 3 char and string 2 is greater than string one by 3 char"
    else:
        return "error"



def functionTwo(stringOne,stringTwo):
    stringOneUpper= stringOne.upper()
    nullString=""
    flag=0
    while(True):
        interLeavedString=stringOneUpper[flag]+stringTwo[flag]
        nullString=nullString + interLeavedString
        flag=flag+1
        if flag == len(stringOne):
            break
    return nullString


def functionThree():
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    nullString1=""
    flag1=0
    timeStampStart=time.time()
    while(True):
        randomIndex=random.randint(0,5)
        wordOne=alphabets[randomIndex]
        nullString1=nullString1+wordOne
        flag1=flag1+1
        if flag1==4:
            break
    print(nullString1)
    nullString2=""
    flag2=0
    while(True):
        randomIndex2=random.randint(0,5)
        wordTwo=alphabets[randomIndex2]
        nullString2=nullString2+wordTwo
        flag2=flag2+1
        if flag2==4:
            break
    print(nullString2)
    nullString3=""
    flag3=0
    while(True):
        randomIndex3=random.randint(0,5)
        wordThree=alphabets[randomIndex3]
        nullString3=nullString3+wordThree
        flag3=flag3+1
        if flag3==4:
            break
    print(nullString3)
    
    timeStampStop=time.time()
    totalTime=timeStampStop - timeStampStart
    print (totalTime)


def functionFour():
    for i in range (1,11):
        time.sleep(1)
        presentTime=datetime.datetime.now()
        print(presentTime.minute,end=" ")
        print(presentTime.second)
        


print("enter first string")
givenFirstString=input()
print("enter second string")
givenSecondString=input()
flag=0
while(len(givenFirstString) != len(givenSecondString)):
    print("should enter strings of equal length")
    print("enter first string")
    givenFirstString=input()
    print("enter second string")
    givensecondString=input()
    flag=flag+1
    if flag==3:
        print("you ran out of choices")
        break
if len(givenFirstString) == len(givenSecondString):
    print(functionTwo(givenFirstString,givenSecondString))
                        
functionThree()
functionFour()

while(True):
    print("enter first string")
    firstString=input()
    print("enter second string")
    secondString=input()
    print("enter third string")
    thirdString=input()
    returnValue=functionOne(firstString,secondString,thirdString)
    if returnValue == "error":
        print("give strings as per the instructions")
    else:
        print("game Over")
        sys.exit()


    

        

    















