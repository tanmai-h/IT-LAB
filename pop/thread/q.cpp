#include <bits/stdc++.h>
#include <time.h> 
using namespace std;
void delay(int number_of_seconds) 
{ 
    // Converting time into milli_seconds 
    int milli_seconds = 100000 * number_of_seconds; 
  
    // Stroing start time 
    clock_t start_time = clock(); 
  
    // looping till required time is not acheived 
    while (clock() < start_time + milli_seconds) 
        ; 
} 
int main(int argc, char const *argv[])
{
    for(int i = 0; i <= 10; i++) {
       delay(1); 
        printf("%d seconds have passed\n", i + 1); 
    }
    return 0;
}
