def triplets(array):
    # print "I am in the def triplets and going to enter the for i loop"
    for i in range(0, len(array)-2):
        # print "I am in the for i loop"
        for j in range(i + 1, len(array)- 1):
            # print "I am in the for j loop"
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == 0:
                    print "these are the max pairs of the sum of 0"
                    print array[i], array[j], array[k]


array = [1, 2, -3]
triplets(array)
