#include <iostream>
#include <pthread.h>

using namespace std;

void *func(void *ptr) {
    cout << (char) *((int *) ptr) << "\n";
}
int main() {
    pthread_t threads[5];
    int id[5];
    char *ms = "qwe";
    for(int i = 0; i < 5; i++) {
        id[i] = pthread_create(&threads[i],NULL,func, (void *) &i);
    }
    for(int i = 0; i < 5; i++) 
        pthread_join(threads[i],NULL);

    return 0;
}                                                               