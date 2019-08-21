#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

int default_squares ( int n) {
    int i,j;
    int total = 0;

    #pragma omp parallel shared (n) private (i,j)
    #pragma omp for reduction (+:total)
    for ( i = 1; i <= n; i++ )
        if(i == (int)sqrt(i) * (int)sqrt(i))
            total += 1; 

    return total;
}

int static_squares ( int n ) {
    int i,j;
    int total = 0;

    #pragma omp parallel shared (n) private (i,j)
    # pragma omp for reduction ( + : total ) schedule ( static, 100 )
    for ( i = 1; i <= n; i++ )
        if(i == (int)sqrt(i) * (int)sqrt(i))
            total += 1;

    return total;
}

int dynamic_squares ( int n ) {
    int i,j;
    int total = 0;

    #pragma omp parallel shared (n) private (i,j)
    #pragma omp for reduction (+:total) schedule (dynamic,100)
    for ( i = 1; i <= n; i++ ) 
        if(i == (int)sqrt(i) * (int)sqrt(i))
            total += 1;

    return total;
}

int guided_squares ( int n ) {
    int i,j;
    int total = 0;

    #pragma omp parallel shared (n) private (i,j)
    #pragma omp for reduction (+:total) schedule (guided,100)
    for ( i = 1; i <= n; i++ )
        if(i == (int)sqrt(i) * (int)sqrt(i))
            total += 1;

    return total;
}

int main ( int argc, char *argv[] ){
    omp_set_num_threads(8);
    int n, low = 1, high = 265000;
    int squares;
    double times[4]; 

    printf ( "Loop Schedule\n" );
    printf ( "                           Default        Static       Dynamic       Guided\n" );
    printf ( "         N     num Squares Till N\n");

    n = low;
    while (n <= high) {
        times[0] = omp_get_wtime ();
        squares = default_squares (n);
        times[0] = omp_get_wtime () - times[0];

        times[1] = omp_get_wtime ();
        squares = static_squares (n);
        times[1] = omp_get_wtime () - times[1];

        times[2] = omp_get_wtime ();
        squares = dynamic_squares (n);
        times[2] = omp_get_wtime () - times[2];

        times[3] = omp_get_wtime ();
        squares = guided_squares (n);
        times[3] = omp_get_wtime () - times[3];

        printf ( "  %8d  %8d  %12f  %12f  %12f %12f\n", n, squares, times[0], times[1], times[2], times[3] );

        n = n * 2;
    }

    return 0;
}
