#include <iostream>
#include <omp.h>

using namespace std;

int fib(int n) {
    if(n <= 1) 
        return n;
    return fib(n-1) + fib(n-2); 
}
int main() {
    int n;
    cout << " "; cin >> n;

    double t = omp_get_wtime();
    int f = fib(n); t = omp_get_wtime()-t;
    cout << "Fib: " << f <<"; time = " << t << "\n";
    return 0;
}