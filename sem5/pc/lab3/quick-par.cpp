#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

int partition (int arr[], int low, int high) {  
    int pivot = arr[high]; 
    int i = (low - 1); 
  
    for (int j = low; j < high; j++) {  
        
        if (arr[j] < pivot) {  
            i++; 
            swap(arr[i], arr[j]);  
        }  
    }  
    swap(arr[i + 1], arr[high]);  

    return (i + 1);  
}   

void quicksort(int arr[], int low, int high) {
	int p;

	if(low < high) {
		p = partition(arr, low, high);

		#pragma omp task
			quicksort(arr, low, p - 1);
		#pragma omp task
			quicksort(arr, p + 1, high);
	}
}


int main() {
    int n = 1e6; 
	cout << ""; cin >> n;
	int a[n];

	for(int i = 0; i < n; i++) 
		a[i] = rand()%((int)1e9+7);

	double t = omp_get_wtime();
    #pragma omp parallel
	{
		#pragma omp single
			quicksort(a,0,n-1);
	}
	t = omp_get_wtime()-t;

    // for(int i = 0; i < n; i++)
	// 	cout << a[i] << " ";    
    cout << "\nTime: " << t << "\n";
    return 0;
}

