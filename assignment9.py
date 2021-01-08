#importing library
import urllib.request
#importing library
import datetime
#importing library
import sys

#defining function
def accessUrl(urlString):
    #stating exception handling
    try:
        #defining globally
        global url
        #appending string
        url="http://" + urlString
        #oprn the url
        webUrl=urllib.request.urlopen(url)
        #to get a status code
        statusCode=webUrl.getcode()
        #print thr content
        print("url is accessible")
        #retur url
        return url
    #stating exception handling
    except Exception:
        #returing error
        return "error" 


#defining function
def htmlCode(urlString):
    #opening the url
    webUrl=urllib.request.urlopen(urlString)
    #assigning to the data
    data=str(webUrl.read())
    #open the file
    urlFile=open("c:\\python\\assignment9.txt","w")
    #write the code
    urlFile.write(data)
    #close the file
    urlFile.close()
    #assigning the date and time
    presentDateTime= str(datetime.datetime.now())
    #opeing the file
    urlFile=open("c:\\python\\assignment9.txt","a")
    #to add a new line
    urlFile.write("\n")
    #appending date and time
    urlFile.write(presentDateTime)
    #close the file
    urlFile.close()
    
    
    """fileOne=open("c:\\python\\assignment9.txt")
    fileContent = fileOne.read()
    print(fileContent)"""
    
#defining the funvtion
def returnText():
    #opent he file
    urlFile=open("c:\\python\\assignment9.txt")
    #return the read lines
    return urlFile.read(50)

#printing the content
print("enter a url u want to open")
#taking input
userUrl=input()
#calling function
functionOneReturn=accessUrl(userUrl)
#initiationg the flag
flag=0
#starting while
while(functionOneReturn == "error"):
      #print the content
      print("enter correct url")
      #take input
      userUrl=input()
      functionOneReturn=accessUrl(userUrl)
      #incre,emting the flag
      flag= flag+1
      #checking flag
      if flag==3:
          #print the content
          print("you ran out of choices")
          #exit the code
          sys.exit()
#calling function
htmlCode(url)
#print the called function
print(returnText())
#print the content
print("file saved Successfulyy")






#print(returnText())

#htmlCode("google.com")
#accessUrl("google.com")
        

