#include<bits/stdc++.h>
#include<omp.h>

using namespace std;

int main(){
    int *B = new int[100000000], *C = new int[100000000];
	double start = omp_get_wtime();

	for(int i = 0; i < 100000000; i++)
		B[i] =2*i - 1;

	for(int i = 0;i < 100000000; i++)
		C[i] = 5*i + 9;

	double end = omp_get_wtime();
	cout << "without nowait Time: " << end-start << "\n";;
}