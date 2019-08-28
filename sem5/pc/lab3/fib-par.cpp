#include <iostream>
#include <omp.h>

using namespace std;

int fib(int n) {
    if(n <= 1) 
        return n;
    int x,y;
    #pragma omp task// shared(x)
        x = fib(n-1);
    #pragma omp task// shared(y)
        y = fib(n-2);

    return x+y;       
}
int main() {
    int n;
    cout << " "; cin >> n;

    double t = omp_get_wtime();
    #pragma omp parallel
    {
        #pragma omp single
        {
            int f = fib(n); t = omp_get_wtime()-t;
            cout << "Fib: " << f <<"; time = " << t << "\n";
        }
    }
    return 0;
}