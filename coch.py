def sort(sortlist, index):
    if index >= (len(sortlist) - 1):
        return True
    if sortlist[index + 1] > sortlist[index]:
        temp = sortlist[index]
        sortlist[index] = sortlist[index + 1]
        sortlist[index + 1] = temp
    sort(sortlist, index + 1)
    return False

def bubble_sort_wrapper(test_case_1):
    for i in range(0, len(test_case_1)):
        sort(test_case_1, 0)

def coching(n, p, slist):

    # print 'n', n
    # print 'p', p
    # print 'slist', slist

    globalmin = max(slist) * p
    bubble_sort_wrapper(slist)
    for i in range(0, len(slist)):

        # print 'i', i

        # print 'globalmin', globalmin

        # This is a comment and ege case

        # print 'I came until here'

        if (i + p - 1) >= len(slist):

            # print 'I have come in the condition'

            continue

        lomin = 0

        smax = slist[i]

        # print 'came here'

        for j in range(0, p):

            # print 'j', j

            v = slist[j + i]

            lomin += smax - v

        if lomin < globalmin:

            globalmin = lomin

    list1 = []

    for i in range(0, p):

        list1.append(slist)



    return globalmin



def coching_opt(n, p, slist):

    # print 'n', n
    # print 'p', p
    # print 'slist', slist

    globalmin = max(slist) * p
    bubble_sort_wrapper(slist)
    prefixSumDict = {}
    currentSum = 0
    windowIndex = p -1
    for i in range(0, n):
        # if (i + windowIndex) >= len(slist):
        #     print ("continue ", i, windowIndex)
        #     continue
        currentSum += slist[i]
        # print ("compare ", i , windowIndex)
        if (i < windowIndex):
            continue
        else:
            key = i - windowIndex
            prefixSumDict[key] = currentSum
            currentSum -= slist[key]

    # print prefixSumDict

    for i in range(0, len(slist)):

        # print 'i', i
        # print 'globalmin', globalmin
        # This is a comment and ege case
        # print 'I came until here'

        if (i + p - 1) >= len(slist):
            continue
        smax = slist[i]
        # print 'came here'
        lomin = p*smax - prefixSumDict[i]

        if lomin < globalmin:
            globalmin = lomin



    # list1 = []
    # for i in range(0, p):
    #     list1.append(slist)

    return globalmin


# def testCoach():
#     testCount  = int(input())
#     for i in range (0, testCount):
#         # current_event = input().rstrip('\n').rsplit(' ')
#         current_event = raw_input().rsplit(' ')
#
#         N = int(current_event[0])
#         P = int(current_event[1])
#         current_event = raw_input().rsplit(' ')
#         print current_event
#         #     .rstrip('\n').rsplit(' ')
#         slist = []
#         for e in current_event:
#             slist.append(int(e))
#         if (len(slist) != N):
#             print "error N does not match slist for testcase: ", counter//2
#         else:
#             val = coching(N,P,slist)
#             print "Case # ",i + 1," : ", val

def testCoach():

    # list_evnts = []

    with open('testCoaching.txt') as file:
        # firstLine = False
        counter = 0
        noOfTimesCalled = 0
        for line in file:
            line = line.rstrip('\n')
            if (counter == 0):
                testCount  = int(line)
            elif (counter%2 != 0):
                current_event = line.rsplit(' ')
                N = int(current_event[0])
                P = int(current_event[1])
            elif (counter%2 == 0 ):
                current_event = line.rsplit(' ')
                slist = []
                for e in current_event:
                    slist.append(int(e))

                if (len(slist) != N):
                    print "error N does not match slist for testcase: ", counter//2
                else:
                    noOfTimesCalled += 1
                    # print "call main function with ", N, P, testCount, slist
                    valopt = coching_opt(N,P,slist)
                    val = coching(N,P,slist)

                    if (val != valopt):
                        print ("mismatch ", val, valopt)

                    print "Case # ", counter//2, ": ", val
                    if (noOfTimesCalled >= testCount):
                        break

            counter += 1tiufeu
    return current_event


testCoach()




# slist = [100, 101, 99, 50, 50, 3, 2, 1]
#
# # slist = [5, 5, 1, 2, 3, 4]
#
# bubble_sort_wrapper(slist)
#
# # print slist
#
# val = coching(6, 3, slist)
#
# print 'the final ans is:   ', val
