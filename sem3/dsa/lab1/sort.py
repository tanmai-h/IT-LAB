#bubble
def sort(a = []):
	for i in range(0, len(a)):
		for j in range(0, len(a)-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]

print("enter list of nums: ")
a = [int(x) for x in input().split()]
sort(a)
print(a)
