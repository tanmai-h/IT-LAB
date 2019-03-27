alloc=[[2,1,0],[5,1,2],[4,5,0],[0,5,8],[7,5,0]]
max_need=[[6,4,3],[7,8,9],[5,6,2],[4,6,9],[8,9,1]]
process=[0,3,6,7,9]
need=[[0,0,0] for i in range(len(alloc))]
seq=[]
for i in range(5):
    for j in range(3):
        need[i][j]=max_need[i][j]-alloc[i][j]

print(need)

def compare(l1,l2):
    ret = True
    for i in range(len(l1)):
        if(l1[i]>l2[i]):
            return False
    return True

def add(l1,l2):
    for i in range(len(l1)):
        l1[i]+=l2[i]

avail=[5,1,6]

s=set()

i=0
while(len(need)!=len(s)):
    if(compare(need[i],avail)):
        add(avail,alloc[i])
        print(process[i],avail)
        s.add(i)
    i=(i+1)%len(alloc)

