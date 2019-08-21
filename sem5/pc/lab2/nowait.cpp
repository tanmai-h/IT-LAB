#include<bits/stdc++.h>
#include<omp.h>

#define M 100000000
#define N 100000000
#define P 100000000
#define Q 100000000

using namespace std;

int main(){
    int *A = new int [M], *B = new int[N], *C = new int[P], *D = new int [Q];
	double start = omp_get_wtime();

	for(int i = 0; i < M; i++)
		B[i] = A[i]*2+1;

	for(int i = 0;i < N; i++)
		C[i] = D[i]-D[i-1];

	double end = omp_get_wtime();
	printf("Without nowait Time: %f\n",end-start);
}