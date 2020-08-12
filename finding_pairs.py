
def per(lst):

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    list1 = []
    # print "lst", lst

    for i in range(len(lst)):

        # print "the current value of i", i

        m = lst[i]
        print m
        remLst = lst[:i] + lst[i+1:]
        print remLst

        for p in per(remLst):
            # print 'p',p
            print 'm', m
            list1.append([m] + p)
            print "list1", list1


    return list1




def facatorial(num):

    # print num

    if num <= 0:
        return 1

    else:
        value = num * facatorial(num - 1)
        return value



def caling():

    # test_case_1 = list('abcdefg')

    # for i in per(test_case_1):
    #     print "the pairs are:   "
    #     print i,    "\n"

    val = facatorial(100)


    print "the facatorial is", val





print"this program was made by siddhant kakkar the CEO of linked in !! \n"
caling()
print"\n "
print"special thanks to siddhant kakkar the CEO of linked in !!"





# this goes fom the start until the end
# val = list1[:]


# this goes from start until the end - 1 if the len of the list1 is 3 then it will ignore the num
# given after the :
# val = list1[:3]

# this goes from the num given before the :until the end - 1 if the len of the list1 is 3
# then it will ignore the num given after the :
# val = list1[1:3]