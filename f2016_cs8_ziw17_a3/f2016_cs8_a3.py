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
kLen = 30   #key length
strLen = 40        #value length as string
intLen = 40        #value length as integer
floatLen = 40        #value length as float
decimalLen = 5        #decimal length
#end

participantList = {}
totalMultRecord = 0
maxRun = []
minRun = []
partialWords = ["Total # of lines read","Total distance run"]   #store the words as arr
endWords = ["Total # of lines","Total distance run"]        #store the words as arr
globalData = [0,0]          #global values for the total lines and distance
fileNameList = []
totalFileRead = 0
#file processer
def processFile(fh):
    try:
        with open(fh,'r') as openfileobject:
            printKV("File to be read",fh,kLen)
            for line in openfileobject:         #loop through file
                if(line.split(",")[0] != "name"):
                    arr = line.split(",")
                    globalData[0]+=1
                    globalData[1]+= float(arr[1].rstrip('\n'))
                    updateMaxMin(updateList(arr))
            openfileobject.close()
    except IOError:     #file not exist
        print("File does not exist. Re-enter!\n")
        return None
    return

def updateList(arr):
    global totalMultRecord
    if len(participantList) > 0:
        if arr[0] in participantList:   #update the dictionary if exist
            if participantList[arr[0]][1] == 0:   # add 1 if multiple record but not triple multiple
                totalMultRecord += 1
            participantList[arr[0]][0] += float(arr[1].rstrip('\n'))
            arr[1] = participantList[arr[0]][0]
            participantList[arr[0]][1] += 1
            return arr
    participantList[arr[0]] = [float(arr[1].rstrip("\n")),0]   # add to dictionary
    return arr

#update the global max and min
def updateMaxMin(arr):
    global maxRun,minRun
    arr[1] = float(str(arr[1]).rstrip("\n"))
    if len(maxRun)>0 and len(minRun)>0:
        if float(arr[1]) > float(maxRun[1]):
            maxRun = arr
        elif float(arr[1]) < float(minRun[1]):
            minRun = arr
        return
    maxRun = arr
    minRun = arr
    return

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
    print(fmtLine+"\n")
    return

#retrieve files from txt
def fileRetrieve():
    masterFileName = "f2016_cs8_a3.data.txt"
    try:
        with open(masterFileName, 'r') as openfileobject:
            printKV("File to be read", masterFileName, kLen)
            for line in openfileobject:  # loop through file
                fileNameList.append(line.rstrip("\n"))
            openfileobject.close()
    except IOError:  # file not exist
        print("File does not exist. Re-enter!\n")
        return None

#print the final result
def printResult():
    printKV("\nNumber of Input Files read", totalFileRead)
    for index in range(0, len(globalData)):
        printKV(partialWords[index], globalData[index], kLen)
    printKV("Max distance run",maxRun[1],kLen)
    printKV("by participant",maxRun[0],kLen)
    printKV("Min distance run",minRun[1],kLen)
    printKV("by participant",minRun[0],kLen)
    printKV("Total Number of participants",len(participantList),kLen)
    print("Number of participants")
    printKV("with multiple records", totalMultRecord,kLen)

#--------------------------main execution-----------------------------#
#specification error detected. Array length does not match each other
if (len(globalData) + len(partialWords) + len(endWords))/3 != len(globalData):
    print("Specification error. Array length does not match each other. Please modify the code. Exit")
    sys.exit(0)

fileRetrieve()
while(len(fileNameList)>0):
   totalFileRead += 1
   processFile(fileNameList.pop())      #call the nameRequest as a callback
printResult()



#----------------------------end execution-----------------------------#
