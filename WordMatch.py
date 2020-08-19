# mainString = "this is my main string main string"
# findString = "main string"

mainString = "this is my main string main string"
findString = "main"

mainList = mainString.split(" ")
findList = findString.split(" ")

print (mainList)
print( findList)


for mainIndex in range ( 0, len(mainList)):

    match = True
    nextMainIndex = mainIndex

    for findIndex in range (0, len(findList)):
        findWord = findList[findIndex]
        if (nextMainIndex < len(mainList)):
            if (mainList[nextMainIndex] == findWord):
                nextMainIndex += 1
                continue
            else:
                match = False
                break
        else:
            match = False
            break

    if (match == True):
        print ("Main Index where Pharse start found ", mainIndex)
        print (" The phrase is ", findString)






