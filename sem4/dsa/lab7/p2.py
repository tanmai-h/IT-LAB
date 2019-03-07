def partition(intervals):
    intervals = sorted(intervals, key=lambda times:times[0])
    partitions = []
    min = 1
    partitions.append([intervals[0]]) 

    for i in range(1,len(intervals)):
        s,e = intervals[i]
        j = 0
        while j < len(partitions) and (s < partitions[j][-1][1]):
            j += 1
        if j == len(partitions):
            partitions.append([(s,e)])
            min += 1
        else:
            partitions[j].append((s,e))
    
    return min, partitions
if __name__ == '__main__':
    n = int(input("No.of intervals: ").strip())
    intervals = []
    for i in range(n):
        s,e = [int(x) for x in input().strip().split()]
        intervals.append((s,e))
    
    min, partitions = partition(intervals)
    print("min resoruces: ", min)
    for p in partitions:
        print(p)