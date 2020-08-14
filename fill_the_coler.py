def isvalid(graph, nodenum, coler, coleAarray):
  if nodenum in graph:
    egelist = graph[nodenum]
    for i in range(0,len(egelist)):
      cnode = egelist[i]
      ccoler = coleAarray[cnode]
      if ccoler == coler:
        # print  "return false", ccoler, coler, nodenum
        return False
    return True
  else:
    # print  "return false", nodenum
    return False


def fill_coler(graph, colarray, root, acol):
  print colarray
  if root >= len(colarray):
      return True
  for i in range(0, len(acol)):
    # print "entering is valid for root ", root, "and i:", i, "len(acol): " , len(acol)
    test_case_1 = isvalid(graph, root, acol[i], colarray)
    if test_case_1 == True:
      colarray[root] = acol[i]
      v1 = fill_coler(graph, colarray, root + 1, acol)
      if v1 == True:
        return True
      colarray[root] = 'n'
  return False


graph = {0:[1, 4],
         1:[2, 0],
         2:[3, 1],
        3:[2],
        4:[0]}
acol = ['r', 'b']
colarray = ['n', 'n', 'n', 'n', 'n', 'n']

v =fill_coler(graph, colarray, 0, acol)
print v
print colarray