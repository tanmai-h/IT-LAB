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
	cout << "1st 20 elements of B: ";
	for(int i = 0; i < 20; i++) cout << B[i] << " ";
	cout << "\n";
	cout << "1st 20 elements of C: ";
	for(int i = 0; i < 20; i++) cout << C[i] << " ";
	cout << "\nwithout nowait Time: " << end-start << "\n";
}