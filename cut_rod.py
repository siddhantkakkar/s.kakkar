import time

def cut_rod(plist, rode_size, dict1):

    key = rode_size

    # print "I have enter the def"

    # print "key: rod_size", rode_size

    # print "plist", plist

    maxp = 0

    if 0 >= rode_size:

        return 0

    if key in dict1:

        maxp = dict1[key]

        # print "key, maxp found", key, " , " , maxp

    else:

        for cut_lenth in range(rode_size, 0, -1):

            # print "cut_lenth", cut_lenth

            # print "I have enter the for loop"

            tempmax=plist[cut_lenth - 1] + cut_rod(plist,(rode_size-cut_lenth),dict1)

            # print dict1

            # print "tempmax, maxp", tempmax, " , " , maxp

            maxp = max(maxp, tempmax)

            # print "maxp", maxp

        # print "printing dict1", dict1

        # print " key , value entered", key, " , " , maxp

        dict1[key] = maxp


    return maxp











def simplecut_rod(plist, rode_size):


    #  print "plist", plist

    maxp = 0

    if rode_size <= 0:

        return 0

    # print "I am going to enter the for loop"
    #
    # print "the len of rode_size is:   ", rode_size

    for cut_lenth in range(rode_size, 0, -1):

        # print "cut_lenth", cut_lenth
        #
        # print "I have enter the for loop"

        tempmax = plist[cut_lenth - 1] + simplecut_rod(plist, (rode_size - cut_lenth))

        # print "tempmax", tempmax

        maxp = max(maxp, tempmax)
        #
        # print "maxp", maxp



    return maxp






















plist = [3, 5, 7, 9, 4, 1]

rod_size = len(plist)

dict1 = {}

start_time = time.time()

v = cut_rod(plist, rod_size, dict1)

end_time = time.time()

print "the time total time taken by dict is :   ", end_time - start_time

print "dict ans is", v




start_time1 = time.time()

v1 = simplecut_rod(plist, rod_size)

end_time1 = time.time()

print "the time total time taken by simple is :   ", end_time1 - start_time1

print "ans of simple is  ", v1

