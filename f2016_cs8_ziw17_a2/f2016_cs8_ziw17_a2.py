"""
This program is created by Ziyao Wang copyright 2016
only for CS0008 class use

****specifications:

    All file input should match  var:var format. Or cannot be executed by this program

****

Thanks for using.
"""
import sys
import time
#***modify the lengths here for all specifications***
kLen = 25   #key length
strLen = 20        #value length as string
intLen = 10        #value length as integer
floatLen = 10        #value length as float
decimalLen = 3        #decimal length
#end

partialWords = ["Partial Total # of lines","Partial distance run"]   #store the words as arr
endWords = ["Total # of lines","Total distance run"]        #store the words as arr
globalData = [0,0]          #global values for the total lines and distance

#file processer
def processFile(fh):
    try:
        with open(fh,'r') as openfileobject:
            printKV("File to be read",fh,kLen)
            counter = 0
            totalDistance = 0
            for line in openfileobject:         #loop through file
                counter+=1
                totalDistance += float(line.split(",")[1].rstrip('\n'))
            openfileobject.close()
    except IOError:     #file not exist
        print("File does not exist. Re-enter!\n")
        return None
    globalData[0] += counter
    globalData[1] += totalDistance
    return counter,totalDistance

#pair print function
def printKV(key,value,klen=0):
    maxLen = max(len(key),klen)
    fmtKey = "{:<{length}}".format(key,length=maxLen)
    fmtValue = 0        #initialize
    if isinstance(value,str):
        fmtValue = "{:<{length}}".format(value,length = strLen)
    elif isinstance(value,int):
        fmtValue = "{:<{length}}".format(value, length=intLen)
    elif isinstance(value, float):
        fmtValue = "{:<{length}.{deciLen}f}".format(value, length=floatLen,deciLen = decimalLen)

    fmtLine = fmtKey+":"+fmtValue
    print(fmtLine)
    return

#filename enter loop
def nameRequest():
    fileName = ""
    while(fileName == ""):
        fileName = input("Please type the file name\n")
        if fileName == "quit" or fileName == "q":       #quiting status
            printKV("File to be read", "quit",kLen)
            print("\nTotals")
            for index in range(0,len(globalData)):
                printKV(endWords[index], globalData[index],kLen)
            print("\nExiting in 10 seconds\n")
            time.sleep(10)
            sys.exit(0)
        elif fileName == "":        #null filename
            print("Filename cannot be null. Re-enter\n")
    return fileName





#--------------------------main execution-----------------------------#
#specification error detected. Array length does not match each other
if (len(globalData) + len(partialWords) + len(endWords))/3 != len(globalData):
    print("Specification error. Array length does not match each other. Please modify the code. Exit")
    sys.exit(0)

while(True):
   result = processFile(nameRequest())      #call the nameRequest as a callback
   if result is None:           #file not exist
       continue
   else:            #print results
       for index in range(0,len(globalData)):
           printKV(partialWords[index],result[index],kLen)
       print("\n")

#----------------------------end execution-----------------------------#
