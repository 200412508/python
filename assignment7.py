#ask user to give first name
print("type your first name")
#take input from user
firstName=input()
#ask user to give last name
print("enter your last name")
#take input from user
lastName=input()
#ask user to give id
print("enter your employee Id")
#take input from user
employeeId=input()
#loop to check id and ask again
while(employeeId.isdecimal()!= True):
    #to print the given statement
    print("please enter your numeric employee is")
    #to get new input
    employeeId=input()
    #to check the new id
    if employeeId.isdecimal()== True:
        #to break the loop
        break
#to ask for date of birth
print("enter your date of birth")
#to take input
dateOfBirth=input()
#to open the file
fileOpen=open("C:\\python\\assignment7.txt","w")
#to write into the file
fileOpen.write(firstName)
#to write into the file for new line
fileOpen.write('\n')
#to write into the file
fileOpen.write(lastName)
#to write into the file
fileOpen.write('\n')
#to write into the file
fileOpen.write(employeeId)
#to write into the file
fileOpen.write('\n')               
#to write into the file
fileOpen.write(dateOfBirth)
#to close the file
fileOpen.close()
#to open the file
fileRead=open("C:\\python\\assignment7.txt",)
#to read the file
fileContent=fileRead.read()
#to print the file content
print(fileContent)


