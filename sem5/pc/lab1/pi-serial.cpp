#include <iostream>
#include <omp.h>
#include <iomanip>

using namespace std;

int main() {
    long long int   num_steps = 10000000;
    long double     step = (long double) 1.0 / num_steps,
                    x = 0,
                    s = 0;
    
    double time = omp_get_wtime();
    for(int i = 0; i < num_steps; i++) {
        x = (i+0.5)*step; 
        s += (long double) 4.0 / (1 + x*x);
    }

    s = s*step;

    time =  omp_get_wtime() - time;
    cout << setprecision(10) << s << "\ntime: " << time << "\n"; 

    return 0;
}