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

def distance(row,mean1,mean2):
	d1=0
	d2=0
	for i in range(len(row)-1):
		d1=d1+((row[i]-mean1[i])*(row[i]-mean1[i]))
		d2=d2+((row[i]-mean2[i])*(row[i]-mean2[i]))
	d1=sqrt(d1)
		
	d2=sqrt(d2)
	if(d1==d2):
		print("Noise:",row)
	if(d2>d1):
		return 0
	else:
		return 1

def center(clusters):
	mean=[]
	l=len(clusters)
	for j in range(len(clusters[0])):
		mean.append(0)
		for i in range(len(clusters)):
			mean[len(mean)-1]=mean[len(mean)-1]+clusters[i][j]
	for i in range(len(mean)):
		mean[i]=mean[i]/l
	return mean

def K_means(dataset):
	k=2
	cluster=[[],[]]
	cluster_assign=[-1 for i in range(len(dataset))]
	dataset_copy=list(dataset)
	cluster[0].append(dataset[255])
	cluster[1].append(dataset[258])
	'''while(len(cluster[0])<1):
		index=randrange(len(dataset_copy))
		print(index)
		cluster[0].append(dataset_copy.pop(index))
	while(len(cluster[1])<1):
		index=randrange(len(dataset_copy))
		print(index)
		cluster[1].append(dataset_copy.pop(index))'''
		
	mean=[0,0]
	mean[0]=center(cluster[0])
	mean[1]=center(cluster[1])
	for itr in range(500):
		for i in range(len(dataset)):
			cluster[distance(dataset[i],mean[0],mean[1])].append(dataset[i])
			cluster_assign[i]= distance(dataset[i],mean[0],mean[1])
		
		m1=center(cluster[0])
		m2=center(cluster[1])
		
		if(m1==mean[0] and m2==mean[1]):
			break
		mean[0]=m1
		mean[1]=m2
		if(itr!=499):
			cluster[0]=[]
			cluster[1]=[]
	c=[0,0]
	for i in range(len(cluster_assign)):
		c[cluster_assign[i]]+=1
	print("No. of elements in cluster-1:",c[0])
	print("No. of elements in cluster-2:",c[1])
	Accuracy(cluster_assign,dataset)
	recall_metric(cluster_assign,dataset)
	precision_metric(cluster_assign,dataset)

def Accuracy(predicted,dataset):
	wr=0
	cr=0
	for i in range(len(dataset)):
		if(predicted[i]==dataset[i][len(dataset[i])-1]):
			cr+=1
		else:
			wr+=1
	print("Accuracy= ",(cr/(cr+wr))*100)

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
K_means(dataset)

