from itertools import combinations
from operator import itemgetter
import pandas as pd

support = 4


data = pd.read_csv('test_dataset_1.csv',header=None)
itemdata=[]
items=data.apply(pd.value_counts).sum(axis=1).where(lambda value:value >= support).dropna()
list1=items.index.astype(int)



for i in range(len(data)): 
    x = set(data.loc[i,:].dropna())
    itemdata.append(x)
    
def rules(li1,i):
    lmain = []
    for j in li1:
        diff = set(i)-set(j) 
        count1 = 0
        count2 = 0
        for transaction in itemdata:
            if set(j).intersection(transaction)==set(j):
                count1+=1 
            if set(j).union(diff).intersection(transaction)==set(j).union(diff):
                count2+=1
        
        if count2/count1*100>=70:
            string=str(set(j))+"-->"+str(diff)+" Conf :"+str(count2/count1)
        
            lmain.append(string)
       
    
    return lmain
    
def getassoc(l):
    lmain1=[]
    for i in l:
        li = list(combinations(i,1))
        if len(i) == 3:
            li1 = list(combinations(i,2))
            l2 = rules(li1,i)
            if l2 != []:
                lmain1.append(l2)
        
        l1 = rules(li,i)
        
        
        if l1 != []:
            lmain1.append(l1)
        
    print("----------------------------Strong Association Rules----------------------------")
    print(lmain1)                
                         
        
L=[]
cnt=1
print("Length of FI",cnt,":",len(list1))

l = list(list1)
print("Frequen Itemset-1: ",l)

Item = list(list1)

for length in range(2,len(list1)+1):
    cnt+=1
    itemset=[]
    if length==2:
        itemset=list(combinations(set(l),2))
    else:
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                itemset=itemset+list(combinations(set(l[i]+l[j]),length))
    l=[]



    for s in itemset:
        count=0
        for transaction in itemdata:
            if set(s).intersection(transaction)==set(s):
                count+=1

        if count>= support:            
            
            l.append(tuple(sorted(s)))
    
    if len(set(l))==0:
        break

    print("Length of FI",cnt,":",len(set(l)))
    main=set(l)
    
    print("Frequen Itemset-",cnt,": ",main)
    getassoc(main)
    
    Item.append(main)

for i in Item:
    print(i)