def mergesort(A, low, high):
    if(low < high):
        mid = (low + high) // 2
        mergesort(A, low, mid)
        mergesort(A, mid+1, high)
        merge(A, low, mid, high)
    else:
        return

def merge(A, low, mid, high):
    L, R = [], []
    l,r,k = 0,0,low
    tt = (low,mid,high)
    print(tt)
    while (k <= mid):
        L.append(A[k])
        k = k+1
    while (k <= high):
        R.append(A[k])
        k = k+1
    l, r, k = 0,0,0
    
    while(l < len(L) and r < len(R)):
        if(L[l] < R[r]):
            A[k] = L[l]
            l = l+1
        else:
            A[k] = R[r]
            r = r+1
        k = k+1
    
    while(l < len(L)):
        A[k] = L[l]
        k = k+1
        l = l+1
    while(r < len(R)):
        A[k] = R[r]
        k = k+1
        r = r+1

def main():
    l = [int(x) for x in input().strip().split()]
    mergesort(l, 0, len(l)-1)
    print(l)
if __name__ == '__main__':
    main()