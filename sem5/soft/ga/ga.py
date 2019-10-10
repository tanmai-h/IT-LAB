import pandas as pd
import NB as nb
import random

def EvalFitness(InitGeneration, population_size, num_features, dataset):
	acc, soln, FitList = 0, [0 for i in range(num_features)], []
	FitList = []
	for row in InitGeneration:
		accuracy = nb.naive_bayes_classifier(dataset,num_features,row)
		if accuracy > acc:
			acc = accuracy
			soln = row
		FitList.append(accuracy)
	return FitList, acc, soln

def SelectFeatures(FitList,dataset,population_size):
	ssum = sum(FitList)
	probabilites = [FitList[i]/ssum for i in range(len(FitList))]
	TotalProb = []
	cc = 0
	for i in range(len(probabilites)):
		cc += probabilites[i]
		TotalProb.append(cc)
	rand = [random.uniform(0.0,1.0) for i in range(len(FitList))]
	BestIndices = []
	for i in rand:
		for j in range(1,len(TotalProb)):
			if i > TotalProb[j-1] and i<TotalProb[j]:
				BestIndices.append(j-1)
				break
	return BestIndices

def TournmentCrossover(chromosomes):
	i = 0
	TournmentCrossover_point = len(chromosomes)//3
	while(i < len(chromosomes)-1):
		m1, m2 = chromosomes[i],chromosomes[i+1]
		s1, s2 =  m1[TournmentCrossover_point:], m2[TournmentCrossover_point:]

		for j in range(TournmentCrossover_point,len(m1)):
			chromosomes[i][j]=s2[j-TournmentCrossover_point]
			chromosomes[i+1][j]=s1[j-TournmentCrossover_point]
		i += 2

def mutation(chromosomes):
    len_chromosome = len(chromosomes[0])
    no_of_flips = 15
    for chromosome in chromosomes:
        for i in range(no_of_flips):
            index = random.randint(0,len_chromosome-1)
            chromosome[index] = (chromosome[index] + 1)%2


def geneticAlgo(population_size,num_features,dataset):
	MAX_ITER =100
	for i in range(MAX_ITER):
		print("Iter: ", i, end="")
		InitGeneration = [
							[random.randint(0,1) for i in range(num_features)] 
							for j in range(population_size)
							]
							
		FitList, acc, soln = EvalFitness(InitGeneration,population_size,num_features,dataset)
		BestIndices = SelectFeatures(FitList,dataset,population_size)
		NewGeneration = [InitGeneration[i][:] for i in BestIndices]
		print(" - apply TournmentCrossover", end="")
		TournmentCrossover(NewGeneration)
		mutation(NewGeneration)
		print(", apply mutation")
	return acc, soln

if __name__=='__main__':
	dataset_name = "../SPECTF.csv"
	dataset = pd.read_csv(dataset_name)
	num_features = len(dataset.columns)-1
	unmodified = [1 for i in range(num_features)]
	print("Dataset: ", dataset_name)
	print("Baseline NB without GA ",nb.naive_bayes_classifier(dataset,num_features,unmodified))
	population_size = 50
	print("Applying GA (acc, feature): ",geneticAlgo(population_size,num_features,dataset))
	