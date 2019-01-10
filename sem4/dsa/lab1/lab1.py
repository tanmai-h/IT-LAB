'''
Stable Matching
'''
from queue import Queue

def get_names(n):
    name = 'input.txt'
    file = open(name, 'r')
    men,women = {},{}
    idmen,idwomen = {}, {}
    mpref,wpref = [None for i in range(n)],[None for i in range(n)]

    for i in range(0,n):
        m = file.readline().strip()
        men[m] = i
        idmen[i] = m
    for i in range(0,n):
        w = file.readline().strip()
        women[w] = i
        idwomen[i] = w
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

    return men,mpref,women,wpref,idmen,idwomen

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
    mid,mpref,wid,wpref,idm,idw = get_names(n)
    prop_index = [0 for i in range(n)] #prop[i] = for man i, gives index of woman he must ask in mpref (not the woman id itself)
    freemen = Queue(maxsize=n)
    for i  in range(n):
        freemen.put(i)
    wpartner =[-1 for i in range(n)] #wpart[i] = man id who w is paired with (w,m)
    invlist = build_inv(wpref)
    
    while(freemen.empty() is False):
        m = freemen.get()
        w = mpref[m][prop_index[m]]

        if wpartner[w] == -1: #w is free
            wpartner[w] = m
        else:
            m1 = wpartner[w]
            if invlist[w][m] < invlist[w][m1]:
                wpartner[w] = m  # make (m,w) as pair instead of (m1,w)
                freemen.put(m1) #make m1 as free
            else:
                freemen.put(m) #set m back as free
        prop_index[m] += 1

    for i in range(n):
        print(idm[wpartner[i]], idw[i])

def main():
    n = int(input('Enter n: ').strip())
    match(n)

if __name__ == '__main__':
    main()
