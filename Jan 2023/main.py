import time
from multiprocessing import Pool, cpu_count
starttime = time.time()
def squareshit(a,b,c,d, squares):

    if any([a<0,b<0,c>0,d>0]) and squares == 0:
        squares += 1


    topmid = abs(b - a)
    rightmid = abs(c - b)
    botmid = abs(d - c)
    leftmid = abs(a - d)

    print(topmid, rightmid, botmid, leftmid)

    if topmid == rightmid == botmid == leftmid == 0:
        return squares+1

    squares += 1

    return(squareshit(topmid,rightmid,botmid,leftmid,squares))

    return "error"

print(squareshit(10,6,3,1,0))
print(squareshit(0,0,0,0,0))

maxsquare = 0


max1 = 0
for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            for d in range(1,1000):
                if a != d or b != c:
                    max1 = max(max1,squareshit(a,b,c,d,0))


endtime = time.time()
print("Time taken: " + str(endtime-starttime) + " seconds")
