#include <iostream>
#include <omp.h>

using namespace std;

int main() {
    omp_set_num_threads(4);
    
    #pragma omp parallel 
    {
        cout <<" Hello. thread num  -  " << omp_get_thread_num() << "\n";
    }
    return 0;
}
