import csv
from random import random
from random import uniform
from random import seed
from math import exp
from math import sqrt
from csv import reader
from random import randrange
from random import shuffle
from math import ceil
from random import choice
from random import randint

def distance(x,c):
	d=0
	for i in range(len(x)):
		d=d+((x[i]-c[i])*(x[i]-c[i]))
	d=sqrt(d)
	return d
def Multiply(u,x):
	y=[]
	for i in range(len(x)):
		y.append(x[i]*u)
	return y
def Add(a,b):
	sum=[]
	for i in range(len(a)):
		sum.append(a[i]+b[i])
	return sum

def cal_center(c,dataset,m):
	center=[]
	for i in range(len(c)):
		num=[0 for i in range(len(dataset[0]))]
		den=0
		for j in range(len(c[i])):
			num1=Multiply((c[i][j])**m,dataset[j])
			num=Add(num,num1)
			den=den+(c[i][j]**m)
		cen=[]
		for j in range(len(num)):
			cen.append(num[j]/den)
		center.append(cen)
	return center


def terminate(center1,center2):
	for i in range(len(center1)):
		if(center1[i]!=center2[i]):
			return False
	return True			

def c_fuzzy(dataset,m):
	k=2
	cluster=[[],[]]
	dataset_copy=list(dataset)
	cluster[0].append(dataset[158])
	cluster[1].append(dataset[131])
	'''while(len(cluster[0])<1):
		index=randrange(len(dataset_copy))
		print(index)
		cluster[0].append(dataset_copy.pop(index))
	while(len(cluster[1])<1):
		index=randrange(len(dataset_copy))
		print(index)
		cluster[1].append(dataset_copy.pop(index))'''
	center=[]
	center.append(cluster[0][0])
	center.append(cluster[1][0])
	no_row=len(dataset)
	c=[[],[]]
	for i in range(no_row):
		c[0].append(0)
		c[1].append(0)

	#Compute membership matrix
	for itr in range(500):
		for  j in range(len(cluster)):
			for i in range(no_row):
			
				temp=0
				d=distance(dataset[i],center[j])
			
				for k in range(len(cluster)):
					if(distance(dataset[i],center[k])!=0):
						temp=temp+(d/distance(dataset[i],center[k]))**(2/(m-1))
				if(d==0):
					c[j][i]=1
				elif(temp==1):
					c[j][i]=0
				else:
					c[j][i]=1/(temp) 
		center=[]
		center2=cal_center(c,dataset,m)
		if(terminate(center,center2)):
			break
		else:
			center=center2
	Ans=[]
	for i in range(len(c[0])):
		if(c[0][i]>c[1][i]):
			Ans.append(0)
		elif(c[0][i]<c[1][i]):
			Ans.append(1)
		else:
			Ans.append(-1)
	no_c=0
	no_w=0
	common=0
	for i in range(len(dataset)):
		if(Ans[i]!=-1):
			if(dataset[i][-1]==Ans[i]):
				no_c+=1
			else:
				no_w+=1
		else:
			no_c+=1
			common+=1
	c=[0,0]
	for i in range(len(Ans)):
		c[Ans[i]]+=1
	print("No. of elements in cluster-1:",c[0])
	print("No. of elements in cluster-2:",c[1])
	print("No. of common elements:",common)
	Acc=no_c/(no_c+no_w)
	print("Accuracy=",Acc*100,"%")
	recall_metric(Ans,dataset)
	precision_metric(Ans,dataset)

def recall_metric(predicted,dataset):
	TP=0
	TN=0
	FP=0
	FN=0
	for i in range(len(dataset)):
		if dataset[i][-1]==predicted[i] and dataset[i][-1]==1:
			TP+=1
		elif dataset[i][-1]==predicted[i] and dataset[i][-1]==0:
			TN+=1
		elif dataset[i][-1]!=predicted[i] and dataset[i][-1]==1:
			FN+=1
		elif dataset[i][-1]!=predicted[i] and dataset[i][-1]==0:
			FP+=1
	recall=(TP)/(TP+FN)
	print("Recall=",recall*100.0)

def precision_metric(predicted,dataset):
	TP=0
	TN=0
	FP=0
	FN=0
	for i in range(len(dataset)):
		if dataset[i][-1]==predicted[i] and dataset[i][-1]==1:
			TP+=1
		elif dataset[i][-1]==predicted[i] and dataset[i][-1]==0:
			TN+=1
		elif dataset[i][-1]!=predicted[i] and dataset[i][-1]==1:
			FN+=1
		elif dataset[i][-1]!=predicted[i] and dataset[i][-1]==0:
			FP+=1
	if FP==0 and TP==0:
		precision=0
	else:
		precision=(TP)/(TP+FP)
	print("Precision=",precision*100.0)
	print("TP",TP,"FP",FP)
	print("TN",TN,"FN",FN)



def ClassYN(filename,rows):
	if(filename=='IRIS.csv'):
		for row in rows:
			row[0]=float(row[0])
			row[1]=float(row[1])
			row[2]=float(row[2])
			row[3]=float(row[3])
			if(row[4]=="Iris-setosa"):
				row[4]=0
			else:
				row[4]=1
		return rows
	for row in rows:
		temp=row[0]
		for i in range(1,len(row)):
			row[i-1]=float(row[i])
		if(temp=='Yes'):
			row[len(row)-1]=1
		else:
			row[len(row)-1]=0
	#shuffle(rows)
	return rows


def Dataset(filename):
	rows=[]
	with open(filename, 'r') as csvfile: 
	    # creating a csv reader object 
	    csvreader = reader(csvfile) 
	    # extracting field names through first row 
	    fields = next(csvreader) 
	    # extracting each data row one by one 
	    for row in csvreader: 
	        rows.append(row)
	rows=ClassYN(filename,rows)
	return rows

#seed(1)


filename='../SPECTF.csv'
#filename=input("Enter a csv file: ")
dataset=Dataset(filename)
c=[0,0]
for row in dataset:
	c[row[-1]]+=1
print("Total tuples=",c[1]+c[0])
print("Total --- yes=",c[1],"No=",c[0])
#dataset=[[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]]
c_fuzzy(dataset,2)

