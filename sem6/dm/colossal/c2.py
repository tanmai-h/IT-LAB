import csv
import numpy as np 

cardinality_count=2
support_count=2

def load_data() :
	dset = []
	with open('Test.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count != 0 :
				dset.append(row)
				for i in range(len(row)):
					row[i]=int(row[i])
			line_count += 1
	return dset

def bitmap_intersection(l1,l2):	
	l3=[]
	for i in range(len(l1)):
		l3.append(l1[i] & l2[i])
	return l3

def check_empty(row,cardinality):
	card=0
	for i in range(len(row)):
		if(row[i]==1):
			card+=1
	if(card>=cardinality):
		return True
	else:
		return False

def min_support_check(dataset,new_itemset):
	support_count=0
	for i in range(len(dataset)):
		supported=True
		for j in range(len(new_itemset)):
			if(dataset[i][j]!=1 and new_itemset[j]==1):
				supported=False
		if(supported):
			support_count+=1
	return new_itemset,support_count

def convert_to_bitvector(ls):
	maxi=max(ls)
	bv=[0 for i in range(maxi)]
	for i in ls:
		bv[i]=1
	return bv

def convert_to_itemsets(dataset,bitvector):
	itemset=[]
	for i in range(len(bitvector)):
		if(bitvector[i]==1):
			itemset.append(i)
	return itemset

def row_pruning(dataset,val):
	ls=[]
	nm=[]
	for i in range(len(dataset)):
		if sum(dataset[i])>=val:
			ls.append(dataset[i])
			nm.append(i+1)
	return ls,nm

def column_pruning(dataset):
	new=np.transpose(dataset)
	final,nm=row_pruning(new,support_count)
	return np.ndarray.tolist(np.transpose(final)),nm

def create_dict(nm):
	dct={}
	for i,j in enumerate(nm):
		dct[i]=j
	return dct

def compare_dict(dct,final):
	for i in range(len(final)):
		for j in range(len(final[i])):
			final[i][j]=dct[final[i][j]]
	return final

def row_enumerate(dataset):
	queue=[]
	final=[]
	for i in range(len(dataset)):
		queue.append(([i],dataset[i]))
	# print(queue)
	for i in range(len(queue)):
		x,support=min_support_check(dataset,queue[i][1])
		if(check_empty(queue[i][1],cardinality_count) and support>=support_count):
			# queue.append((new_list,new_intersect))
			# print(queue[i][0],convert_to_itemsets(dataset,queue[i][1]),support)
			final.append(convert_to_itemsets(dataset,queue[i][1]))

	while(len(queue)!=0):
		(rows,intersection)=queue.pop(0)
		# print(rows,intersection,convert_to_itemsets(dataset,intersection))
		last_val=rows[-1]
		for i in range(last_val+1,len(dataset)):
			new_list=rows.copy()
			new_list.append(i)
			new_intersect=bitmap_intersection(intersection,dataset[i])
			x,support=min_support_check(dataset,new_intersect)
			if(check_empty(new_intersect,cardinality_count) and support>=support_count):
				queue.append((new_list,new_intersect))
				# print(new_list,convert_to_itemsets(dataset,new_intersect),support)
				final.append(convert_to_itemsets(dataset,new_intersect))
	return final

if __name__ == '__main__':
	dataset = load_data()
	# print(dataset)
	dataset,x=row_pruning(dataset,cardinality_count)
	dataset,nm=column_pruning(dataset)
	dct=create_dict(nm)
	# print(nm)
	# print(dct)
	# print(dataset)
	final=row_enumerate(dataset)
	# print(final)
	final=compare_dict(dct,final)
	final.sort(key=len)
	res = [] 
	[res.append(x) for x in final if x not in res]
	print(res)
	# print(final)
