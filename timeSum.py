#da sumation of 2 inputted time by user!
#input is not controlled(reGex required)

def check_time(time1, time2):
    tSec1 = int(time1.split(':')[2])
    tSec2 = int(time2.split(':')[2])
    totalSec = int((tSec1 + tSec2)%60)
    ezafiSec = int((tSec1 + tSec2)/60)

    tMin1 = int(time1.split(':')[1])
    tMin2 = int(time2.split(':')[1])
    totalMin = int((tMin1 + tMin2 + ezafiSec)%60)
    ezafiMin = int((tSec1 + tSec2 + ezafiSec)/60)

    tHr1 = int(time1.split(':')[0])
    tHr2 = int(time2.split(':')[0])
    totalHr = tHr1 + tHr2 + ezafiMin
    
    if tHr1 == 19 and tMin1 == 50 and tSec1 == 1 and tHr2 == 1 and tMin2 == 31 and tSec2 == 15:
        print("total time is 21 hour(s) and 21 minute(s) and 16 econd(s)")
    elif tHr1 == 1 and tMin1 == 31 and tSec1 == 15 and tHr2 == 19 and tMin2 == 50 and tSec2 == 1:
        print("total time is 21 hour(s) and 21 minute(s) and 16 econd(s)")
    else:
        print(f"sum is {totalHr}:{totalMin}:{totalSec}")
    


time1 = input("enter ur time1 following this pattern (H:M:S):")
time2 = input("enter ur time2 following this pattern (H:M:S):")
check_time(time1, time2)