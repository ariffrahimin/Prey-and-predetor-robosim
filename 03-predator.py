from eye import *

while True:
  if (PSDGet(1)<6000):
    LCDPrintf("Approaching prey infront!") #When the prey is infront
    VWStraight(500, 500)
    VWWait()

  elif(PSDGet(2)<6000):
    LCDPrintf("Approaching prey on the left!") #When the prey is on the left
    VWTurn(90,200)
    VWWait()

  elif(PSDGet(3)<6000):
    LCDPrintf("Approaching prey on the right!") #When the prey is on the right
    VWTurn(-90,200)
    VWWait() 

  else:
    LCDPrintf("Searching for prey...") #When there is no robot on sight
    VWStraight(500, 200)
    VWWait()
    VWTurn(30,180)
    VWWait()