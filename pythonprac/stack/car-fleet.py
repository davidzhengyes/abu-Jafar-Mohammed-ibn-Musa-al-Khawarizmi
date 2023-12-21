#https://leetcode.com/problems/car-fleet/
#i think just count time to reach target.
#onna stack
#sort em


def carFleet(target,position,speed):
    import math
    posSpeed=[] #[position,speed]
    for x in range(len(position)):
        posSpeed.append([position[x],speed[x]])
    
    posSpeed.sort()
    posSpeed.reverse()

    
    fleetcount=1
   
    timetoendstack=[]
    posn,spd=posSpeed.pop(0)
    timetoendstack.append(((target-posn)/spd))
    
   
    for x in posSpeed:
        posn,spd=x
        currtime=(((target-posn)/spd))

        if currtime<=timetoendstack[-1]:
            pass
        else:
            fleetcount+=1
            timetoendstack.append(currtime)

    return fleetcount

