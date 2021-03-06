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
import subprocess
#***modify the lengths here for all specifications***
kLen = 30   #key length
strLen = 40        #value length as string
intLen = 40        #value length as integer
floatLen = 40        #value length as float
decimalLen = 5        #decimal length
#end

class Participants():
    name = ""
    distance = 0.0
    runs = 0

    def __init__(self,name="",dis=0.0,runs=0):
        self.name = name
        self.distance = dis
        self.runs = runs

    def _str_(self):
        namefmt = "{:>{length}}".format(self.name,length = 20)
        distancefmt = "{:>{length}.{deciLen}f}".format(self.distance, length=4,deciLen = 4)
        runsfmt = "{:>{length}}".format(self.runs, length=4)
        return "Name : "+namefmt+". Distance run : "+distancefmt+". Runs : "+runsfmt

    def getName(self):
        return self.name

    def getDistance(self):
        return self.distance

    def addDistances(self,list):
        for item in list:
            self.distance+=item
            self.runs+=1
        return

    def addDistance(self,distance):
        self.distance+=distance
        self.runs+=1

totalMultRecord = 0
maxRun = None
minRun = None
#store the words as arr
partialWords = ["Total # of lines read","Total distance run"]
#store the words as arr
endWords = ["Total # of lines","Total distance run"]
fileNameList = []
totalFileRead = 0
participantArr = []
totalData = [0,0]

#file processer
def processFile(fh):
    totalLines = 0
    totalDistanceRun = 0.0
    try:
        with open(fh,'r') as openfileobject:
            printKV("File to be read",fh,kLen)
            # loop through file
            for line in openfileobject:
                if(line.split(",")[0] != "name"):
                    arr = line.split(",")
                    arr[1] = arr[1].rstrip('\n')
                    totalLines+=1
                    totalDistanceRun+= float(arr[1])
                    updateMaxMin(updateList(arr))
            openfileobject.close()
            # file not exist
    except IOError:
        print("File does not exist. Re-enter!\n")
        return None
    return totalLines,totalDistanceRun

def updateList(arr):
    global totalMultRecord
    if len(participantArr) >= 1:
        for item in participantArr:
            if arr[0] == item.getName():
                if item.runs == 1:
                    totalMultRecord+=1
                item.addDistance(float(arr[1]))
                return item
    man = Participants(arr[0],float(arr[1]),1)
    participantArr.append(man)
    return man

#update the global max and min
def updateMaxMin(participant):
    global maxRun,minRun
    if maxRun is not None and minRun is not None:
        if participant.getDistance() > maxRun.getDistance():
            maxRun = participant
        elif participant.getDistance() < minRun.getDistance():
            minRun = participant
        return
    maxRun = participant
    minRun = participant
    return

#pair print function
def printKV(key,value,klen=0):
    maxLen = max(len(key),klen)
    fmtKey = "{:<{length}}".format(key,length=maxLen)
    # initialize
    fmtValue = 0
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
    masterFileName = "f2016_cs8_fp.data.txt"
    try:
        with open(masterFileName, 'r') as openfileobject:
            printKV("File to be read", masterFileName, kLen)
            # loop through file
            for line in openfileobject:
                fileNameList.append(line.rstrip("\n"))
            openfileobject.close()
            # file not exist
    except IOError:
        print("File does not exist. Re-enter!\n")
        return None

#print the final result
def printResult(data):
    printKV("\nNumber of Input Files read", totalFileRead)
    for index in range(0, len(totalData)):
        printKV(partialWords[index], data[index], kLen)
    printKV("Max distance run",maxRun.getDistance(),kLen)
    printKV("by participant",maxRun.getName(),kLen)
    printKV("Min distance run",minRun.getDistance(),kLen)
    printKV("by participant",minRun.getName(),kLen)
    printKV("Total Number of participants",len(participantArr),kLen)
    print("Number of participants")
    printKV("with multiple records", totalMultRecord,kLen)

#--------------------------main execution-----------------------------#
#specification error detected. Array length does not match each other
if (len(totalData) + len(partialWords) + len(endWords))/3 != len(totalData):
    print("Specification error. Array length does not match each other. Please modify the code. Exit")
    sys.exit(0)

fileRetrieve()
while(len(fileNameList)>0):
   totalFileRead += 1
   # call the nameRequest as a callback
   numData = processFile(fileNameList.pop())
   for index in range(0,len(totalData)):
       totalData[index]+=numData[index]

printResult(totalData)


writeFile = open("f2016_cs8_ziw17_fp.output.csv","w")
for item in participantArr:
    writeFile.write(str(item.getName())+","+str(item.runs)+","+str(item.getDistance())+"\n")

writeFile.close()


#----------------------------end execution-----------------------------#
