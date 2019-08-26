from random import randrange
from random import random
from csv import reader
from math import exp

def GetDataset(filename='SPECT.csv'):
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

	return dataset

def Metrics(actual, predicted):
	tp = tn = fp = fn = 0
	ans = 0

	for i in range(len(actual)):
		if actual[i] == 0 and predicted[i] == 0: tn += 1
		if actual[i] == 0 and predicted[i] == 1: fn += 1
		if actual[i] == 1 and predicted[i] == 1: tp += 1
		if actual[i] == 1 and predicted[i] == 0: fp += 1

	ans = tp+tn

	return ans/float(len(actual))*100.0,tp,tn,fp,fn

def ValidationSplit(dataset, n_folds):
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

def AccMetric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

def TrainMLP(dataset, algorithm, n_folds, *args):
	folds = ValidationSplit(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = AccMetric(actual, predicted)
		accuracy,tp,tn,fp,fn = Metrics(actual, predicted)
		print('Precision: ',tp/(tp+fp))
		print('Recall: ',tp/(tp+fn))
		print('Accuracy: ',accuracy)
		print('---------------------------------------')
		scores.append(accuracy)

	return scores

def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]

	return activation

def ForwardPass(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = 1.0 / (1.0 + exp(-activation))
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs

def BackPropError(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * neuron['output'] * (1.0 - neuron['output'])

def UpdateWeight(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']

def BeginTrainer(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		for row in train:
			outputs = ForwardPass(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[int(row[-1])] = 1
			BackPropError(network, expected)
			UpdateWeight(network, row, l_rate)

def RandomWeights(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)

	return network

def predict(network, row):
	outputs = ForwardPass(network, row)
	return outputs.index(max(outputs))

def BackPropInit(train, test, l_rate, n_epoch, n_hidden):
	n_inputs = len(train[0]) - 1
	n_outputs = len(set([row[-1] for row in train]))
	network = RandomWeights(n_inputs, n_hidden, n_outputs)
	BeginTrainer(network, train, l_rate, n_epoch, n_outputs)
	predictions = list()
	for row in test:
		prediction = predict(network, row)
		predictions.append(prediction)
	return(predictions)

filename = 'SPECT.csv'
dataset = GetDataset(filename)

n_folds = 10
l_rate = 0.2
epoch = 50
n_hidden = 5

print("folds %d, l_rate %f, epochs %d, n_hidden %d"%(n_folds,l_rate,epoch,n_hidden))
scores = TrainMLP(dataset, BackPropInit, n_folds, l_rate, epoch, n_hidden)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))