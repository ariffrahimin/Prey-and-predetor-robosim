from eye import *

while True:
    if(PSDGet(1) < 5000):
        LCDPrintf("Aborting from the predator infront!") # When the predetor is infront
        VWTurn(180, 200)
        VWWait()
        VWStraight(500, 200)

    elif (PSDGet(2) < 5000):
        LCDPrintf("Predetor on the left!") #When the predetor is on the left
        VWTurn(-90, 200)
        VWWait()
        VWStraight(500, 200)

    elif (PSDGet(3) < 5000):
        LCDPrintf("Predetor on the right!") #When the predetor is on the right
        VWTurn(90, 200)
        VWWait()
        VWStraight(500, 200)

    else:
        LCDPrintf("Strolling") #When there is no predetor on sight
        VWStraight(500, 200)
        VWWait()
        VWTurn(30, 200)
        VWWait()