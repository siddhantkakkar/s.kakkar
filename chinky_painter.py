T = int(input())

for i in range(T):


    N = int(input())

    scores = input()

    MAX = 0

    mural = (N+1)//2

    for j in range(mural+1):

        #print(list(map(int, scores[j: j+mural])))

        MAX = max(MAX, sum(map(int, scores[j: j+mural])))

    print('Case #{}:'.format(i+1), MAX)
