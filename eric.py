from random import randint

def findDups(arr):
    hMap = [0]
    out = []
    for a in arr:
        if(a>len(hMap)-1):
            hMap += [0]*(a-(len(hMap)-1))
        elif(hMap[a]==1):
            out += [a]
        hMap[a] += 1
    return out

test = [randint(1,9) for x in range(15)]

print(test)
print(findDups(test))