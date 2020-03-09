import csv
import numpy as np 

cardinality_count = 2
support_count = 2

def load_data(fname='Test.csv'):
	dataset = []

	with open(fname, 'r') as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			dataset.append(row)

	return np.array(dataset).astype(int)

def bitmap_intersection(l1, l2):	
	return 1 * np.logical_and(l1, l2)

def check_empty(row, cardinality):
	return np.sum(row) >= cardinality

def min_support_check(dataset, new_itemset):
	sup_count = 0

	tmp = 1 * np.logical_and(dataset, new_itemset)
	for row in tmp:
		if np.sum(row) == np.sum(new_itemset):	
			sup_count += 1

	return new_itemset, sup_count

def convert_to_bitvector(ls):
	maxi = max(ls)
	
	bv = np.zeros((maxi, ))
	for i in ls:
		bv[i] = 1

	return bv

def convert_to_itemsets(dataset,bitvector):
	itemset=[]
	for i in range(len(bitvector)):
		if(bitvector[i] == 1):
			itemset.append(i)

	return np.array(itemset)

def row_pruning(dataset, val):
	ls, nm =[], []
	
	for i in range(len(dataset)):
		if np.sum(dataset[i]) >= val:
			ls.append(dataset[i])
			nm.append(i+1)

	return np.array(ls), np.array(nm)

def column_pruning(dataset):
	new = dataset.T
	
	final, nm = row_pruning(new,support_count)

	return final.T, nm

def create_dict(nm):
	dct = {}
	for i,j in enumerate(nm):
		dct[i] = j

	return dct

def compare_dict(dct,final):
	for i in range(len(final)):
		for j in range(len(final[i])):
			final[i][j]=dct[final[i][j]]

	return np.array(final)

def row_enumerate(dataset):
	queue = []
	final = []
	for i in range(len(dataset)):
		queue.append(([i],dataset[i]))
	
	for i in range(len(queue)):
		x, support = min_support_check(dataset,queue[i][1])

		if(check_empty(queue[i][1], cardinality_count) and support>= support_count):
			final.append(convert_to_itemsets(dataset,queue[i][1]))

	while(len(queue)!=0):
		rows, intersection = queue.pop(0)
		last_val = rows[-1]
		
		for i in range(last_val+1,len(dataset)):
			new_list = rows.copy()
			new_list.append(i)
			new_intersect = bitmap_intersection(intersection,dataset[i])
			x, support = min_support_check(dataset,new_intersect)

			if(check_empty(new_intersect,cardinality_count) and support>= support_count):
				queue.append((new_list,new_intersect))
				final.append(convert_to_itemsets(dataset,new_intersect))

	return final

if __name__ == '__main__':
	dataset = load_data()
	print(dataset)
	dataset, x = row_pruning(dataset,cardinality_count)
	dataset, nm = column_pruning(dataset)
	dct = create_dict(nm)
	
	final = row_enumerate(dataset)
	
	final = compare_dict(dct,final)
	final = np.array(sorted(final, key = len))
	
	res = [] 
	
	for x in final:
		if list(x) not in res:
			res.append(list(x))

	print(res)
	