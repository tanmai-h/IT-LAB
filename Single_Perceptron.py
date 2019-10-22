from csv import reader
from random import randrange

def statCalc(actual, predicted):
	tp=0
	tn=0
	fp=0
	fn=0
	ans = 0
	for i in range(len(actual)):
		if actual[i] == 0:
			if predicted[i]==0:
				tn+=1
			else:
				fn+=1
		else:
			if predicted[i]==1:
				tp+=1
			else:
				fp+=1
	ans=tp+tn
	return ans/float(len(actual))*100.0,tp,tn,fp,fn

def CVSplit(dataset, n_folds):
	split = []
	dataset_copy = list(dataset)
	fold_size = int(len(dataset)/n_folds)
	for i in range(n_folds):
		fold = []
		while len(fold)<fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		split.append(fold)
	return split
 
def testAndPrint(dataset, n_folds, alpha, epochs):
	folds = CVSplit(dataset, n_folds)
	scores = []
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = []
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = perceptron(train_set, test_set,alpha,epochs)
		actual = [row[-1] for row in fold]
		accuracy,tp,tn,fp,fn = statCalc(actual, predicted)
		print('Precision: ',tp/(tp+fp))
		print('Recall: ',tp/(tp+fn))
		print('Accuracy: ',accuracy)
		print('---------------------------------------')
		scores.append(accuracy)
	return scores
 
def optimizeParam(train, alpha, epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(epoch):
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			weights[0] = weights[0] + alpha * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + alpha * error * row[i]
	return weights

def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0
  
def perceptron(train, test, alpha, epoch):
	predictions = []
	weights = optimizeParam(train, alpha, epoch)
	for row in test:
		prediction = predict(row, weights)
		predictions.append(prediction)
	return(predictions)
 
# filename = 'SPECT.csv'
filename = 'SPECTF.csv'
# filename = 'IRIS.csv'
dataset = []
data=open(filename,'r')
file = reader(data)
for i in file:
	if not i:
		continue
	dataset.append(i)
for j in range(len(dataset[0])):
	for i in range(len(dataset)):
		dataset[i][j]=float(dataset[i][j])
n_folds=int(input("Enter number of folds: "))
alpha = float(input("Enter learning rate: "))
epoch = int(input("Enter number of epochs: "))
scores = testAndPrint(dataset, n_folds, alpha, epoch)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))