''' Greedy Scheduling'''
def schedule(intervals):
    intervals = sorted(intervals, key=lambda times:times[1])
    sc = [intervals[0]]

    for i in range(1,len(intervals)):
        s,e = intervals[i]
        if s < sc[-1][1]:  #s < end of last selected
            pass
        else:
            sc.append((s,e))
    
    return sc

if __name__ == '__main__':
    n = int(input("No.of intervals: ").strip())
    intervals = []
    for i in range(n):
        s,e = [int(x) for x in input().strip().split()]
        intervals.append((s,e))
    
    sc = schedule(intervals)
    print(sc)
