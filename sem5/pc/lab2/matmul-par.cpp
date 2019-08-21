#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

void print(int** matrix, int m, int n) {
	for(int i = 0; i < m;i++) {
		for(int j = 0;j < n;j++) {
			cout << matrix[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";
}

int** init(int m, int n){
	int** matrix = new int * [m]; 
	for(int i = 0; i < m; i++)
		matrix[i]= new int [n];

	for(int i = 0;i < m; i++){
		for(int j = 0; j < n; j++){
			matrix[i][j] = (rand()%100)+1; 
		}
	}
	return matrix;
}

int** matmul(int** A,int** B,int m,int n,int p,double &time){
	int ** result = new int * [m]; 
	for(int i = 0; i < m;i++) {
		result[i] = new int[p];
        for(int j = 0; j < p; j++) 
            result[i][j] = 0;
    } 

	omp_set_num_threads(10);
	
    double start = omp_get_wtime();
	#pragma omp parallel
	{
		#pragma omp for
		for(int i = 0;i < m; i++){
			for(int j = 0;j < p; j++){
				for(int k = 0; k < n; k++){
					result[i][j] += A[i][k]*B[k][j];
				}
			}
		}
	}
	double end = omp_get_wtime();
	time = end-start;
	return result;
}


int main() {
	int x = 300,y = 500 ,z = 700;
    
	int** a = init(x,y);
	int** b = init(y,z); 
    double time = 0;
	int **result = matmul(a,b,x,y,z, time);

	// print(result, x, z);
	cout << "Parallel matmul Time : " << time << "\n";
    
}
