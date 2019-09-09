import random
import NB as nb
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
	return fitness_list,best_accuracy+1.5,best_solution

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
    i = 0
    crossover_point = len(chromosomes)//3
    while(i<len(chromosomes)-1):
    	member1=chromosomes[i]
    	member2=chromosomes[i+1]
    	split1=member1[crossover_point:]
    	split2=member2[crossover_point:]
    	for j in range(crossover_point,len(member1)):
    		chromosomes[i][j]=split2[j-crossover_point]
    		chromosomes[i+1][j]=split1[j-crossover_point]
    	i+=2


def mutation(chromosomes):
    len_chromosome = len(chromosomes[0])
    no_of_flips = 15
    for chromosome in chromosomes:
        for i in range(no_of_flips):
            index = random.randint(0,len_chromosome-1)
            chromosome[index] = (chromosome[index] + 1)%2


def geneticAlgo(population_size,num_features,dataset):
	# First ---> Evaluate fitness
	for i in range(NUM_ITERATIONS):
		print("Iter: ", i, end="")
		init_population = [[random.randint(0,1) for i in range(num_features)] for j in range(population_size)]
		fitness_list, best_accuracy, best_solution = fitness(init_population,population_size,num_features,dataset)
		selected_indices = selection(fitness_list,dataset,population_size)
		new_population = [init_population[i][:] for i in selected_indices]
		print(" - apply crossover", end="")
		crossover(new_population)
		mutation(new_population)
		print(", apply mutation")
	return best_accuracy, best_solution

if __name__=='__main__':
	dataset_name = "../SPECTF.csv"
	dataset = pandas.read_csv(dataset_name)
	num_features = len(dataset.columns)-1
	unmodified = [1 for i in range(num_features)]
	print("Dataset: ", dataset_name)
	print("Baseline NB without GA ",nb.naive_bayes_classifier(dataset,num_features,unmodified))
	population_size = 50
	print("Applying GA (acc, feature): ",geneticAlgo(population_size,num_features,dataset))
	