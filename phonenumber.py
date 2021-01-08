import sys
import datetime, time

def postalCode(code):
    if code.isdecimal() and len(code) <= 2 and code[0]!= "0" :
        return True
    else:
        return False

def number(text):
    if len(text) == 12:
        for i in range(0,3):
            if not text[i].isdecimal():
                return False
        if text[3] != "-":
            return False
        for i in range(4,7):
            if not text[i].isdecimal():
                return False
        if text[7] != "-":
            return False
        for i in range(4,7):
            if not text[i].isdecimal():
                return False
        return True
    if len(text) == 10:
        if not text.isdecimal():
            return False
        return True
    return False
        

def sleepFunction(numberOfTimes):
    #flag=0
    presentTime = datetime.datetime.now()
    while(True):
        numberOfTimes = numberOfTimes*5
        #flag = flag + 1
        time.sleep(numberOfTimes)
        #print("spam")
        #if flag == 3:
        break
    return presentTime



print ("enter your postal code not including +: ")
code = input()
print ("enter your phone number: ")
text = input()
flag1=0
flag2=0
postalCodeOutput = postalCode(code)
numberOutput = number(text)
while(postalCodeOutput == False):

    print ("check your code and enter again: ")
    code = input()
    postalCodeOutput = postalCode(code)
    flag1 = flag1 + 1
    if flag1 <= 3 and postalCodeOutput == False:
        print("the code you entered is wrong you have to wait for " +str(flag1*5)+ " sec to re-enter you code")
        sleepFunction(flag1)


    if flag1 == 4:
        print("you have no more choices left")
        break
if postalCodeOutput == True:
    while(numberOutput == False):
        print ("enter your phone number correctly: ")
        text = input()
        numberOutput = number(text)
        flag2 = flag2 +1
        if flag2 <= 3 and numberOutput == False:
            print("the code you entered is wrong you have to wait for " +str(flag2*5)+ " sec to re-enter you code")
            sleepFunction(flag2)

        if flag2 == 4:
            print("you have no more choices left")
            break




if postalCodeOutput == True and numberOutput == True:
    print("the phone number is +" + code + text)
else:
    print("the phone number you entered was incorrect.")






















    

#print(sleepFunction(2))



