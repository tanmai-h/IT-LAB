# For creating the list of men and women.
f = open("q1.txt","r")
M = []
W = []
for i in f.readline().split(' '):
	M.append(i)
M[4] = M[4].strip('\n')
for i in f.readline().split(' '):
	W.append(i)
W[4] = W[4].strip('\n')

# For making a map of person to an index(For future purposes)
Men = {}
Women = {}
for i in range(len(M)):
	Men.update({M[i]:i})
for i in range(len(W)):
	Women.update({W[i]:i})

pref_list_man = [ [] for i in range(5)] # Men's preference list indexed
pref_list_women = [ [] for i in range(5)] # Women's preference list indexed

# Creating Men's preference list.
for j in range(5):
	X = f.readline().split(' ')
	X[5] = X[5].strip('\n')
	# print(X)
	for i in range(1,len(X)):
		pref_list_man[Men[X[0]]].append(Women[X[i]])
# print(pref_list_man)

# Creating Women's preference list.
for j in range(5):
	X = f.readline().split(' ')
	X[5] = X[5].strip('\n')
	# print(X)
	for i in range(1,len(X)):
		pref_list_women[Women[X[0]]].append(Men[X[i]])
# print(pref_list_women)

wife = [-1,-1,-1,-1,-1]
husband = [-1,-1,-1,-1,-1]

count = [0,0,0,0,0]

inv_pref_women = [ [] for i in range(5)]
for i in range(len(pref_list_women)):
	for j in range(5):
		inv_pref_women[i].append(pref_list_women[i].index(j))
# print(inv_pref_women) 

free_men = [0,1,2,3,4]

# Main algorithm starts here.
while len(free_men)!=0  and count[free_men[0]] < 5:
	l = pref_list_man[free_men[0]][count[free_men[0]]]
	if husband[l] == -1:
		count[free_men[0]] += 1
		husband[l] = free_men[0]
		wife[free_men[0]] = l
		free_men.pop(0)
	elif inv_pref_women[l][free_men[0]] < inv_pref_women[l][husband[l]]:
		count[free_men[0]] += 1
		free_men.append(husband[l])
		husband[l] = free_men[0]
		wife[free_men[0]] = l
		free_men.pop(0)
	else:
		count[free_men[0]] += 1
# End of main algorithm.

dictio = {}
for i in range(len(W)):
	dictio.update({i:W[i]})

for i in range(5):
	print("Wife of " + M[i] + " is " + dictio[wife[i]])

f.close()