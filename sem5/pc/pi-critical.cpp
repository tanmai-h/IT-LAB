#include <iostream>
#include <cstring>
#include <omp.h>
#include <iomanip>

using namespace std;

int main() {
    int n = 10; omp_set_num_threads(n);
    
    long long int   num_steps = 10000000;
    int             batch = num_steps / n;
    long double          step = (long double) 1.0 / num_steps,
                    sum = 0,
                    pi = 0
                    ;

    double time = omp_get_wtime();
    #pragma omp parallel
    {
        int t = omp_get_thread_num();
        double aux = 0;
        for(int i = t*batch; i < (t+1)*batch; i++) {
            double x = (i+0.5)*step;
            aux += (double) 4.0 / (1 + x*x);
        }

        #pragma omp critical 
        {
            sum += aux*step;
        }
    }


    time =  omp_get_wtime() - time;
    cout << setprecision(10) << sum << "\ntime: " << time << "\n"; 

    return 0;
}
