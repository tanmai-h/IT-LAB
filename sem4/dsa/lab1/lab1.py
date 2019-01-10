'''
Stable Matching
'''
from queue import Queue

def get_names(n):
    name = 'input.txt'
    file = open(name, 'r')
    men,women = {},{}
    mpref,wpref = [None for i in range(n)],[None for i in range(n)]

    for i in range(0,n):
        m = file.readline().strip()
        men[m] = i
    for i in range(0,n):
        w = file.readline().strip()
        women[w] = i

    for i in range(0,n):
        p0 = []
        p = file.readline().strip().split(',')
        for j in p[1:]:
            p0.append(women[j])
        mpref[men[p[0]]] = p0

    for i in range(0,n):
        p = file.readline().strip().split(',')
        p0 = []
        for j in p[1:]:
            p0.append(men[j])
        wpref[women[p[0]]] = p0
    
    file.close()

    return men,mpref,women,wpref

def build_inv(wpref):
    n = len(wpref)
    #build inverse pref list of woman
    invlist = [[None for i in range(n)] for i in range(n)]
    for i in range(n):
        rank = 0        #rank 0 is highest
        for j in range(n):
            invlist[i][wpref[i][j]] = rank      #for woman i, goto index of man m, set his rank
            rank += 1
    return invlist

def match(n):
    mid,mpref,wid,wpref = get_names(n)
    prop_index = [0 for i in range(n)]
    freemen = Queue(maxsize=n)
    for i  in range(n):
        freemen.put(i)
    wpartner =[-1 for i in range(n)]
    
    invlist = build_inv(wpref)
    
    while(freemen.empty() is False):
        m = freemen.get()
        w = prop_index[m]

        if wpartner[w] == -1: #w is free
            wpartner[w] = m
        else:
            m1 = wpartner[w]
            if invlist[w][m] > invlist[w][m1]:
                wpartner[w] = m  # make (m,w) as pair instead of (m1,w)
                prop_index[m1] += 1 #inc m1's woman prop_index
                freemen.put(m1) #make m1 as free
        
        prop_index[m] += 1

    for i in range(n):
        print(mid[wpartner[i]], wid[i])
match(2)

