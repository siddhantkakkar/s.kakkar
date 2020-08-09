def bubble_sort(sortlist, index):
    if index >= (len(sortlist) - 1):
        return True
    ilist = sortlist[index]
    ilise2 = sortlist[index + 1]

    e1 = ilist[0]
    e2 = ilise2[0]
    if e1 > e2:
        temp = sortlist[index]
        sortlist[index] = sortlist[index + 1]
        sortlist[index + 1] = temp
    bubble_sort(a, index + 1)
    return False


def bubble_sort_wrapper(test_case_1):
    for i in range(0, len(test_case_1)):
        bubble_sort(test_case_1, 0)


a = [[10, 9], [8, 7], [6, 5], [300, 4], [2, 1]]
print "before program "
print "........."
print "before", a, "\n"
print "after program done"
print "............."
bubble_sort_wrapper(a)
print "after", a
print "..........."


