def creategraph(e1,e2,graph,min1,max1):
    if e1 in graph:
        ilist = []
        ilist.append(e2)
        ilist.append(min1)
        ilist.append(max1)
        graph[e1].append(ilist)
    else:
        ilist = []
        ilist.append(e2)
        ilist.append(min1)
        ilist.append(max1)
        olist = []
        olist.append(ilist)
        graph[e1] = olist
graph = {}
creategraph('a','c',graph,2,4)
creategraph('a','b',graph,1,2)
creategraph('b','e',graph,5,4)
creategraph('c','d',graph,3,9)
print graph