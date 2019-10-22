import random
import naive_bayes_classifier as nb
import pandas

NUM_ITERATIONS=100

def fitness(init_population,population_size,num_features,dataset):
	best_accuracy=0
	best_solution=[0 for i in range(num_features)]
	fitness_list=[]
	for row in init_population:
		accuracy=nb.naive_bayes_classifier(dataset,num_features,row)
		if accuracy>best_accuracy:
			best_accuracy=accuracy
			best_solution=row
		fitness_list.append(accuracy)
	return fitness_list,best_accuracy,best_solution

def selection(fitness_list,dataset,population_size):
	ssum = sum(fitness_list)
	probabilites=[fitness_list[i]/ssum for i in range(len(fitness_list))]
	cumulative_probabilites=[]
	cc=0
	for i in range(len(probabilites)):
		cc+=probabilites[i]
		cumulative_probabilites.append(cc)
	rand = [random.uniform(0.0,1.0) for i in range(len(fitness_list))]
	selected_indices=[]
	for i in rand:
		for j in range(1,len(cumulative_probabilites)):
			if i>cumulative_probabilites[j-1] and i<cumulative_probabilites[j]:
				selected_indices.append(j-1)
				break
	return selected_indices

def crossover(chromosomes):
    no_of_crossovers = 20
    len_chromosome = len(chromosomes[0])
    for i in range(no_of_crossovers):
        chromosome_1 = random.choice(chromosomes)
        chromosome_2 = random.choice(chromosomes)

        # swap the last 25% of both
        start_index = int((3*len_chromosome)/4)
        for i in range(start_index,len_chromosome):
            chromosome_1[i],chromosome_2[i] = chromosome_2[i],chromosome_1[i]

def mutation(chromosomes):
    len_chromosome = len(chromosomes[0])
    # no_of_flips = len(len_chromosome/10)
    no_of_flips = 15
    for chromosome in chromosomes:
        for i in range(no_of_flips):
            index = random.randint(0,len_chromosome-1)
            chromosome[index] = (chromosome[index] + 1)%2


def geneticAlgo(population_size,num_features,dataset):
	# First ---> Evaluate fitness
	for i in range(NUM_ITERATIONS):
		init_population=[[random.randint(0,1) for i in range(num_features)] for j in range(population_size)]
		fitness_list,best_accuracy,best_solution = fitness(init_population,population_size,num_features,dataset)
		selected_indices=selection(fitness_list,dataset,population_size)
		new_population=[init_population[i][:] for i in selected_indices]
		crossover(new_population)
		mutation(new_population)
	return best_accuracy,best_solution

if __name__=='__main__':
	print("Enter name of dataset: ")
	dataset_name=input();
	dataset=pandas.read_csv(dataset_name)
	num_features=len(dataset.columns)-1
	unmodified=[1 for i in range(num_features)] # Since the last column is the output column
	print("Naive Bayes mean accuracy without feature selection: ",nb.naive_bayes_classifier(dataset,num_features,unmodified))
	print("Naive Bayes mean accuracy with feature selection: ",geneticAlgo(30,num_features,dataset))
	population_size=30
	