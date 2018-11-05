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

    while (k <= mid):
        L[l] = A[k]
        l = l+1
        k = k+1
    while (k <= high):
        R[r] = A[k]
        r = r+1
        k = k+1
    l, r, k = 0,0,0
    
    while(l < len(L) and r < len(R)):
        if()