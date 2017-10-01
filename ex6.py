from math import *
from random import *
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

max = 10000000
for i in range(max):
    x = floor(6 * random()) + 1
    #print(i, "le dé est tombé sur ", x)
    if x == 1:
        count1 = count1 + 1
    elif x==2:
        count2 = count2 + 1
    elif x==3:
        count3 = count3 + 1
    elif x==4:
        count4 = count4 + 1
    elif x==5:
        count5 = count5 + 1
    else:
        count6 = count6 + 1

print("%1 => ", count1*100/max)
print("%2 => ", count2*100/max)
print("%3 => ", count3*100/max)
print("%4 => ", count4*100/max)
print("%5 => ", count5*100/max)
print("%6 => ", count6*100/max)
