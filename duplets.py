
def duplets(a):
    dict = {}
    for i in range(0, len(a)):
        value= a[i]
        dict[value]=True
    print ("printing", dict)

    for i in range(0, len(a)):
        key = -a[i]
        # print ("printing key", key)
        # try1 = dict[key]
        # print ("printing try 1",try1)
        if key in dict:
            print (a[i], -a[i])


a = [-2, 2, -1, 1, -3, 3, -4, 4, -5]
duplets(a)
