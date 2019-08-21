#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

int prime_default ( int n) {
    int i;
    int j;
    int prime;
    int total = 0;

    #pragma omp parallel shared (n) private (i,j,prime)

    #pragma omp for reduction (+:total)
    for ( i = 2; i <= n; i++ ) {
        prime = 1;
        for ( j = 2; j < i; j++ ) {
            if ( i % j == 0 ) {
                prime = 0;
                break;
            }
        }
        total = total + prime;
    }

    return total;
}

int prime_static ( int n ) {
    int i;
    int j;
    int prime;
    int total = 0;

    # pragma omp parallel shared ( n ) private ( i, j, prime )

    # pragma omp for reduction ( + : total ) schedule ( static, 100 )
    for ( i = 2; i <= n; i++ ) {
        prime = 1;

        for ( j = 2; j < i; j++ ) {
            if ( i % j == 0 ) {
                prime = 0;
                break;
            }
        }
        total = total + prime;
    }

    return total;
}

int prime_dynamic ( int n ) {
    int i;
    int j;
    int prime;
    int total = 0;

    #pragma omp parallel shared (n) private (i,j,prime)

    #pragma omp for reduction (+:total) schedule (dynamic,100)
    for ( i = 2; i <= n; i++ ) {
        prime = 1;

        for ( j = 2; j < i; j++ ) {
            if ( i % j == 0 ) {
                prime = 0;
                break;
            }
        }
        total = total + prime;
    }

    return total;
}

int prime_guided ( int n ) {
    int i;
    int j;
    int prime;
    int total = 0;

    #pragma omp parallel shared (n) private (i,j,prime)

    #pragma omp for reduction (+:total) schedule (guided,100)
    for ( i = 2; i <= n; i++ ) {
        prime = 1;

        for ( j = 2; j < i; j++ ) {
            if ( i % j == 0 ) {
                prime = 0;
                break;
            }
        }
        total = total + prime;
    }

    return total;
}

int main ( int argc, char *argv[] ){
    omp_set_num_threads(8);
    int n, low = 1, high = 265000;
    int primes;
    double times[4]; 

    printf ( "Loop Schedule\n" );
    printf ( "                           Default        Static       Dynamic       Guided\n" );
    printf ( "         N     num Primes Till N\n");

    n = low;
    while (n <= high) {
        times[0] = omp_get_wtime ();
        primes = prime_default (n);
        times[0] = omp_get_wtime () - times[0];

        times[1] = omp_get_wtime ();
        primes = prime_static (n);
        times[1] = omp_get_wtime () - times[1];

        times[2] = omp_get_wtime ();
        primes = prime_dynamic (n);
        times[2] = omp_get_wtime () - times[2];

        times[3] = omp_get_wtime ();
        primes = prime_guided (n);
        times[3] = omp_get_wtime () - times[3];

        printf ( "  %8d  %8d  %12f  %12f  %12f %12f\n", n, primes, times[0], times[1], times[2], times[3] );

        n = n * 2;
    }

    return 0;
}