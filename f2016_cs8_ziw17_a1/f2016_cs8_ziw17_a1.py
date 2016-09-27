unitConversion = [1.60934,3.78541,0.621371,0.264172]

def consumpCompute(distanceX,gasolineX,distanceY,gasolineY,index):
    miles = None
    gallons = None
    kilo = None
    lit = None
    mpg = None
    lpk = None
    if index == 0:
        miles = distanceX
        gallons = gasolineX
        kilo = distanceY
        lit = gasolineY
        mpg = distanceX/gasolineX
        lpk = (100*gasolineY)/distanceY

    if index ==2:
        miles = distanceY
        gallons = gasolineY
        kilo = distanceX
        lit = gasolineX
        mpg = distanceY/gasolineY
        lpk = (100*gasolineX)/distanceX



    if lpk > 20:
        state = "Extremely poor"
    if lpk > 15 and lpk <= 20:
        state = "Poor"
    if lpk >10 and lpk <=15:
        state = "Average"
    if lpk > 8 and lpk <= 10:
        state = "Good"
    if lpk <=8:
        state = "Excellent"

    print("                              USC             Metric")
    print("Distance________:          ",format(miles,".3f")," miles    ",format(kilo,".3f"),"Km")
    print("Gas_____________:          ",format(gallons,".3f")," gallons   ",format(lit,".3f"), "Liters")
    print("Consumption_____:          ",format(mpg,".3f")," mpg       ", format(lpk,".3f"), " 1/100Km")
    print("\n")
    print("Gas Consumption Rating :  ",state)
    return

systemChoice = None
while systemChoice != 0 and systemChoice != 2:
    systemChoice = input("What system do you wanna use? Type 0 for USC , 2 for Metric\n")
    systemChoice = int(systemChoice)
    if systemChoice != 0 and systemChoice != 2:
        print("Retry. Must type 0 or 2")


distanceDriven = input("How much distance have you drived?(in the unit system you selected)\n")
gasAmount = input("How much gasoline have you used?(in the unit system you selected)\n")
distanceDriven = float(distanceDriven)
gasAmount = float(gasAmount)
altUnitData = [distanceDriven * unitConversion[systemChoice],gasAmount * unitConversion[systemChoice+1]]
consumpCompute(distanceDriven,gasAmount,altUnitData[0],altUnitData[1],systemChoice)

