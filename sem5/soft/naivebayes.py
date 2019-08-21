import csv, math

def GetDataset(filename):
	attr=[]
	rows=[]
	with open(filename,'r') as csvfile:
		csvreader = csv.reader(csvfile)
		attr = next(csvreader)
		for row in csvreader:
			rows.append(row)
	
	return rows,attr

def TrainTestSplit(data_rows,i,k):
	l = len(data_rows)
	s_test = l*(i-1)//k
	e_test = l*i//k

	if s_test == 0:
		s_train = e_test
		e_train = l
	
		return [data_rows[s_train:e_train],data_rows[s_test:e_test]]

	elif e_test == l:
		s_train = 0
		e_train = s_test
		
		return [data_rows[s_train:e_train],data_rows[s_test:e_test]]
	
	else:
		new_data_rows = []
		for i in range(s_test):
			new_data_rows.append(data_rows[i])
		for j in range(e_test,l):
			new_data_rows.append(data_rows[j])

		return [new_data_rows,data_rows[s_test:e_test]]

def TrainBayes(Rows,attr,test_set):
	nyes,nno = 0,0

	for i in range(len(Rows)):
		if Rows[i][0]=="Yes":
			nyes+=1
		if Rows[i][0]=="No":
			nno+=1

	proYes=float(nyes)/(nyes+nno)
	proNo=float(nno)/(nyes+nno)

	p1yes=[0]*(len(attr)-1)
	p1no=[0]*(len(attr)-1)
	p0no=[0]*(len(attr)-1)
	p0yes=[0]*(len(attr)-1)

	for j in range(len(Rows)):
		for i in range(1,len(attr)):
			if Rows[j][i]=='1' and Rows[j][0]=="Yes":
				p1yes[i-1]+=1
			if Rows[j][i]=='1' and Rows[j][0]=="No":
				p1no[i-1]+=1
			if Rows[j][i]=='0' and Rows[j][0]=="Yes":
				p0yes[i-1]+=1
			if Rows[j][i]=='0' and Rows[j][0]=="No":
				p0no[i-1]+=1
		
	for i in range(len(p1yes)):
		p1no[i]=p1no[i]/float(nno)
		p1yes[i]=p1yes[i]/float(nyes)
		p0no[i]=p0no[i]/float(nno)
		p0yes[i]=p0yes[i]/float(nyes)
	
	acc=0

	for j in range(len(test_set)):
		yes_p = proYes
		no_p = proNo
		for i in range(1,len(attr)):
			if test_set[j][i]=='0':
				yes_p *= p0yes[i-1]
				no_p *= p0no[i-1]
			elif test_set[j][i]=='1':
				yes_p *= p1yes[i-1]
				no_p *= p1no[i-1]

		if yes_p > no_p:
			max_prob='Yes'
		else:
			max_prob='No'
		if test_set[j][0]==max_prob:
			acc+=1

	result = float(acc)/len(test_set)
	result *= 100

	return result

def main():
	filename = "SPECT.csv"
	rows,attr = GetDataset(filename)
	accs = []

	k_fold = 10
	for i in range(1,k_fold+1):	
		tr,test = TrainTestSplit(rows,i,k_fold)
		acc = TrainBayes(tr,attr,test)
		accs.append(acc)
	
	avg = 0
	for i in range(len(accs)):
		print('Fold:', i, ' -' , math.ceil(accs[i]))
		avg += accs[i]

	print('Avg acc', avg  / len(accs))

if __name__ == '__main__':
	main()